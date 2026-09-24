import json
import os
from typing import Any

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import OpenAI

load_dotenv()

app = FastAPI(title="AI Agent Starter", version="0.1.0")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class ChatRequest(BaseModel):
    message: str
    model: str | None = None


def get_time_in_timezone(city: str) -> str:
    city_map = {
        "tokyo": "2026-09-24 12:00 JST",
        "london": "2026-09-24 04:00 BST",
        "new york": "2026-09-24 00:00 EDT",
        "dubai": "2026-09-24 07:00 GST",
    }
    return city_map.get(city.lower(), f"I don't have a timezone entry for {city} in this demo tool.")


def get_fact(topic: str) -> str:
    fact_bank = {
        "python": "Python was created by Guido van Rossum and is widely used for automation, web apps, and AI.",
        "ai": "AI systems often use large language models to reason over text and call tools when needed.",
        "space": "The Moon is slowly moving away from Earth by about 3.8 centimeters per year.",
    }
    return fact_bank.get(topic.lower(), f"Here is a quick fact about {topic}: it is a fascinating topic to explore.")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/chat")
def chat(request: ChatRequest) -> dict[str, Any]:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise HTTPException(status_code=500, detail="OPENAI_API_KEY is missing. Add it to your .env file.")

    model = request.model or os.getenv("MODEL", "gpt-4o-mini")

    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_time_in_timezone",
                "description": "Return a sample current time for a city in a demo app.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "city": {"type": "string", "description": "City name such as Tokyo, London, or New York"}
                    },
                    "required": ["city"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "get_fact",
                "description": "Return a short fact about a topic.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "topic": {"type": "string", "description": "Topic to discuss"}
                    },
                    "required": ["topic"],
                },
            },
        },
    ]

    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": request.message}],
        tools=tools,
        tool_choice="auto",
    )

    message = response.choices[0].message
    tool_calls = message.tool_calls

    if not tool_calls:
        return {"response": message.content or "I don't have a direct answer."}

    tool_call = tool_calls[0]
    function_name = tool_call.function.name
    arguments = json.loads(tool_call.function.arguments)

    if function_name == "get_time_in_timezone":
        tool_result = get_time_in_timezone(arguments["city"])
    elif function_name == "get_fact":
        tool_result = get_fact(arguments["topic"])
    else:
        tool_result = f"Unsupported tool: {function_name}"

    second_response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": request.message},
            {"role": "assistant", "content": None, "tool_calls": tool_calls},
            {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "name": function_name,
                "content": tool_result,
            },
        ],
    )

    return {"response": second_response.choices[0].message.content or "Tool executed successfully."}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
