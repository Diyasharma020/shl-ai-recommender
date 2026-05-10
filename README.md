# SHL Conversational Assessment Recommender

An AI-powered conversational recommendation platform that suggests relevant SHL assessments using semantic retrieval, conversational API logic, and intelligent recruiter query matching.

---

## Features

* Conversational recommendation API
* Semantic assessment retrieval
* Clarifying question support
* Assessment comparison support
* Dynamic recommendation refinement
* Job description URL extraction
* Skill detection system
* Public frontend and backend deployment

---

## Tech Stack

* Python
* FastAPI
* Streamlit
* Scikit-learn
* TF-IDF Vectorization
* Cosine Similarity
* BeautifulSoup
* Requests

---

## System Architecture

Frontend (Streamlit)
↓
FastAPI Conversational API
↓
Semantic Retrieval Engine
↓
TF-IDF Vectorization
↓
Cosine Similarity Ranking
↓
SHL Assessment Recommendations

---

## API Endpoints

### GET /

Returns API status message.

### GET /health

Health check endpoint.

### POST /chat

Conversational recommendation endpoint.

Example Request:

```json
{
  "message": "Looking for backend engineer with Java SQL APIs debugging"
}
```

---

## Conversational Features

The API supports:

* Clarifying questions for ambiguous recruiter queries
* Assessment comparison behavior
* Contextual recommendation refinement
* Grounded recommendation reasoning

---

## Retrieval Approach

The recommendation engine uses semantic retrieval techniques to match recruiter queries against SHL assessment metadata and descriptions.

The deployed system uses:

* TF-IDF vectorization
* cosine similarity ranking
* contextual skill matching

Initial experimentation included SentenceTransformers and FAISS vector search before deployment optimization.

---

## Evaluation

The system was evaluated using:

* Precision@K
* semantic relevance testing
* grounded recommendation validation
* recruiter query testing

---

## Deployment

### Frontend

Streamlit Cloud

### Backend

Render

---

## Live Deployment

### Frontend

https://diyasharma020-shl-ai-recommender-frontendstreamlit-app-1y5id1.streamlit.app/

### Backend

https://shl-ai-backend-yn8p.onrender.com/

---

## Author

Diya Sharma
