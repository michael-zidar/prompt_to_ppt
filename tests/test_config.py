import os
from app.config import get_settings


def test_get_settings(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "x")
    settings = get_settings()
    assert settings.openai_api_key == "x"
