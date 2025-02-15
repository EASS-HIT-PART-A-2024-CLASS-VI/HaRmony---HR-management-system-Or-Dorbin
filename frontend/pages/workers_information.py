import streamlit as st
import requests
from datetime import datetime
import streamlit.components.v1 as components
import random


st.set_page_config(page_title="Employees", layout="wide", initial_sidebar_state="collapsed")

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
                <a href="http://localhost:8501/home" style="text-decoration: none; color: black;">Home</a>
                <a href="http://localhost:8501/potential_recruits" style="text-decoration: none; color: black;">Potential recruits</a>
                <a href="http://localhost:8501/happy_hour" style="text-decoration: none; color: black;">Happy Hour</a>
                <a href="http://localhost:8501/formation_days" style="text-decoration: none; color: black;">Formation days</a>
                <a href="http://localhost:8501/workers_information" style="text-decoration: none; color: black;background-color: #e0e0e0; padding: 5px 10px; border-radius: 5px;">Workers Information</a>
            </div>
            <div style="display: flex; align-items: center; gap: 10px;">
                <span style="font-family: Calibri; font-size: 18px;">{user}</span>
                <img src="http://localhost:8000/assets/usernamedisplay.png" alt="User Icon" width="30" style="border-radius: 50%;">
                <img src="http://localhost:8000/assets/HaRmonyLogo.png" alt="HaRmony Logo" width="120">
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_title_image():
    st.image("http://localhost:8000/assets/WorkerPageTitle.png", width=600)

def get_employees():
    response = requests.get("http://backend:8000/Employees/")
    if response.status_code == 200:
        return response.json()
    return []

def get_birthday_employees():
    month = datetime.now().month
    response = requests.get(f"http://backend:8000/Employees/birthdays/?month={month}")
    if response.status_code == 200:
        return response.json()
    return []

if "employees" not in st.session_state:
    st.session_state["employees"] = get_employees()

if "show_birthdays" not in st.session_state:
    st.session_state["show_birthdays"] = False


employees = st.session_state["employees"]

def calculate_age(birthdate):
    if not birthdate or birthdate in ["", None]:  
        return "Unknown Age"  

    try:
        if isinstance(birthdate, str):  
            birth_date = datetime.strptime(birthdate, "%Y-%m-%d")  
        elif isinstance(birthdate, datetime):  
            birth_date = birthdate
        else:
            return "Invalid Date Format"  

        today = datetime.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return f"Age: {age}"
    except ValueError:
        return "Invalid Date Format"  


def render_employee_cards(employees, birthday_employees=[]):
    num_columns = 4
    cols = st.columns(num_columns)
    birthday_employees = get_birthday_employees() if st.session_state["show_birthdays"] else []
    birthday_ids = {emp['id'] for emp in birthday_employees if 'id' in emp}

    for index, emp in enumerate(employees):
        emp_id = emp.get('id', None)
        bg_color = "#e8f5e9" if emp_id in birthday_ids else "#ffffff"

        birthdate = emp.get("date_of_birth", None)  
        age_text = calculate_age(birthdate) 

        with cols[index % num_columns]:
            st.markdown(
                f"""
                <div style="
                    border: 1px solid #ddd; 
                    border-radius: 10px; 
                    padding: 15px; 
                    background-color: {bg_color}; 
                    box-shadow: 2px 2px 5px rgba(0,0,0,0.2); 
                    text-align: center;
                    width: 100%; 
                    margin-bottom: 5px;
                ">
                    <img src="{emp.get('image_url', 'http://localhost:8000/uploads/employees_pictures/default.png')}" 
                         alt="{emp['full_name']}" 
                         style="width: 120px; height: 120px; border-radius: 50%; margin-bottom: 10px;">
                    <h4>{emp['full_name']}</h4>
                    <p>{age_text}</p>
                    <p>Email: {emp['email']}</p>
                    <p>Department: {emp['department']}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )




def show_birthdays():
    birthday_employees = get_birthday_employees()
    if birthday_employees:
        st.session_state["balloons_shown"] = False  
        employee_names = ", ".join([emp["full_name"] for emp in birthday_employees])  
        st.success(f"🎉 Happy Birthday to {employee_names}!")  
    else:
        st.warning("No employees are celebrating birthdays this month.")
    return birthday_employees




def search_employees(query):
    response = requests.get(f"http://backend:8000/Employees/search/?name={query}")
    if response.status_code == 200:
        employees = response.json()
        if employees:
            st.session_state["employees"] = employees  
            st.session_state["show_birthdays"] = False  
        else:
            st.warning("No employees found matching your search.")
    else:
        st.error("Failed to fetch employees. Please try again.")

# Run all components
logged_in_user = st.session_state.get("logged_in_user", "USERNAME")
render_top_navbar(logged_in_user)
render_title_image()

# Employee Search
search_query = st.text_input("Search Employees", placeholder="Enter employee name...")
if st.button("Search Employees"):
    search_employees(search_query)


if st.button("Show Birthdays This Month"):
    st.session_state["show_birthdays"] = not st.session_state["show_birthdays"]  
    st.session_state["employees"] = get_employees()  
    st.session_state["balloons_shown"] = False
    if st.session_state["show_birthdays"]:
        show_birthdays() 
        st.balloons()

render_employee_cards(st.session_state["employees"])

