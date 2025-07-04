# 🤖 Freelancers Bot

Freelancers Bot is an AI-powered platform that connects freelancers with clients, streamlines job posting and matching, and provides a smart assistant for guidance. Built using **Streamlit**, **Supabase**, and **OpenAI's GPT**, it is designed to be lightweight, deployable, and monetizable.

---

## 🚀 Features

- 🔐 **Authentication** via Supabase (sign-up and login)
- 📝 **Job Posting** for clients
- 🧠 **AI-Powered Matching** for freelancers based on skills
- 📋 **Dashboard** to manage job listings
- 💬 **GPT Assistant** to help with questions, proposals, and freelancing tips

---

## 🛠️ Tech Stack

| Layer       | Technology             |
|------------|------------------------|
| Frontend   | [Streamlit](https://streamlit.io/)       |
| Backend    | [Supabase](https://supabase.io/)         |
| AI         | [OpenAI GPT](https://platform.openai.com/) |
| Hosting    | [Streamlit Cloud](https://streamlit.io/cloud) |

---

## 📦 Project Structure

```bash
freelancers_bot/
├── app.py                 # Main Streamlit app
├── ai_matching.py         # AI-based job matching logic
├── ai_assistant.py        # OpenAI GPT integration
├── utils.py               # Supabase DB functions
├── supabase_config.py     # Supabase connection handler
├── requirements.txt       # Python dependencies
├── .streamlit/
│   └── secrets.toml       # API keys and DB credentials (not pushed to GitHub)
└── README.md              # Project documentation

⚙️ Setup Instructions
1. Clone the Repo
bash
Copy
Edit
git clone https://github.com/yourusername/freelancers-bot.git
cd freelancers-bot
2. Add Secrets
Create a file called .streamlit/secrets.toml and add your credentials:

toml
Copy
Edit
SUPABASE_URL = "https://your-project.supabase.co"
SUPABASE_KEY = "your-anon-public-key"
OPENAI_API_KEY = "sk-your-openai-key"
3. Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
4. Run the App
bash
Copy
Edit
streamlit run app.py

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