from supabase_config import supabase

def load_jobs():
    try:
        response = supabase.table("jobs").select("*").execute()
        return response.data if response.data else []
    except Exception as e:
        return []

def save_job_post(client, title, description, skills):
    try:
        supabase.table("jobs").insert({
            "client": client,
            "title": title,
            "description": description,
            "skills": skills
        }).execute()
    except Exception as e:
        print(f"Failed to save job post: {e}")