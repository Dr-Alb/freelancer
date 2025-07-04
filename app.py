import streamlit as st
from supabase_config import supabase
from ai_matching import get_job_matches
from utils import load_jobs, save_job_post

st.set_page_config(page_title="Freelancers Bot", layout="centered")
st.title("🤖 Freelancers Bot")
st.subheader("Connecting Freelancers with Clients Using AI")

# --- Supabase login/signup ---
st.sidebar.subheader("Sign Up or Log In")

email = st.sidebar.text_input("Email")
password = st.sidebar.text_input("Password", type="password")
auth_action = st.sidebar.radio("Action", ["Login", "Sign Up"])
auth_button = st.sidebar.button("Go")

user = None

if auth_button:
    try:
        if auth_action == "Sign Up":
            result = supabase.auth.sign_up({"email": email, "password": password})
        else:
            result = supabase.auth.sign_in_with_password({"email": email, "password": password})
        user = result.user
        if user:
            st.success(f"Welcome, {email}")
            st.session_state["logged_in"] = True
            st.session_state["user_email"] = email
    except Exception as e:
        st.error(f"Auth failed: {e}")

if st.session_state.get("logged_in", False):
    st.sidebar.success("Logged in as " + st.session_state["user_email"])
    user_role = st.sidebar.radio("Select Role", ["Client", "Freelancer"])

    if user_role == "Client":
        st.header("📝 Post a Job")
        title = st.text_input("Job Title")
        description = st.text_area("Job Description")
        skills = st.text_input("Required Skills (comma-separated)")
        post_btn = st.button("Post Job")

        if post_btn:
            save_job_post(st.session_state["user_email"], title, description, skills)
            st.success("✅ Job posted!")

    elif user_role == "Freelancer":
        st.header("🎯 Matched Jobs")
        st.info("We’ll match jobs based on your skills using AI.")
        skills_input = st.text_input("Enter your skills (comma-separated)")
        match_btn = st.button("Find Matches")

        if match_btn:
            jobs = load_jobs()
            matches = get_job_matches(skills_input, jobs)
            st.subheader("Top Matches:")
            for job in matches:
                st.write(f"**{job['title']}** by {job['client']}")
                st.write(f"🔹 Description: {job['description']}")
                st.write(f"🔧 Required Skills: {job['skills']}")
                st.markdown("---")