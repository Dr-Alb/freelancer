import json
from pathlib import Path

DATA_FILE = Path("jobs.json")

def load_jobs():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_job_post(client, title, description, skills):
    jobs = load_jobs()
    jobs.append({
        "client": client,
        "title": title,
        "description": description,
        "skills": skills
    })
    with open(DATA_FILE, "w") as f:
        json.dump(jobs, f)