import requests
import streamlit as st
from datetime import date
import json

# Set page configuration
st.set_page_config(page_title="Formation Days", page_icon="🙏​", layout="wide", initial_sidebar_state="collapsed", menu_items={})
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

hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;} 
    footer {visibility: hidden;} 
    header {visibility: hidden;} 
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


# Retrieve logged-in user
logged_in_user = st.session_state.get("logged_in_user", "USERNAME")

# Top navigation bar
st.markdown(
    f"""
    <div style="display: flex; justify-content: space-between; align-items: center; width: 100%; padding: 10px; background-color: #f7f7f7;">
        <div style="display: flex; gap: 20px; font-family: Calibri; font-size: 18px;">
            <a href="http://localhost:8501/home" target="_self" style="text-decoration: none; color: black;">Log out</a>
            <a href="http://localhost:8501/potential_recruits" target="_self" style="text-decoration: none; color: black;">Potential recruits</a>
            <a href="http://localhost:8501/happy_hour" target="_self" style="text-decoration: none; color: black;">Happy Hour</a>
            <a href="http://localhost:8501/formation_days" target="_self" style="text-decoration: none; color: black; background-color: #e0e0e0; padding: 5px 10px; border-radius: 5px;">Formation days</a>
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

# Title under the navigation bar
st.image("http://localhost:8000/assets/formationdaystitle.png", width=600)


# Styling buttons with CSS
st.markdown(
    """
<style>
.button-container {
    display: flex; 
    justify-content: space-evenly; 
    flex-wrap: nowrap; 
    width: 100%;
    gap: 20px; 
}

button {
    background-color: #a4c2db; 
    color: white;
    border: none;
    border-radius: 5px;
    padding: 15px 30px;
    font-size: 16px;
    cursor: pointer;
    text-align: center;
    margin: 5px;
    flex: 1; 
}

button:hover {
    background-color: #3333db; 
    color: #ffffff;
}

button:hover p{
    color: #ffffff;
}

button:focus {
    outline: none;
    color: white;
    background-color: #a4c2db;
    border: none;
}

button:focus p{
    color: #ffffff;
}
</style>



    """,
    unsafe_allow_html=True,
)

# Define options
buttons = [
    "View Approved Places",
    "Create Approved Place",
    "Create Formation Event",
    "Get Past Formation Days",
    "Get Upcoming Formation Event",
]


# Create 5 columns for buttons
col1, col2, col3, col4, col5 = st.columns(5)

# Place buttons in columns
with col1:
    if st.button("View Approved Places"):
        st.session_state["selected_button"] = "View Approved Places"

with col2:
    if st.button("Create Approved Place"):
        st.session_state["selected_button"] = "Create Approved Place"

with col3:
    if st.button("Create Formation Event"):
        st.session_state["selected_button"] = "Create Formation Event"

with col4:
    if st.button("Get Past Formation Days"):
        st.session_state["selected_button"] = "Get Past Formation Days"

with col5:
    if st.button("Get Upcoming Formation Event"):
        st.session_state["selected_button"] = "Get Upcoming Formation Event"

# Display content for the selected button
selected_button = st.session_state.get("selected_button")

if selected_button == "View Approved Places":
    st.subheader("Approved Places")
    try:
        response = requests.get("http://backend:8000/formation_events/approved_places/")
        if response.status_code == 200:
            approved_places = response.json()
            for place in approved_places:
                st.markdown(
                    f"""
                    <div style="background-color: #e4e2f6; border: 1px solid #040465; padding: 10px; margin-bottom: 10px;">
                        <strong>Name:</strong> {place['name']}<br>
                        <strong>Location:</strong> {place['location']}<br>
                        <strong>Description:</strong> {place['description']}<br>
                        <strong>Website:</strong> <a href="{place['website_url']}" target="_blank">{place['website_url']}</a>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
        else:
            st.error("Failed to fetch approved places.")
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching approved places: {str(e)}")

elif selected_button == "Create Approved Place":
    st.subheader("Create a New Approved Place")
    with st.form("create_approved_place_form"):
        name = st.text_input("Name")
        location = st.text_input("Location")
        description = st.text_area("Description")
        website_url = st.text_input("Website URL")
        submit = st.form_submit_button("Submit")

        if submit:
            payload = {
                "name": name,
                "location": location,
                "description": description,
                "website_url": website_url,
            }
            try:
                response = requests.post(
                    "http://backend:8000/formation_events/create_place/",
                    headers={"Content-Type": "application/json"},
                    data=json.dumps(payload),
                )
                if response.status_code == 200:
                    st.success("Place created successfully!")
                else:
                    st.error("Failed to create place.")
            except requests.exceptions.RequestException as e:
                st.error(f"Error creating place: {str(e)}")

elif selected_button ==  "Create Formation Event":
    st.subheader("Create a New Formation Event")
    with st.form("create_formation_event_form"):
        name = st.text_input("Name")
        event_date = st.date_input("Date", min_value=date.today())
        location = st.text_input("Location")
        organizer = st.text_input("Organizer")
        description = st.text_area("Description")
        event_type = st.selectbox("Type", ["Formation"])
        images = st.text_area("Images (enter URLs separated by commas)")
        submit = st.form_submit_button("Submit")

        if submit:
            payload = {
                "name": name,
                "date": str(event_date),
                "location": location,
                "organizer": organizer,
                "description": description,
                "type": event_type,
                "images": images,
            }
            try:
                response = requests.post(
                    "http://backend:8000/formation_events/create_event/",
                    headers={"Content-Type": "application/json"},
                    data=json.dumps(payload),
                )
                if response.status_code == 200:
                    st.success("Formation event created successfully!")
                else:
                    st.error("Failed to create formation event.")
            except requests.exceptions.RequestException as e:
                st.error(f"Error creating formation event: {str(e)}")

elif selected_button ==  "Get Past Formation Days":
    st.subheader("Past Formation Days")
    try:
        response = requests.get("http://backend:8000/formation_events/past/")
        if response.status_code == 200:
            past_events = response.json()
            for event in past_events:
                st.markdown(
                    f"""
                    <div style="background-color: #e4e2f6; border: 1px solid #040465; padding: 10px; margin-bottom: 10px;">
                        <strong>Name:</strong> {event['name']}<br>
                        <strong>Date:</strong> {event['date']}<br>
                        <strong>Location:</strong> {event['location']}<br>
                        <strong>Organizer:</strong> {event['organizer']}<br>
                        <strong>Description:</strong> {event['description']}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
        else:
            st.error("Failed to fetch past formation days.")
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching past formation days: {str(e)}")

elif selected_button == "Get Upcoming Formation Event":
    st.subheader("Upcoming Formation Events")
    try:
        response = requests.get("http://backend:8000/formation_events/upcoming/")
        if response.status_code == 200:
            upcoming_events = response.json()
            for event in upcoming_events:
                st.markdown(
                    f"""
                    <div style="background-color: #e4e2f6; border: 1px solid #040465; padding: 10px; margin-bottom: 10px;">
                        <strong>Name:</strong> {event['name']}<br>
                        <strong>Date:</strong> {event['date']}<br>
                        <strong>Location:</strong> {event['location']}<br>
                        <strong>Organizer:</strong> {event['organizer']}<br>
                        <strong>Description:</strong> {event['description']}<br>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
        else:
            st.error("Failed to fetch upcoming formation events.")
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching upcoming formation events: {str(e)}")
