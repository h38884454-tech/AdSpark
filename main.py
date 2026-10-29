from __future__ import annotations

import json
import os
from typing import Any

from .models import AdRequest, AdResponse, AdVariant


def _safe_join(values: list[str], fallback: str) -> str:
    return ", ".join(v for v in values if v).strip() or fallback


def _build_local_variants(request: AdRequest) -> list[AdVariant]:
    primary_feature = request.features[0] if request.features else "premium value"
    secondary_feature = request.features[1] if len(request.features) > 1 else "simple setup"
    keyword_text = _safe_join(request.keywords, "smart growth")

    headline_templates = {
        "bold": [
            f"{request.product_name} is built for {request.audience}.",
            f"Turn {keyword_text} into momentum with {request.product_name}.",
            f"The smarter way to grow for {request.audience}.",
        ],
        "playful": [
            f"Meet {request.product_name}: the fun way to win more attention.",
            f"{request.product_name} makes {request.audience} feel unstoppable.",
            f"Small steps. Big wins. {request.product_name}.",
        ],
        "luxury": [
            f"Elevate your {request.audience} experience with {request.product_name}.",
            f"Luxury performance for modern brands.",
            f"{request.product_name} brings effortless polish to every campaign.",
        ],
        "trustworthy": [
            f"{request.product_name} helps {request.audience} do more with confidence.",
            f"A dependable way to reach customers and grow faster.",
            f"Built to support {request.audience} with clarity and consistency.",
        ],
        "urgent": [
            f"{request.product_name} helps {request.audience} move faster today.",
            f"Act now: {request.product_name} is built to convert attention into action.",
            f"Your next win starts with {request.product_name}.",
        ],
    }

    body_templates = {
        "bold": [
            f"{primary_feature} meets high-converting messaging for {request.audience}.",
            f"Designed to help brands grow through better creative, faster decisions, and simpler execution.",
            f"Built for {request.goal} campaigns and optimized for {request.platform} audiences.",
        ],
        "playful": [
            f"{primary_feature} with a lighter, faster path from idea to impact.",
            f"Perfect for brands that want more personality and better performance.",
            f"From inspiration to conversion, {request.product_name} keeps the momentum going.",
        ],
        "luxury": [
            f"A premium experience for {request.audience}, backed by {secondary_feature} and polished execution.",
            f"Thoughtful creative, refined positioning, and premium results for modern campaigns.",
            f"{request.product_name} blends elegance, clarity, and performance.",
        ],
        "trustworthy": [
            f"Reliable support for {request.audience} who value quality, speed, and clarity.",
            f"{request.product_name} helps teams turn features into clear value for customers.",
            f"Create a consistent message that feels helpful, intentional, and effective.",
        ],
        "urgent": [
            f"Don’t wait to launch a better campaign. {primary_feature} helps you move faster.",
            f"Now is the time to turn attention into action with {request.product_name}.",
            f"Get a stronger message and better conversion results without extra complexity.",
        ],
    }

    variants: list[AdVariant] = []
    headlines = headline_templates.get(request.tone, headline_templates["bold"])
    bodies = body_templates.get(request.tone, body_templates["bold"])

    for idx in range(3):
        headline = headlines[idx % len(headlines)]
        body = bodies[idx % len(bodies)]
        variants.append(
            AdVariant(
                headline=headline,
                body=body,
                cta=request.cta or "Shop now",
            )
        )

    return variants


def _build_openai_variants(request: AdRequest) -> list[AdVariant] | None:
    try:
        from openai import OpenAI
    except ModuleNotFoundError:
        return None

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return None

    try:
        client = OpenAI(api_key=api_key)
        prompt = f"""
        Generate 3 ad variants for a product called {request.product_name}.
        Audience: {request.audience}
        Tone: {request.tone}
        Platform: {request.platform}
        Goal: {request.goal}
        Features: {', '.join(request.features) if request.features else 'high quality and easy adoption'}
        Keywords: {', '.join(request.keywords) if request.keywords else 'growth and conversion'}
        CTA: {request.cta}

        Return valid JSON in this structure:
        [{"headline": "...", "body": "...", "cta": "..."}, ...]
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an expert ad copywriter. Respond with only valid JSON array."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.7,
        )
        raw_text = response.choices[0].message.content or "[]"
        data = json.loads(raw_text)
        items = [AdVariant(**item) for item in data[:3]]
        return items
    except Exception:
        return None


def generate_ad_variants(request: AdRequest) -> AdResponse:
    variants = _build_openai_variants(request)
    if variants is None:
        variants = _build_local_variants(request)
        source = "local"
    else:
        source = "openai"

    return AdResponse(
        product_name=request.product_name,
        audience=request.audience,
        platform=request.platform,
        goal=request.goal,
        tone=request.tone,
        source=source,
        variants=variants,
    )
