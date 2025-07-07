import streamlit as st
from supabase_config import supabase
from ai_matching import get_job_matches
from utils import load_jobs, save_job_post
from ai_assistant import get_ai_reply

st.set_page_config(page_title="Freelancers Bot", layout="wide")
st.title("🤖 Freelancers Bot")

st.sidebar.subheader("Login or Sign Up")
email = st.sidebar.text_input("Email")
password = st.sidebar.text_input("Password", type="password")
auth_action = st.sidebar.radio("Action", ["Login", "Sign Up"])
auth_button = st.sidebar.button("Go")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if auth_button:
    try:
        if auth_action == "Sign Up":
            result = supabase.auth.sign_up({"email": email, "password": password})
        else:
            result = supabase.auth.sign_in_with_password({"email": email, "password": password})

        if result and result.user:
            st.session_state.logged_in = True
            st.session_state.user_email = email
            st.success(f"Welcome, {email}")
    except Exception as e:
        st.error(f"Auth error: {e}")

if st.session_state.logged_in:
    st.sidebar.success(f"Logged in as {st.session_state.user_email}")
    view = st.sidebar.radio("Choose View", ["Client", "Freelancer", "Dashboard", "AI Assistant"])

    if view == "Client":
        st.header("Post a Job")
        title = st.text_input("Job Title")
        description = st.text_area("Description")
        skills = st.text_input("Required Skills")
        if st.button("Post Job"):
            save_job_post(st.session_state.user_email, title, description, skills)
            st.success("Job posted!")

    elif view == "Freelancer":
        st.header("Job Matches")
        skills_input = st.text_input("Your Skills")
        if st.button("Find Jobs"):
            jobs = load_jobs()
            matches = get_job_matches(skills_input, jobs)
            for job in matches:
                st.write(f"**{job['title']}** by {job['client']}")
                st.write(job["description"])
                st.write(f"Skills: {job['skills']}")
                st.markdown("---")

    elif view == "Dashboard":
        st.header("All Job Posts")
        jobs = load_jobs()
        for job in jobs:
            st.write(f"**{job['title']}** (by {job['client']})")
            st.write(job["description"])
            st.write(f"Skills: {job['skills']}")
            st.markdown("---")

    elif view == "AI Assistant":
        st.header("AI Assistant")
        prompt = st.text_input("Ask something...")
        if st.button("Ask GPT"):
            reply = get_ai_reply(prompt)
            st.success(reply)