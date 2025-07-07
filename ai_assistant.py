import openai
import streamlit as st

openai.api_key = st.secrets["OPENAI_API_KEY"]

def get_ai_reply(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant for freelancers."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        return f"Error: {e}"