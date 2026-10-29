# AdSpark

AdSpark is an AI-powered ad generation platform that helps teams turn a product, audience, and brand tone into polished marketing copy for multiple channels.

## Features
- Generate ad headlines and body copy for different platforms
- Customize by audience, tone, campaign goal, and CTA
- Support optional OpenAI-powered generation when `OPENAI_API_KEY` is set
- Expose a clean REST API and a Python package for reuse

## Quick start

1. Create and activate a virtual environment
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Optional: configure AI access
   ```bash
   cp .env.example .env
   ```
   Then edit `.env` and set `OPENAI_API_KEY` if you want model-based generation.

4. Run the API server
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

5. Call the API
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

## Project layout
```text
adspark/
  __init__.py
  generator.py
  models.py
main.py
tests/
  test_generator.py
requirements.txt
.env.example
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
- If `OPENAI_API_KEY` is absent, the project still works using a built-in generator.
- The app is intentionally lightweight and easy to extend for a full SaaS frontend.
