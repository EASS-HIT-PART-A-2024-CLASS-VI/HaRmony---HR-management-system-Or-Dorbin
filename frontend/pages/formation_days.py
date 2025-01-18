import requests
import streamlit as st
from datetime import date
import json

# Set page configuration
st.set_page_config(page_title="Formation Days", layout="wide", initial_sidebar_state="collapsed")

# Retrieve logged-in user
logged_in_user = st.session_state.get("logged_in_user", "USERNAME")

# Top navigation bar
st.markdown(
    f"""
    <div style="display: flex; justify-content: space-between; align-items: center; width: 100%; padding: 10px; background-color: #f7f7f7;">
        <div style="display: flex; gap: 20px; font-family: Calibri; font-size: 18px;">
            <a href="http://localhost:8501/home" style="text-decoration: none; color: black;">Home</a>
            <a href="http://localhost:8501/potential_recruits" style="text-decoration: none; color: black;">Potential recruits</a>
            <a href="http://localhost:8501/happy_hour" style="text-decoration: none; color: black;">Happy Hour</a>
            <a href="http://localhost:8501/formation_days" style="text-decoration: none; color: black; background-color: #e0e0e0; padding: 5px 10px; border-radius: 5px;">Formation days</a>
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

# Title under the navigation bar
st.image("http://localhost:8000/assets/formationdaystitle.png", width=600)

# Dashboard buttons on the page
st.markdown("### Please select an option below to view details:")
selected_section = st.radio(
    "",
    options=[
        "View Approved Places",
        "Create Approved Place",
        "Create Formation Event",
        "Get Past Formation Days",
        "Get Upcoming Formation Event",
    ],
    index=0,
    label_visibility="collapsed",
)

# Colors for active and inactive buttons
active_color = "#3333db"
inactive_color = "#a4c2db"

# Dynamically display sections based on the selected button
if selected_section == "View Approved Places":
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

elif selected_section == "Create Approved Place":
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

elif selected_section == "Create Formation Event":
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

elif selected_section == "Get Past Formation Days":
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

elif selected_section == "Get Upcoming Formation Event":
    st.subheader("Upcoming Formation Events")
    try:
        response = requests.get("http://backend:8000/formation_events/upcoming/")
        if response.status_code == 200:
            upcoming_events = response.json()
            st.json(upcoming_events)  # Temporary JSON display for upcoming events
        else:
            st.error("Failed to fetch upcoming formation events.")
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching upcoming formation events: {str(e)}")
