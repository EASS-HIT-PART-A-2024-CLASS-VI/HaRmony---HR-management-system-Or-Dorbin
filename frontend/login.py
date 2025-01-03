import requests
import streamlit as st


st.set_page_config(page_title="HaRmony", layout="centered")
st.markdown("<h1 style='text-align: center; color: navy;'>HaRmony</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>log in to your account</h3>", unsafe_allow_html=True)

# enter user details
username = st.text_input("enter username", key="username")
password = st.text_input("enter password", type="password", key="password")
if st.button("Register"):
    st.markdown("Don't have an account? [Click here to register](http://localhost:8501/register)")

# login button
if st.button("Login"):
    try:
        response = requests.post(
            "http://backend:8000/login/",  # backend service
            json={"username": username, "password": password},
        )
        if response.status_code == 200:
            st.success(f"Welcome, {username}!")
        elif response.status_code == 400:
            st.error("Invalid username or password. Please try again.")
        elif response.status_code == 404:
            st.error("User not found. Please register.")
        else:
            st.error(f"Error: {response.status_code}. Something went wrong.")
    except requests.exceptions.ConnectionError:
        st.error("Unable to connect to the backend. Please check the backend service.")

