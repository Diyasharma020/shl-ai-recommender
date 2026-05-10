import requests
from bs4 import BeautifulSoup
import json

URL = "https://www.shl.com/solutions/products/product-catalog/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(URL, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

assessments = []

for tag in soup.find_all(["h2", "h3", "h4", "a"]):

    text = tag.get_text(strip=True)

    href = tag.get("href")

    if (
        text
        and len(text) > 10
        and href
        and "/products/" in href
    ):

        full_url = (
            "https://www.shl.com" + href
            if href.startswith("/")
            else href
        )

        assessments.append({
            "name": text,
            "url": full_url,
            "description": text
        })

# Remove duplicates
unique = []

seen = set()

for item in assessments:

    if item["name"] not in seen:

        seen.add(item["name"])

        unique.append(item)

with open("data/assessments.json", "w", encoding="utf-8") as f:

    json.dump(unique, f, indent=4)

print(f"Saved {len(unique)} assessments.")