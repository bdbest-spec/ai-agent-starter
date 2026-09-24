# AI Agent Starter

This repository contains a minimal AI agent starter project built with Python, FastAPI, and OpenAI function calling.

## Features
- FastAPI backend
- `/health` endpoint
- `/chat` endpoint
- OpenAI function calling demo
- Simple tool-based agent loop

## Local setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Then add your OpenAI API key to `.env`:

```bash
OPENAI_API_KEY=your_key_here
MODEL=gpt-4o-mini
```

## Run the app

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Example request

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Tell me a fact about Python and also give me the current time in Tokyo."}'
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

## Notes

This is intentionally a lightweight starter to help you build a more advanced agent with:
- memory
- database integration
- web search tools
- authentication
- background jobs
- deployment to cloud platforms
