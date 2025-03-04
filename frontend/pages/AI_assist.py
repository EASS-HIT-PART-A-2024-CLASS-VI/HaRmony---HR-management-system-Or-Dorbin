import streamlit as st
import requests
import json
import time
import urllib.parse
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="AI Assist", page_icon="🚀", layout="wide", initial_sidebar_state="collapsed", menu_items={})


st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stDeployButton {display:none;}
        .appview-container .main .block-container {
            padding-top: 0rem;
            padding-right: 1rem;
            padding-left: 1rem;
            padding-bottom: 1rem;
        }
        .stApp > header {
            display: none;
        }
        .stApp {
            margin-top: -80px;
        }
        section[data-testid="stSidebar"] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)


# Retrieve query params to check if user is logged in
query_params = st.query_params
logged_in_user = query_params.get("logged_in_user", [None]) # Extract username

if isinstance(logged_in_user, list) and len(logged_in_user) == 1:
    logged_in_user = logged_in_user[0]  
elif isinstance(logged_in_user, list):  
    logged_in_user = "".join(logged_in_user)  

# If query param exists, store it in session state
if logged_in_user and logged_in_user != "None":
    st.session_state["logged_in_user"] = logged_in_user
else:
    # Default to session state or Guest
    logged_in_user = st.session_state.get("logged_in_user", "Guest")

# Logout Handling
if "logout" in query_params:
    st.session_state["logged_in_user"] = "Guest"
    switch_page("login")  # Redirect to login page


def render_top_navbar(user):
    st.markdown(
        f"""
        <script>
        function navigate(url) {{
            window.location.href = url;
        }}
        </script>

        <div style="display: flex; justify-content: space-between; align-items: center; width: 100%; padding: 10px; background-color: #f7f7f7;">
            <div style="display: flex; gap: 20px; font-family: Calibri; font-size: 18px;">
                <a href="http://localhost:8501/home?logout=true" target="_self" style="text-decoration: none; color: black;">Log out</a>
                <a href="http://localhost:8501/potential_recruits?logged_in_user={logged_in_user}" target="_self" style="text-decoration: none; color: black;">Potential recruits</a>
                <a href="http://localhost:8501/happy_hour?logged_in_user={logged_in_user}" target="_self" style="text-decoration: none; color: black;">Happy Hour</a>
                <a href="http://localhost:8501/formation_days?logged_in_user={logged_in_user}" target="_self" style="text-decoration: none; color: black;">Formation days</a>
                <a href="http://localhost:8501/workers_information?logged_in_user={logged_in_user}" target="_self" style="text-decoration: none; color: black;">Workers Information</a>
                <a href="http://localhost:8501/AI_assist?logged_in_user={logged_in_user}" target="_self" style="text-decoration: none; color: black;background-color: #e0e0e0; padding: 5px 10px; border-radius: 5px;">AI Assist</a>
            </div>
            <div style="display: flex; align-items: center; gap: 10px;">
                <span style="font-family: Calibri; font-size: 18px;">{logged_in_user}</span>
                <img src="http://localhost:8000/assets/usernamedisplay.png" alt="User Icon" width="30" style="border-radius: 50%;">
                <img src="http://localhost:8000/assets/HaRmonyLogo.png" alt="HaRmony Logo" width="120">
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
render_top_navbar(logged_in_user)

st.markdown(
    """
    <div style="text-align: center;">
        <img src="http://localhost:8000/assets/AiAssistTitle.gif" alt="AI Assist Title" width="600">
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("<h2 style='text-align: center; color: #4A90E2;'>🤖 AI Chat Assistant</h2>", unsafe_allow_html=True)

def chat_with_ai(user_query):
    try:
        response = requests.post(
            "http://backend:8000/chat/",  
            headers={"Content-Type": "application/json"},
            json={"prompt": user_query}  
        )
        data = response.json()
        return data if "response" in data else {"error": "Invalid response format"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Could not connect to AI service. Exception: {str(e)}"}


user_query = st.text_input("💬 Ask me anything about HR, recruitment, company events & more:")

if st.button("🚀 Send"):
    if user_query.strip():
        with st.status("Thinking...", expanded=True) as status:
            st.write("Looking for an answer to the question...")
            time.sleep(2)
            st.write("A suitable answer was found.")
            time.sleep(1)
            st.write("Showing an answer soon...")
            time.sleep(1)
            status.update(label="Process complete! Answer displayed to the user", state="complete", expanded=False)
        
        response = chat_with_ai(user_query)
        if response and isinstance(response, dict) and "response" in response:
            st.markdown(f"<div style='background-color: #f1f1f1; padding: 10px; border-radius: 10px;'><strong>🧠 AI Response:</strong><br>{response['response']}</div>", unsafe_allow_html=True)
        else:
            st.error(f"⚠️ {response.get('error', 'Unknown error or invalid response format.')}")
    else:
        st.warning("⚠️ Please enter a question before submitting.")
