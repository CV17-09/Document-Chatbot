from fastapi import FastAPI, UploadFile, File
from dotenv import load_dotenv
from openai import OpenAI
import chromadb
import os
import pypdf
import docx

load_dotenv()

app = FastAPI()
client = OpenAI()

chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection(name="documents")


def read_file(path, filename):
    if filename.endswith(".pdf"):
        reader = pypdf.PdfReader(path)
        return "\n".join(page.extract_text() or "" for page in reader.pages)

    if filename.endswith(".docx"):
        document = docx.Document(path)
        return "\n".join(p.text for p in document.paragraphs)

    if filename.endswith(".txt"):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    return ""


def chunk_text(text, size=500, overlap=100):
    chunks = []
    start = 0

    while start < len(text):
        chunks.append(text[start:start + size])
        start += size - overlap

    return chunks


def embed(text):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding


@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    os.makedirs("data", exist_ok=True)

    file_path = f"data/{file.filename}"

    with open(file_path, "wb") as f:
        f.write(await file.read())

    text = read_file(file_path, file.filename)

    if not text:
        return {"error": "Could not read file"}

    chunks = chunk_text(text)

    for i, chunk in enumerate(chunks):
        collection.add(
            ids=[f"{file.filename}_{i}"],
            embeddings=[embed(chunk)],
            documents=[chunk],
            metadatas=[{"source": file.filename, "chunk": i}]
        )

    return {"message": "Document uploaded", "chunks": len(chunks)}


@app.get("/ask")
def ask(question: str):
    question_embedding = embed(question)

    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=3
    )

    chunks = results["documents"][0]
    sources = results["metadatas"][0]

    context = "\n\n".join(chunks)

    prompt = f"""
Answer the question using only the context below.
If the answer is not in the context, say:
"I do not know based on the uploaded document."

Context:
{context}

Question:
{question}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return {
        "answer": response.choices[0].message.content,
        "sources": sources,
        "retrieved_chunks": chunks
    }