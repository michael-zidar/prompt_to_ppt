# Prompt to PPT

A modular Flask application that generates PowerPoint decks from a text prompt and an optional sample presentation. Style rules are extracted from the sample and applied to the generated deck. The web interface is styled with Tailwind CSS via CDN for a modern look.

## Quickstart

```bash
pip install -r requirements.txt
cp .env.example .env  # populate environment variables locally
python -m flask --app app:create_app run
```

## Environment Variables

The application expects the following variables (usually provided via a `.env` file):

- `OPENAI_API_KEY` – API key for the OpenAI API
- `OPENAI_MODEL` – model name (default `gpt-4o-mini`)
- `MAX_TOKENS` – maximum tokens for generation
- `SECRET_KEY` – Flask session secret

## Testing

Run the test suite with:

```bash
pytest
```
