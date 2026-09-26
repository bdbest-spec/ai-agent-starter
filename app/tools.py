"""OpenAI function definitions used by the chat endpoint."""

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_time_in_timezone",
            "description": "Return a sample current time for a city in a demo app.",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "City name, such as Tokyo, London, New York, Dubai, or Dhaka.",
                    }
                },
                "required": ["city"],
                "additionalProperties": False,
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_fact",
            "description": "Return a short fact about a given topic.",
            "parameters": {
                "type": "object",
                "properties": {
                    "topic": {
                        "type": "string",
                        "description": "Topic to discuss, such as Python, AI, ethics, or Quran.",
                    }
                },
                "required": ["topic"],
                "additionalProperties": False,
            },
        },
    },
]
