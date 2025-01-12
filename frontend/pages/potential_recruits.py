import requests
import streamlit as st

# Set page configuration
st.set_page_config(page_title="Potential Recruits", layout="wide", initial_sidebar_state="collapsed")


# Check if the user is logged in

# Retrieve logged-in user
logged_in_user = st.session_state.get("logged_in_user", "USERNAME")


# Top navigation bar
st.markdown(
    f"""
    <div style="display: flex; justify-content: space-between; align-items: center; width: 100%; padding: 10px; background-color: #f7f7f7;">
        <div style="display: flex; gap: 20px; font-family: Calibri; font-size: 18px;">
            <a href="http://localhost:8501/home" style="text-decoration: none; color: black;">Home</a>
            <a href="http://localhost:8501/potential_recruits" style="text-decoration: none; color: black; background-color: #e0e0e0; padding: 5px 10px; border-radius: 5px;">Potential recruits</a>
            <a href="http://localhost:8501/happy_hour" style="text-decoration: none; color: black;">Happy Hour</a>
            <a href="http://localhost:8501/formation_days" style="text-decoration: none; color: black;">Formation days</a>
            <a href="http://localhost:8501/workers_information" style="text-decoration: none; color: black;">Workers Information</a>
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

# CSS for styling
st.markdown(
    """
    <style>
  
    .stButton > button {
        background-color: #007bff;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
    }
    .stButton > button:hover {
        background-color: #0056b3;
    }
    .recruit-card {
        text-align: center;
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 15px;
        background-color: #f9f9f9;
        margin: 10px;
    }
    .recruit-card img {
        width: 80px;
        height: 80px;
        border-radius: 50%;
        margin-bottom: 10px;
    }
    .recruit-card h3 {
        margin: 5px 0;
    }
    .recruit-card p {
        margin: 5px 0;
        color: gray;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

 #Streamlit search bar logic
search_query = st.text_input("Search recruits", placeholder="Search recruits here...", key="search_input")
if st.button("Search"):
    # Send request based on user input
    if search_query.strip():
        response = requests.get(f"http://backend:8000/potential_recruits/search/?keyword={search_query}")
        recruits = response.json() if response.status_code == 200 else []
    else:
        recruits = []
        st.warning("Please enter a search query.")
else:
    # Default behavior to fetch all recruits
    response = requests.get("http://backend:8000/potential_recruits/")
    recruits = response.json() if response.status_code == 200 else []

# Display recruits
st.markdown("---")
if recruits:
    recruit_cols = st.columns(4)
    for index, recruit in enumerate(recruits):
        with recruit_cols[index % 4]:
            st.markdown(
                f"""
                <div class="recruit-card">
                    <img src="http://localhost:8000/assets/recruitsphotos/{index+1}.png" alt="Profile Picture">
                    <h3>{recruit['first_name']} {recruit['last_name']}, {recruit['age']}</h3>
                    <p><i>{recruit['role_description']}</i></p>
                    <p>{recruit['description']}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
else:
    st.warning("No recruits found.")
