# Web app

The FastAPI application now serves a browser interface at `/` and static assets from `/static`. Start the project with:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Open <http://localhost:8000> in a browser. The website sends chat messages to the existing `/chat` endpoint and does not expose the OpenAI API key to the browser.
