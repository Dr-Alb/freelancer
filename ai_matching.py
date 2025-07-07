def get_job_matches(user_skills, jobs):
    user_skills = [s.strip().lower() for s in user_skills.split(",")]
    matched = []

    for job in jobs:
        job_skills = [s.strip().lower() for s in job["skills"].split(",")]
        if any(skill in job_skills for skill in user_skills):
            matched.append(job)

    return matched