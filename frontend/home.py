import streamlit as st

st.set_page_config(page_title="HaRmony", layout="wide", initial_sidebar_state="collapsed")

col1, col2, col3 = st.columns([1, 2, 1])  
with col2:  
    st.image("assets/HaRmonyLogo.png", width=200)

    st.markdown("<h2 style='text-align: center;'>everything needed for HR!</h2>", unsafe_allow_html=True)

    st.image("assets/homepagemanvector.jpg", width=150)

    col4, col5 = st.columns([1, 1], gap="large")
    with col4:
        if st.button("Sign In", use_container_width=True):
            st.markdown("[Click here to register](http://localhost:8501/register)", unsafe_allow_html=True)
    with col5:
        if st.button("Log In", use_container_width=True):
            st.markdown("[Click here to login](http://localhost:8501/login)", unsafe_allow_html=True)
