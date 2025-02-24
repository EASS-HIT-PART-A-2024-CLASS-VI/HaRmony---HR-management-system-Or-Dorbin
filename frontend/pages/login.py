import requests
import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="HaRmony",page_icon="🔐​", layout="wide", initial_sidebar_state="collapsed")

if "logged_in_user" in st.session_state and st.session_state["logged_in_user"] != "Guest":
    st.switch_page("pages/potential_recruits.py")


st.markdown(
    """
    <div style='text-align: center;'>
        <img src="http://localhost:8000/assets/HaRmonyLogo.png" alt="HaRmony Logo" width="400"/>
        <h3 style='font-family: Calibri;'>log in to your account</h3>
    </div>
    """,
    unsafe_allow_html=True
)

# enter user details
username = st.text_input("enter username", key="username")
password = st.text_input("enter password", type="password", key="password")
if st.button("Register"):
    st.markdown("Don't have an account? [Click here to register](http://localhost:8501/register)")

# login button
if st.button("Login"):
    try:
        response = requests.post(
            "http://backend:8000/auth/login/",  
            json={"username": username, "password": password},
        )
        if response.status_code == 200:
            st.success(f"Welcome, {username}!")
            st.session_state["logged_in_user"] = username 
            switch_page("potential_recruits")

        elif response.status_code == 400:
            st.error("Invalid username or password. Please try again.")
        elif response.status_code == 404:
            st.error("User not found. Please register.")
        else:
            st.error(f"Error: {response.status_code}. Something went wrong.")
    except requests.exceptions.ConnectionError:
        st.error("Unable to connect to the backend. Please check the backend service.")

# Check if redirection is required
if "redirect_to" in st.session_state and st.session_state["redirect_to"] == "potential_recruits":
    st.write("[Redirecting to Potential Recruits page...](http://localhost:8501/potential_recruits)")
    st.stop()
