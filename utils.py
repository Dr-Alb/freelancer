from supabase_config import supabase

def load_jobs():
    response = supabase.table("jobs").select("*").execute()
    return response.data if response.data else []

def save_job_post(client, title, description, skills):
    supabase.table("jobs").insert({
        "client": client,
        "title": title,
        "description": description,
        "skills": skills
    }).execute()