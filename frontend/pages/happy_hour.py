import requests
import streamlit as st
from datetime import date, datetime
import json
from streamlit_extras.let_it_rain import rain


# Set page configuration
st.set_page_config(page_title="Happy Hour", page_icon="🥂", layout="wide", initial_sidebar_state="collapsed", menu_items={})
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

if "rain_shown" not in st.session_state:
    rain(
        emoji="🍷🥂",  
        font_size=70,  
        falling_speed=7,  
        animation_length=0.7,  
    )
    st.session_state.rain_shown = True
# Retrieve logged-in user
logged_in_user = st.session_state.get("logged_in_user", "USERNAME")

# Top navigation bar
st.markdown(
    f"""
    <div style="display: flex; justify-content: space-between; align-items: center; width: 100%; padding: 10px; background-color: #f7f7f7;">
        <div style="display: flex; gap: 20px; font-family: Calibri; font-size: 18px;">
            <a href="http://localhost:8501/home" target="_self" style="text-decoration: none; color: black;">Log out</a>
            <a href="http://localhost:8501/potential_recruits" target="_self" style="text-decoration: none; color: black;">Potential recruits</a>
            <a href="http://localhost:8501/happy_hour" target="_self" style="text-decoration: none; color: black; background-color: #e0e0e0; padding: 5px 10px; border-radius: 5px;">Happy Hour</a>
            <a href="http://localhost:8501/formation_days" target="_self" style="text-decoration: none; color: black;">Formation days</a>
            <a href="http://localhost:8501/workers_information" target="_self" style="text-decoration: none; color: black;">Workers Information</a>
            <a href="http://localhost:8501/AI_assist" target="_self" style="text-decoration: none; color: black;">AI Assist</a>
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
    @font-face {
        font-family: "HandmadeValentine";
        src: url('/assets/fonts/Handmade Valentine.otf') format('opentype');
    }

    @keyframes blink {
        0% { color: #a4c2db; }
        50% { color: #010163; }
        100% { color: #a4c2db; }
    }
    .blinking-title {
        font-size: 60px;
        font-weight: bold;
        text-align: center;
        animation: blink 2s infinite;
        font-family: "HandmadeValentine", "Arial Rounded MT Bold", sans-serif;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        margin: 5px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }

    </style>
    """,
    unsafe_allow_html=True,
)

# Title with blinking effect
st.markdown('<div class="blinking-title">HAPPY HOUR!</div>', unsafe_allow_html=True)

# Layout
col1, col2 = st.columns([1, 1])

# Left column: Text and Button for drawing employees
# Left column: Drawing employees
with col1:
    st.write("""
        Want to add a new twist to the next Happy Hour?
        Suggest an idea and vote for your favorite department to organize it!
        We'll randomly select employees from that department to plan the next amazing Happy Hour. Join the fun!
    """)

    with st.form("draw_employees_form"):
        num_employees = st.slider("Select number of employees", min_value=2, max_value=10, value=5)
        with st.spinner("Loading departments..."):
            response = requests.get("http://backend:8000/Employees/departments/")
            if response.status_code == 200:
                departments = response.json()
            else:
                st.error("Failed to fetch departments.")
                departments = ["No departments available"]

        department = st.selectbox("Select department", departments)
        submitted = st.form_submit_button("Draw")

        if submitted:
            payload = {
                "department": department,
                "num_employees": num_employees
            }
            response = requests.post(
                "http://backend:8000/happy_hour/draw/",
                params=payload  
            )
            if response.status_code == 200:
                employees = response.json().get("employees", [])
                selected_employees = "\n".join([f"{employee['full_name']} ({employee['email']})" for employee in employees])
                st.info(f"Employees Selected:\n{selected_employees}")
            else:
                st.error(response.json().get("detail", "Failed to draw employees."))




# Right column: Calendar and upcoming events
with col2:
    st.write("### Upcoming Events")
    response = requests.get("http://backend:8000/happy_hour/events/all/")
    if response.status_code == 200:
        events = response.json()
        for event in events:
            st.write(f"- **{event['name']}** on {event['date']} at {event['location']} (Organizer: {event['organizer']})")
    else:
        st.warning("No upcoming events.")




st.title("Create a New Happy Hour Event")

with st.form("happy_hour_form", clear_on_submit=True):
    st.subheader("Fill in the Event Details:")
    
    name = st.text_input("Event Name", placeholder="Enter the name of the event")
    event_date = st.date_input("Event Date", min_value=date.today())
    location = st.text_input("Event Location", placeholder="Enter the event location")
    organizer = st.text_input("Event Organizer", placeholder="Enter the organizer's name")
    
    submitted = st.form_submit_button("Create Event")

    if submitted:
        if not name or not location or not organizer:
            st.error("All fields are required. Please fill in all the details.")
        else:
            payload = {
                "name": name,
                "date": str(event_date),
                "location": location,
                "organizer": organizer,
            }
            
            try:
                response = requests.post(
                    "http://backend:8000/happy_hour/event/",
                    headers={"Content-Type": "application/json"},
                    data=json.dumps(payload),
                )
                
                if response.status_code == 200:
                    st.success("Event created successfully!")
                    rain(
                        emoji="🎊🎉",  
                        font_size=64,  
                        falling_speed=8,  
                        animation_length=2,  
                         )
                else:
                    error_message = response.json().get("detail", "An error occurred while creating the event.")
                    st.error(f"Failed to create event: {error_message}")
            except requests.exceptions.RequestException as e:
                st.error(f"An error occurred: {str(e)}")