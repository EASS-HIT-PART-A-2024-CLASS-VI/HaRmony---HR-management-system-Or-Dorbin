import streamlit as st

# Set page configuration
st.set_page_config(page_title="HaRmony", layout="wide", initial_sidebar_state="collapsed")

# Create two columns for layout
col1, col2 = st.columns([1, 2])

# Column 2: Display the man image
with col2:
    st.image("assets/homepagemanvector.jpg", width=450)

# Column 1: Display logo and text
with col1:
    st.image("assets/HaRmonyLogo.png", width=300, caption="HaRmony Logo")
    st.markdown(
        """
        <div style='display: flex; flex-direction: column; align-items: center;'>
            <h2 style='text-align: center; font-family: Calibri;'>everything needed for HR!</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

# Buttons for Sign In and Log In
st.markdown(
    """
    <div style='display: flex; justify-content: center; margin-top: 20px;'>
        <a href='http://localhost:8501/register' style="text-decoration: none;">
            <button style="background-color: #001F54; color: white; font-size: 18px; padding: 10px 20px; border: none; border-radius: 5px; margin-right: 10px;">Sign In</button>
        </a>
        <a href='http://localhost:8501/login' style="text-decoration: none;">
            <button style="background-color: #F0F0F0; color: black; font-size: 18px; padding: 10px 20px; border: 1px solid #CCC; border-radius: 5px;">Log In</button>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

# Styling for hover effects
st.markdown(
    """
    <style>
        button:hover {
            filter: brightness(0.9);
            cursor: pointer;
        }
    </style>
    """,
    unsafe_allow_html=True
)
