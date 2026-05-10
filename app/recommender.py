import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# ---------- LOAD MODEL ----------

model = SentenceTransformer(
    'all-MiniLM-L6-v2'
)

# ---------- LOAD INDEX ----------

index = faiss.read_index(
    "data/assessment_index.faiss"
)

# ---------- LOAD DATA ----------

with open(
    "data/assessments.json",
    "r",
    encoding="utf-8"
) as f:

    assessments = json.load(f)

# ---------- RECOMMENDER ----------

def recommend(query, top_k=5):

    query_embedding = model.encode([query])

    distances, indices = index.search(
        np.array(query_embedding),
        top_k
    )

    results = []

    used_names = set()

    for i, idx in enumerate(indices[0]):

        item = assessments[idx]

        # ---------- REMOVE DUPLICATES ----------

        if item["name"] in used_names:
            continue

        used_names.add(item["name"])

        # ---------- BETTER MATCH SCORE ----------

        similarity = 1 / (1 + distances[0][i])

        score = round(similarity * 100, 2)

        # ---------- FILTER WEAK MATCHES ----------

        if score < 35:
            continue

        # ---------- DYNAMIC REASON ----------

        reason = (
            f"Recommended because this assessment evaluates "
            f"skills related to: {item['description'][:120]}"
        )

        results.append({

            "name": item["name"],

            "url": item["url"],

            "description": item["description"],

            "score": score,

            "reason": reason
        })

    return results