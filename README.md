# AI Agent Starter

A minimal starter project for building an AI agent with Python, FastAPI, and OpenAI function-calling.

## What this includes

- FastAPI app
- `/health` endpoint
- `/chat` endpoint
- Demo tool-calling functions
- Basic environment configuration

## Local setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Then add your OpenAI API key in `.env`:

```bash
OPENAI_API_KEY=your_key_here
MODEL=gpt-4o-mini
```

## Run the app

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Test the chat endpoint

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Tell me a fact about Python and the time in Tokyo."}'
```

## Project structure

```text
app/
  __init__.py
  main.py
requirements.txt
.env.example
.gitignore
README.md
```

## Next ideas

- Add memory with Redis or SQLite
- Add web search tool
- Add user auth
- Add RAG over documents
- Deploy to Railway, Render, Fly.io, or Azure
