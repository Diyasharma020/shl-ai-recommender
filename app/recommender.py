import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ---------- LOAD DATA ----------

with open(
    "data/assessments.json",
    "r",
    encoding="utf-8"
) as f:

    assessments = json.load(f)

# ---------- PREPARE TEXT ----------

documents = [
    item["description"]
    for item in assessments
]

# ---------- TF-IDF ----------

vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(documents)

# ---------- RECOMMENDER ----------

def recommend(query, top_k=5):

    query_vector = vectorizer.transform([query])

    similarities = cosine_similarity(
        query_vector,
        tfidf_matrix
    )[0]

    top_indices = similarities.argsort()[::-1][:top_k]

    results = []

    for idx in top_indices:

        item = assessments[idx]

        score = round(similarities[idx] * 100, 2)

        results.append({

            "name": item["name"],

            "url": item["url"],

            "description": item["description"],

            "score": score,

            "reason": (
                "Recommended because the assessment aligns "
                "with the required technical skills and "
                "semantic context in the job description."
            )
        })

    return results