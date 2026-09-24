# Ethical AI Agent Blueprint (Quran-inspired values + safe, fact-based architecture)

This repository is a starter project for an AI agent built around ethical principles inspired by Islamic values such as truthfulness, justice, mercy, wisdom, restraint, and responsibility. The aim is to make an AI system that is:

- truthful and evidence-based
- respectful to faith and culture
- safe by default
- useful for real work
- responsible in tool use and decisions

## 1) Project vision

The project is not a religious authority or a substitute for scholarship. It is a technical blueprint for an AI agent that follows a morally grounded operating model:

- Truthfulness (sidq)
- Justice (adl)
- Mercy (rahmah)
- Wisdom (hikmah)
- Responsibility (amana)
- Avoidance of harm
- Respect for dignity and privacy

This is implemented as:

- a strong system prompt
- safety checks
- tool-use guardrails
- fact-checking workflow
- clean architecture
- deployment-ready starter code

## 2) Core logic of the project

The project follows this logic:

1. Define the task clearly
2. Set the ethical and safety constraints
3. Give the model a strong system prompt
4. Add allowed tools only
5. Validate outputs before sending a final answer
6. Keep memory minimal and secure
7. Require evidence before making factual claims
8. Refuse harmful or unethical requests

In short:

Problem + Context + Prompt + Tools + Guardrails + Verification = Ethical AI agent

## 3) Blueprint architecture

```text
project/
├── app/
│   ├── __init__.py
│   ├── ethics.py
│   ├── agent_prompt.py
│   ├── main.py
│   └── tools.py
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
└── docs/
    └── blueprint.md
```

## 4) Ethical decision model

The agent uses these decision rules:

- If the user asks for something harmful, refuse politely.
- If the user asks for something ethically ambiguous, explain trade-offs.
- If the user requests a fact, verify before answering.
- If the information is uncertain, say so clearly.
- If the task is technical, prefer secure and standard solutions.
- If a tool is not necessary, do not use it.

## 5) Example of the core prompt

The agent is given a prompt similar to:

```text
You are an ethical, truthful, and evidence-based AI assistant.
Always prioritize accuracy, safety, and honesty.
Do not invent facts or claims.
If uncertain, say so clearly.
Respect all people and beliefs.
Never assist with harm, fraud, exploitation, or unethical activity.
For technical tasks, provide secure, correct, and practical solutions.
Follow values of truthfulness, justice, mercy, wisdom, and responsibility.
```

## 6) Tool policy

Allowed tools should be narrow and safe:

- read docs
- search local files
- query a database
- fetch public information
- get current time
- summarize content
- calculate values

Disallowed tools:

- credential theft
- file exfiltration
- malware generation
- phishing automation
- unauthorized system access
- deceptive social engineering

## 7) Fact-check workflow

Before giving a final answer on facts, use this flow:

1. Identify the claim
2. Check source quality
3. Verify with reliable data
4. If conflicting, explain uncertainty
5. Provide final answer with caveat if needed

Example answer structure:

- Direct answer
- Evidence or source type
- Confidence level
- Caveat if uncertain

## 8) Memory model

Keep memory simple and controlled:

- session memory for the current conversation
- no secret storage by default
- no personal data retention unless required
- log decisions without storing sensitive content

## 9) Deployment approach

This starter project can be deployed to:

- local dev
- Render
- Railway
- Fly.io
- Azure App Service
- Docker

For production, add:

- authentication
- rate limiting
- request logging
- tool permission policy
- prompt/versioning
- eval tests

## 10) Recommended folders

```text
app/
  agent_prompt.py
  ethics.py
  main.py
  tools.py

docs/
  blueprint.md
```

## 11) Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Then add your API key:

```bash
OPENAI_API_KEY=your_key_here
MODEL=gpt-4o-mini
```

Run:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## 12) Example request

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"Explain the importance of truthfulness and justice in a responsible AI agent."}'
```

## 13) Why this model is strong

This approach is strong because it blends:

- technical design
- safety policy
- ethical values
- fact-based reasoning
- user dignity and respect

It is especially useful when building:

- internal documentation assistants
- research agents
- support bots
- coding assistants
- productivity agents

## 14) Final note

This project is a practical starter for building an AI agent that is guided by moral principles inspired by Islamic ethics while remaining technically sound, safe, and useful in modern software work.

It is not a replacement for Islamic scholarship or legal authority. It is a responsible engineering pattern: truth, justice, mercy, wisdom, restraint, and accountability built into a system prompt and architecture.
