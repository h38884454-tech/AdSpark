* {
  box-sizing: border-box;
}

body {
  margin: 0;
  font-family: Inter, Arial, sans-serif;
  background: linear-gradient(135deg, #f5f7ff 0%, #eef7f4 100%);
  color: #1b1f2a;
}

.container {
  max-width: 1100px;
  margin: 0 auto;
  padding: 48px 20px 72px;
}

.hero {
  text-align: center;
  margin-bottom: 24px;
}

.eyebrow {
  display: inline-block;
  margin-bottom: 8px;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  font-size: 0.75rem;
  color: #4a5cf7;
  font-weight: 700;
}

h1 {
  margin: 0;
  font-size: clamp(2.4rem, 7vw, 4rem);
}

.subtitle {
  color: #445066;
  font-size: 1.1rem;
}

.panel {
  background: rgba(255,255,255,0.75);
  border: 1px solid rgba(14, 25, 48, 0.08);
  border-radius: 16px;
  padding: 24px;
  box-shadow: 0 8px 24px rgba(31, 41, 55, 0.08);
}

.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 18px;
}

label {
  display: block;
  font-weight: 600;
  margin-top: 18px;
}

input,
select,
button {
  width: 100%;
  margin-top: 8px;
  padding: 12px 14px;
  border-radius: 10px;
  border: 1px solid #dfe7f1;
  font-size: 1rem;
}

button {
  background: linear-gradient(135deg, #4a5cf7, #3bb4a5);
  color: white;
  border: 0;
  cursor: pointer;
  font-weight: 700;
  transition: transform 0.15s ease;
}

button:hover {
  transform: translateY(-1px);
}

.results {
  margin-top: 28px;
}

.result-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 18px;
}

.card {
  background: rgba(255,255,255,0.86);
  border: 1px solid rgba(17, 22, 25, 0.07);
  border-radius: 14px;
  padding: 18px;
  box-shadow: 0 8px 22px rgba(15, 23, 42, 0.06);
}

.card h3 {
  margin-top: 0;
  margin-bottom: 12px;
}

.card p {
  color: #374151;
  line-height: 1.5;
}

.badge {
  display: inline-block;
  padding: 6px 10px;
  margin-bottom: 10px;
  border-radius: 999px;
  background: #eef2ff;
  color: #3b5ff5;
  font-size: 0.78rem;
  font-weight: 700;
}

.hidden {
  display: none;
}
