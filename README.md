# SHL Conversational Assessment Recommender

An AI-powered conversational recommendation system that suggests relevant SHL assessments using semantic search, embeddings, and FAISS vector similarity.

## Features

- Conversational recommendation API
- Clarifying questions
- Assessment comparison support
- Semantic retrieval using embeddings
- FAISS vector similarity search
- Streamlit frontend
- FastAPI backend
- SHL assessment recommendation engine

## Tech Stack

- Python
- FastAPI
- Streamlit
- SentenceTransformers
- FAISS
- BeautifulSoup
- Uvicorn

## Architecture

Frontend (Streamlit)
↓
FastAPI Backend
↓
SentenceTransformer Embeddings
↓
FAISS Vector Search
↓
SHL Assessment Recommendations

## API Endpoints

### GET /health

Health check endpoint.

### POST /chat

Conversational recommendation endpoint.

Example Request:

```json
{
  "message": "Looking for backend engineer with Java SQL APIs debugging"
}
