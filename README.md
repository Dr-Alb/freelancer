# Freelancers Bot (Streamlit + Supabase + GPT)

## Features
- Supabase user authentication
- Post and match freelance jobs
- Dashboard for managing job posts
- AI Chat Assistant powered by OpenAI GPT

## Setup Instructions

1. Replace `.streamlit/secrets.toml` values with your real Supabase and OpenAI credentials.
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the app:
```bash
streamlit run app.py
```

## Deploying to Streamlit Cloud

1. Push this project to GitHub
2. Deploy at https://streamlit.io/cloud
3. Paste your `secrets.toml` values into the app's Secrets Settings