# 🤖 Freelancers Bot

Freelancers Bot is an intelligent platform built with **Streamlit**, **Supabase**, and **OpenAI GPT** to connect **freelancers** and **clients**. It enables users to post freelance jobs, match those jobs to skilled professionals, and even get help from an AI assistant to write proposals or answer questions.

---

## 🔥 Key Features

- 🔐 **Authentication** with Supabase (Sign Up & Login)
- 📝 **Job Posting** system for clients
- 🎯 **AI-based Skill Matching** for freelancers
- 📊 **Dashboard** to view all job listings
- 💬 **GPT-powered AI Assistant** for tips and proposal writing
- ☁️ **Deployable to Streamlit Cloud**

---

## 🧱 Tech Stack

| Layer       | Technology             |
|-------------|------------------------|
| Frontend    | [Streamlit](https://streamlit.io/)       |
| Backend     | [Supabase](https://supabase.io/)         |
| Database    | PostgreSQL (via Supabase)  |
| Authentication | Supabase Auth       |
| AI Assistant | [OpenAI GPT](https://platform.openai.com/) |
| Hosting     | [Streamlit Cloud](https://streamlit.io/cloud) |

---

## 📁 Project Structure

freelancers_bot/
├── app.py # Main Streamlit app logic
├── ai_assistant.py # GPT assistant logic
├── ai_matching.py # AI job matching logic
├── supabase_config.py # Supabase client setup
├── utils.py # Job posting/loading functions
├── requirements.txt # Required Python packages
├── README.md # This documentation
├── .gitignore # Git ignore file
└── .streamlit/
└── secrets.toml # 🔐 API keys (never push this to GitHub)

yaml
Copy
Edit

---

## ⚙️ Getting Started (Local Setup)

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/freelancers_bot.git
cd freelancers_bot
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Add Secrets
Create a file at .streamlit/secrets.toml:


bash
Copy
Edit
streamlit run app.py
