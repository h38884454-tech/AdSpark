from adspark.generator import generate_ad_variants
from adspark.models import AdRequest


def test_generate_ad_variants_returns_three_variants():
    request = AdRequest(
        product_name="NovaFit",
        audience="busy professionals",
        tone="bold",
        platform="instagram",
        goal="sales",
        keywords=["fitness", "smart", "daily"],
        features=["AI coaching", "7-day progress tracking", "Minimal setup"],
        cta="Start your plan",
    )

    response = generate_ad_variants(request)

    assert response.product_name == "NovaFit"
    assert response.platform == "instagram"
    assert response.source in {"local", "openai"}
    assert len(response.variants) >= 3
    assert all(variant.headline for variant in response.variants)
    assert all(variant.body for variant in response.variants)
    assert all(variant.cta for variant in response.variants)
