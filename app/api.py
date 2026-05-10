from fastapi import FastAPI
from pydantic import BaseModel
from app.recommender import recommend

app = FastAPI()
@app.get("/")
def root():
    return {
        "message": "SHL Conversational AI Recommender API"
    }
# ---------- REQUEST MODEL ----------

class ChatRequest(BaseModel):
    message: str

# ---------- HEALTH ENDPOINT ----------

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "message": "SHL AI Recommender API Running"
    }

# ---------- CHAT ENDPOINT ----------

@app.post("/chat")
def chat(request: ChatRequest):

    query = request.message.lower()

    # ---------- CLARIFYING QUESTIONS ----------

    if (
        "developer" in query
        and "python" not in query
        and "java" not in query
        and "frontend" not in query
    ):

        return {
            "response": (
                "Could you clarify whether you are hiring "
                "for backend, frontend, full stack, or "
                "AI/ML development roles?"
            )
        }

    # ---------- COMPARISON ----------

    if "compare" in query:

        return {
            "response": (
                "Technical Skills Assessment focuses on "
                "practical engineering and coding abilities, "
                "while Automata assessments emphasize "
                "compiler-based coding and debugging tasks."
            )
        }

    # ---------- RECOMMEND ----------

    results = recommend(query)

    return {
        "query": query,
        "recommendations": results
    }

    # ---------- GET RECOMMENDATIONS ----------

    results = recommend(query)

    recommendations = []

    for item in results:

        recommendations.append({
            "assessment_name": item["name"],
            "match_score": item["score"],
            "description": item["description"],
            "url": item["url"],
            "reason": (
                "Recommended because the assessment aligns "
                "with the technical skills and semantic context "
                "identified in the job description."
            )
        })

    return {
        "query": query,
        "recommendations": recommendations
    }