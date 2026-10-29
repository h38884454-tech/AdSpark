from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class AdRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    product_name: str = Field(..., min_length=1)
    audience: str = Field(..., min_length=1)
    tone: Literal["bold", "playful", "luxury", "trustworthy", "urgent"] = "bold"
    platform: Literal["instagram", "facebook", "google", "linkedin", "youtube", "tiktok", "website"] = "instagram"
    goal: Literal["awareness", "traffic", "sales", "engagement"] = "sales"
    keywords: list[str] = Field(default_factory=list)
    features: list[str] = Field(default_factory=list)
    cta: str = "Shop now"


class AdVariant(BaseModel):
    headline: str
    body: str
    cta: str


class AdResponse(BaseModel):
    product_name: str
    audience: str
    platform: str
    goal: str
    tone: str
    source: str
    variants: list[AdVariant]
