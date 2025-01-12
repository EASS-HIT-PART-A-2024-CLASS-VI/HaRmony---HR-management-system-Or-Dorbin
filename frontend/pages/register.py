import streamlit as st
import requests

st.set_page_config(page_title="HaRmony - Registration", layout="centered", initial_sidebar_state="collapsed")

# Display logo
st.image("assets/HaRmonyLogo.png", width=200)

# Layout with the image on the left
col1, col2 = st.columns([1, 2])

with col1:
    st.image("assets/registerpagevector.jpg", use_container_width=True)

with col2:
    st.markdown("<h3>Register for HaRmony</h3>", unsafe_allow_html=True)
    username = st.text_input("Enter Username")
    password = st.text_input("Enter Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    company_role = st.text_input("Company Role")
    company_name = st.text_input("Company Name")
    
if st.button("Continue"):
    if password != confirm_password:
        st.error("Passwords do not match!")
    else:
        try:
            response = requests.post(
                "http://backend:8000/auth/register/",
                json={
                    "username": username,
                    "password": password,
                    "role": company_role,
                    "company": company_name,
                },
            )
            if response.status_code == 200:
                result = response.json()
                st.success(f"{result['message']}. [Click here to login](http://localhost:8501/login)")
            else:
                st.error("An error occurred. Please try again.")
        except Exception as e:
            st.error(f"Unable to connect to the backend service: {str(e)}")
