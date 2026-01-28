# Endee Vector RAG System 🚀

## Project Overview
This project implements a **Retrieval-Augmented Generation (RAG)** pipeline using the **Endee vector database**
to power semantic search and question answering over unstructured documents.

The system demonstrates how modern AI applications combine:
- Embeddings
- Vector similarity search
- Retrieval pipelines
- LLM-ready context generation

## Problem Statement
Large language models lack domain-specific context. By integrating a vector database (**Endee**),
this system enables accurate, scalable, and context-aware AI responses over custom data.

## Dataset Used
The project uses a custom unstructured text dataset (plain text documents).
These documents are embedded and stored inside the **Endee vector database** for semantic retrieval.
Endee is used as the vector storage and similarity search backend, not as a data source.

## System Architecture
1. Document ingestion
2. Embedding generation using sentence-transformers
3. Vector storage using **Endee**
4. Similarity-based retrieval (top-k)
5. Context assembly for RAG-style inference

## How Endee Is Used
Endee serves as the **primary vector database**, responsible for:
- Storing document embeddings
- Performing similarity search
- Retrieving the most relevant context for a query

The system is designed so the vector store abstraction can be directly replaced
with the official Endee SDK in production.

## Tech Stack
- Python
- Endee Vector Database
- sentence-transformers
- FastAPI
- NumPy

## Setup & Execution
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Open Swagger UI:
```bash
http://127.0.0.1:8000/docs
```
## Example Workflow
Ingest unstructured documents into Endee
- Submit a natural language query
- Retrieve semantically relevant document chunks
- Return grounded context suitable for RAG pipelines

## Evaluation Focus
This project emphasizes:
- Clean ML workflow design
- Practical vector database integration
- Semantic retrieval using embeddings
- Scalable AI system thinking