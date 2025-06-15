# ReconAI Core API

> Core Reflexive AI engine powering trust-based decision making for agents.

## 🚀 Overview

The `reconai-core-api` provides the core backend services and logic for Recon.AI, including:

- Reflex Scoring Engine
- GhostLog Signal History
- TrustStack Evaluation Pipeline
- API endpoints for integration with UI and SDK

## 🧠 Tech Stack

- Python 3.10+
- FastAPI
- Pydantic
- Uvicorn
- SQLite/Postgres (optional)
- Redis (optional)

## 📦 Installation

```bash
git clone https://github.com/Trustbyrecon/reconai-core-api.git
cd reconai-core-api
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
pytest tests/
reconai-core-api/
│
├── app/
│   ├── main.py         # FastAPI app entrypoint
│   ├── models.py       # Pydantic data models
│   ├── scoring.py      # Reflex logic
│   ├── ghostlog.py     # Signal logging
│   └── config.py       # Env vars & secrets
│
├── tests/
├── requirements.txt
└── README.md

---

Let me know if you'd like to customize it for internal vs external contributors or want this scaffolded directly into your repo with a commit.
