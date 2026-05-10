import json
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

with open("data/assessments.json", "r", encoding="utf-8") as f:
    assessments = json.load(f)

texts = [
    item["name"] + " " + item["description"]
    for item in assessments
]

embeddings = model.encode(texts)

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

faiss.write_index(index, "data/assessment_index.faiss")

print("FAISS index saved.")