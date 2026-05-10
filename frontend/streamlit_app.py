import requests
import streamlit as st
import streamlit.components.v1 as components
from bs4 import BeautifulSoup

# ---------- PAGE CONFIG ----------

st.set_page_config(
    page_title="SHL AI Recommender",
    page_icon="🧠",
    layout="wide"
)

# ---------- CUSTOM CSS ----------

st.markdown("""
<style>

.stApp {
    background: linear-gradient(to right, #0f172a, #1e293b);
    color: white;
}

.main-title {
    font-size: 52px;
    font-weight: 700;
    text-align: center;
    margin-top: 20px;
    color: white;
}

.sub-title {
    text-align: center;
    font-size: 20px;
    color: #cbd5e1;
    margin-bottom: 40px;
}

.stButton>button {
    width: 100%;
    background: linear-gradient(to right, #2563eb, #7c3aed);
    color: white;
    border-radius: 15px;
    padding: 14px;
    font-size: 18px;
    border: none;
    font-weight: bold;
}

.stButton>button:hover {
    background: linear-gradient(to right, #1d4ed8, #6d28d9);
    color: white;
}

.skill-pill {
    display: inline-block;
    background: #2563eb;
    color: white;
    padding: 6px 14px;
    border-radius: 20px;
    margin-right: 10px;
    margin-top: 8px;
    font-size: 14px;
}

.footer {
    text-align: center;
    color: #94a3b8;
    margin-top: 50px;
    margin-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------

st.markdown(
    '<div class="main-title">🧠 SHL AI Assessment Recommender</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">Semantic AI-Powered Hiring Intelligence Platform</div>',
    unsafe_allow_html=True
)

# ---------- SIDEBAR ----------

with st.sidebar:

    st.header("⚡ About")

    st.write("""
This AI platform uses:

- Semantic embeddings
- FAISS vector similarity search
- NLP-powered recommendation engine
- Intelligent assessment matching
    """)

    st.write("---")

    st.subheader("🛠 Tech Stack")

    st.write("""
- FastAPI
- Streamlit
- SentenceTransformers
- FAISS
- Python
    """)

    st.write("---")

    st.success("AI Recommendation System Active")

# ---------- INPUT SECTION ----------

query = st.text_area(
    "📄 Paste Job Description",
    height=220,
    placeholder="Example: Looking for a backend engineer with Java, SQL, APIs, debugging, and cloud deployment skills..."
)

jd_url = st.text_input(
    "🔗 Optional: Paste Job Description URL",
    placeholder="https://company.com/job-description"
)

# ---------- SKILL DETECTION ----------

skills = []

keywords = [
    "Python", "Java", "SQL", "React",
    "AWS", "Machine Learning",
    "APIs", "Debugging", "Cloud",
    "Data Science", "DevOps",
    "Spring Boot", "Docker",
    "Kubernetes", "AI", "NLP"
]

combined_text = query.lower()

for skill in keywords:
    if skill.lower() in combined_text:
        skills.append(skill)

if skills:

    st.markdown("### 🔍 Detected Skills")

    skill_html = ""

    for skill in skills:
        skill_html += f"""
        <span class="skill-pill">{skill}</span>
        """

    st.markdown(skill_html, unsafe_allow_html=True)

# ---------- BUTTON ----------

if st.button("🚀 Generate Recommendations"):

    final_query = query

    # ---------- URL EXTRACTION ----------

    if jd_url.strip() != "":

        try:

            response = requests.get(
                jd_url,
                headers={"User-Agent": "Mozilla/5.0"}
            )

            soup = BeautifulSoup(
                response.text,
                "html.parser"
            )

            extracted_text = soup.get_text(
                separator=" ",
                strip=True
            )

            final_query += " " + extracted_text[:3000]

            st.success(
                "✅ Job description extracted successfully from URL."
            )

        except:

            st.error(
                "❌ Could not extract content from URL."
            )

    # ---------- EMPTY CHECK ----------

    if final_query.strip() == "":

        st.warning(
            "Please enter a job description or URL."
        )

    else:

        with st.spinner(
            "Analyzing job description using semantic AI..."
        ):

            api_url = "http://127.0.0.1:8000/chat"

            payload = {
                "message": final_query
            }

            response = requests.post(
                api_url,
                json=payload
            )

            data = response.json()

            # ---------- HANDLE CLARIFICATION ----------

            if "response" in data:

                st.warning(data["response"])

                results = []

            else:

                results = data["recommendations"]

                st.success(
                    "✅ Top matching assessments generated."
                )

        # ---------- RESULT CARDS ----------

        for item in results:

            card_html = f"""
            <html>
            <head>

            <style>

            body {{
                margin: 0;
                padding: 0;
                background: transparent;
                font-family: Arial, sans-serif;
            }}

            .card {{
                background: rgba(255,255,255,0.08);
                backdrop-filter: blur(12px);
                border-radius: 20px;
                padding: 25px;
                margin-top: 20px;
                box-shadow: 0px 8px 32px rgba(0,0,0,0.3);
                border: 1px solid rgba(255,255,255,0.1);
                color: white;
            }}

            .title {{
                font-size: 28px;
                font-weight: bold;
                margin-bottom: 10px;
            }}

            .score {{
                font-size: 22px;
                font-weight: bold;
                color: #22c55e;
                margin-bottom: 20px;
            }}

            .desc {{
                margin-top: 15px;
                line-height: 1.6;
                color: #e2e8f0;
            }}

            .tag {{
                display: inline-block;
                background: #2563eb;
                color: white;
                padding: 6px 12px;
                border-radius: 20px;
                margin-right: 8px;
                margin-top: 15px;
                font-size: 13px;
            }}

            .btn {{
                display: inline-block;
                margin-top: 20px;
                padding: 10px 18px;
                background: linear-gradient(to right, #2563eb, #7c3aed);
                color: white;
                text-decoration: none;
                border-radius: 12px;
                font-weight: bold;
            }}

            </style>

            </head>

            <body>

            <div class="card">

                <div class="title">
                 {item['name']}
                </div>

                <div class="score">
                Match Score: {item['score']}%
                </div>

                <div class="desc">
                    {item['description']}
                </div>

                <div class="tag">Semantic Search</div>
                <div class="tag">FAISS</div>
                <div class="tag">AI Matching</div>

                <div class="desc">
                    {item['reason']}
                </div>

                <a class="btn" href="{item['url']}" target="_blank">
                    🔍 Explore on SHL
                </a>

            </div>

            </body>
            </html>
            """

            components.html(card_html, height=400)

# ---------- FOOTER ----------

st.markdown("""
<div class="footer">

Built with ❤️ using FastAPI, Streamlit, SentenceTransformers, and FAISS

</div>
""", unsafe_allow_html=True)