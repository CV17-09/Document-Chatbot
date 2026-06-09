# Document Q&A RAG Chatbot

## Overview

The Document Q&A RAG Chatbot is an AI-powered application that allows users to upload documents and ask questions about their contents. The system uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from uploaded documents and generate accurate, context-aware responses grounded in the source material.

Unlike traditional chatbots that rely solely on a language model's training data, this application retrieves relevant document sections before generating an answer, helping reduce hallucinations and improve response reliability.

---

## Features

* Upload PDF, TXT, and DOCX documents
* Ask natural language questions about uploaded files
* Retrieve relevant document chunks using vector similarity search
* Generate grounded answers with Large Language Models (LLMs)
* Display source references used to generate responses
* Reduce hallucinations through document-based retrieval
* Persistent vector storage using ChromaDB
* REST API built with FastAPI

---

## Tech Stack

### Backend

* Python
* FastAPI
* OpenAI API

### Retrieval & Storage

* ChromaDB
* Vector Embeddings

### Document Processing

* PyPDF
* python-docx

### AI Frameworks

* Retrieval-Augmented Generation (RAG)
* OpenAI Embeddings
* OpenAI Chat Models

---

## AI Concepts Demonstrated

### Tokenization

Documents and user queries are converted into tokens that can be processed by language models.

### Chunking

Large documents are divided into smaller sections to improve retrieval performance.

### Chunk Overlap

Overlapping chunks preserve context between document sections and improve answer quality.

### Embeddings

Text is transformed into high-dimensional vector representations that capture semantic meaning.

### Vector Database

Embeddings are stored in ChromaDB for efficient retrieval.

### Similarity Search

Relevant document chunks are identified by comparing vector similarity between user queries and stored document embeddings.

### Retrieval-Augmented Generation (RAG)

Retrieved document content is provided to the LLM as context before answer generation.

### Prompt Engineering

Structured prompts guide the model to answer only from retrieved document content.

### Large Language Models (LLMs)

OpenAI models generate natural language responses grounded in retrieved information.

---

## System Architecture

1. User uploads a document.
2. Document text is extracted.
3. Text is split into chunks with overlap.
4. Embeddings are generated for each chunk.
5. Embeddings are stored in ChromaDB.
6. User submits a question.
7. The question is embedded.
8. Similarity search retrieves the most relevant chunks.
9. Retrieved context is passed to the LLM.
10. The model generates a grounded answer with source references.

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/document-chatbot.git
cd document-chatbot
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

Mac/Linux:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

---

## Running the Application

Start the FastAPI server:

```bash
uvicorn app:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

Use the interactive Swagger UI to:

* Upload documents
* Ask questions
* View generated responses and sources

---

## Example Workflow

### Upload

Upload:

```text
software_requirements.pdf
```

### Ask

```text
What authentication method does the system use?
```

### Response

```text
The system uses OAuth 2.0 authentication for user login and API access.

Source:
software_requirements.pdf (Chunk 12)
```

---

## Future Improvements

* User authentication and authorization
* Chat history and conversation memory
* Multiple document collections
* PDF source highlighting
* Streaming responses
* Docker deployment
* Cloud hosting
* Multi-user support
* Advanced reranking techniques
* Support for additional file formats

---

## Learning Outcomes

This project demonstrates practical experience with:

* Retrieval-Augmented Generation (RAG)
* FastAPI development
* Vector databases
* Embedding models
* Semantic search
* Prompt engineering
* LLM integration
* Document processing pipelines
* AI application development

---

## License

This project is intended for educational and portfolio purposes.
