import json
from typing import Dict, Any, List

from .config import get_settings


def generate_slide_json(prompt: str, style: Dict[str, Any]) -> List[Dict[str, Any]]:
    settings = get_settings()
    # Import OpenAI lazily so tests can run without the package installed
    import openai
    openai.api_key = settings.openai_api_key

    system_prompt = (
        "You are a helpful assistant that creates slide outlines as JSON."
        " Use the provided style rules to guide your response."
    )
    messages = [
        {"role": "system", "content": system_prompt},
        {
            "role": "user",
            "content": json.dumps({"prompt": prompt, "style": style})[:1000],
        },
    ]

    response = openai.ChatCompletion.create(
        model=settings.openai_model,
        messages=messages,
        max_tokens=settings.max_tokens,
        response_format={"type": "json_object"},
    )

    content = response.choices[0].message["content"]
    data = json.loads(content)
    return data.get("slides", [])
