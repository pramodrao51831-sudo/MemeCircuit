# ⚡ MemeCircuit — Autonomous Meme Trend Agent

MemeCircuit is an AI-powered culture engine built with **Streamlit**, **LangGraph**, and **Reddit (PRAW)** that dynamically detects viral meme trends and manages automated publishing.

## 🛠️ Tech Stack
- **UI Framework:** Streamlit
- **Agent Orchestration:** LangGraph (with `SqliteSaver` checkpointer state)
- **Data & Distribution Pipeline:** Reddit API (PRAW)
- **Language:** Python 3.10+

## 🚀 Quickstart
```bash
pip install -r requirements.txt
streamlit run app.py