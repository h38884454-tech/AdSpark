# AdSpark

AdSpark is a lightweight AI-powered ad generation platform for marketers, founders, and agencies who want fast campaign copy without starting from scratch.

The project includes:
- a FastAPI backend for generating ad variants
- a fully working local fallback generator
- optional OpenAI-powered generation when `OPENAI_API_KEY` is configured
- a simple browser UI for testing ideas without a separate frontend app

## Features
- Generate ad copy for multiple platforms and campaign goals
- Customize tone, audience, CTA, keywords, and product features
- Return 3 polished ad variants per request
- Work locally without external API access
- Easily extend to saved campaigns, user auth, and analytics

## Quick start

1. Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Configure environment variables:

```bash
cp .env.example .env
```

Edit `.env` if needed and set `OPENAI_API_KEY` for model-based generation.

4. Run the app:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

5. Open the browser UI:

```text
http://localhost:8000/
```

6. Or call the API directly:

```bash
curl -X POST "http://localhost:8000/api/ads/generate" \
  -H "Content-Type: application/json" \
  -d '{
    "product_name": "NovaFit",
    "audience": "busy professionals",
    "tone": "bold",
    "platform": "instagram",
    "goal": "sales",
    "keywords": ["fitness", "smart", "daily"],
    "features": ["AI coaching", "7-day progress tracking", "Minimal setup"],
    "cta": "Start your plan"
  }'
```

## Project structure

```text
AdSpark/
├── adspark/
│   ├── __init__.py
│   ├── generator.py
│   ├── models.py
├── static/
│   ├── app.js
│   └── styles.css
├── templates/
│   └── index.html
├── .env.example
├── .gitignore
├── Dockerfile
├── README.md
├── main.py
├── requirements.txt
├── tests/
│   ├── __init__.py
│   └── test_generator.py
└── .venv/
```

## Example response

```json
{
  "product_name": "NovaFit",
  "audience": "busy professionals",
  "platform": "instagram",
  "goal": "sales",
  "tone": "bold",
  "source": "local",
  "variants": [
    {
      "headline": "NovaFit helps busy professionals build stronger routines.",
      "body": "Stay on track with AI coaching, 7-day progress tracking, and minimal setup.",
      "cta": "Start your plan"
    }
  ]
}
```

## Notes
- If `OPENAI_API_KEY` is missing, the app still works using an internal generator.
- The app is intentionally lightweight and designed to be extended for auth, billing, and persisted campaigns.
