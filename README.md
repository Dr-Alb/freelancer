# 🤖 Freelancers Bot

Freelancers Bot is an AI-powered Streamlit web app that connects freelancers with clients using GPT and Supabase.

## Features

- 🔐 Supabase authentication
- 📝 Job posting
- 🧠 GPT-based matching
- 📋 Job dashboard
- 💬 AI assistant powered by OpenAI

## Setup

1. Create `.streamlit/secrets.toml` with your credentials:

```toml
SUPABASE_URL = "https://your-project.supabase.co"
SUPABASE_KEY = "your-anon-key"
OPENAI_API_KEY = "sk-your-openai-key"
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
streamlit run app.py
```

4. Deploy on Streamlit Cloud and add secrets in the dashboard.