const form = document.getElementById('ad-form');
const resultsContainer = document.getElementById('results');

function parseList(value) {
  return value
    .split(',')
    .map((item) => item.trim())
    .filter(Boolean);
}

function renderResults(data) {
  resultsContainer.classList.remove('hidden');
  const variants = data.variants || [];

  resultsContainer.innerHTML = `
    <h2>Generated variants</h2>
    <div class="result-grid">
      ${variants
        .map(
          (variant, index) => `
            <article class="card">
              <span class="badge">Variant ${index + 1}</span>
              <h3>${variant.headline}</h3>
              <p>${variant.body}</p>
              <p><strong>CTA:</strong> ${variant.cta}</p>
            </article>
          `,
        )
        .join('')}
    </div>
  `;
}

form.addEventListener('submit', async (event) => {
  event.preventDefault();

  const formData = new FormData(form);
  const payload = {
    product_name: formData.get('product_name'),
    audience: formData.get('audience'),
    tone: formData.get('tone'),
    platform: formData.get('platform'),
    goal: formData.get('goal'),
    keywords: parseList(formData.get('keywords') || ''),
    features: parseList(formData.get('features') || ''),
    cta: formData.get('cta') || 'Shop now',
  };

  try {
    const response = await fetch('/api/ads/generate', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(payload),
    });

    if (!response.ok) {
      throw new Error('Request failed');
    }

    const data = await response.json();
    renderResults(data);
  } catch (error) {
    resultsContainer.classList.remove('hidden');
    resultsContainer.innerHTML = `
      <h2>Something went wrong</h2>
      <p>${error.message}</p>
    `;
  }
});
