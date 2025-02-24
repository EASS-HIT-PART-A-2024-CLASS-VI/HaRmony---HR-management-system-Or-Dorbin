import requests
import streamlit as st
import datetime
import urllib.parse
from streamlit_extras.switch_page_button import switch_page


# Set page configuration
st.set_page_config(page_title="Potential Recruits",page_icon="🗣️​", layout="wide", initial_sidebar_state="collapsed", menu_items={})
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

def upload_resume(recruit_id, file):
    files = {"file": file}
    response = requests.post(f"http://backend:8000/potential_recruits/{recruit_id}/upload_resume/", files=files)
    if response.status_code == 200:
        st.success("🏆 Resume uploaded successfully!")
    else:
        st.error("❌ Failed to upload resume.")


def download_resume(recruit_id):
    response = requests.get(f"http://backend:8000/potential_recruits/{recruit_id}/download_resume/")
    if response.status_code == 200:
        with open(f"resume_{recruit_id}.pdf", "wb") as f:
            f.write(response.content)
        st.success(f"💾 Resume for recruit {recruit_id} downloaded successfully!")
    else:
        st.error("❌ Failed to download resume.")



# Top navigation bar
st.markdown(
    f"""
    <div style="display: flex; justify-content: space-between; align-items: center; width: 100%; padding: 10px; background-color: #f7f7f7;">
        <div style="display: flex; gap: 20px; font-family: Calibri; font-size: 18px;">
            <a href="http://localhost:8501/home?logout=true" target="_self" style="text-decoration: none; color: black;">Log out</a>
            <a href="http://localhost:8501/potential_recruits?logged_in_user={logged_in_user}" target="_self" style="text-decoration: none; color: black; background-color: #e0e0e0; padding: 5px 10px; border-radius: 5px;">Potential recruits</a>
            <a href="http://localhost:8501/happy_hour?logged_in_user={logged_in_user}" target="_self" style="text-decoration: none; color: black;">Happy Hour</a>
            <a href="http://localhost:8501/formation_days?logged_in_user={logged_in_user}" target="_self" style="text-decoration: none; color: black;">Formation days</a>
            <a href="http://localhost:8501/workers_information?logged_in_user={logged_in_user}" target="_self" style="text-decoration: none; color: black;">Workers Information</a>
            <a href="http://localhost:8501/AI_assist?logged_in_user={logged_in_user}" target="_self" style="text-decoration: none; color: black;">AI Assist</a>
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

 /* Add Recruit Form - Green */
    .add-recruit input[type="text"], .add-recruit input[type="number"], .add-recruit textarea, .add-recruit .stDateInput input {
        border: 2px solid #4CAF50; /* Green border */
        border-radius: 5px;
        padding: 5px;
    }
    .add-recruit input[type="text"]:hover, .add-recruit input[type="number"]:hover, .add-recruit textarea:hover, .add-recruit .stDateInput input:hover {
        border-color: #45a049; /* Darker green on hover */
    }
    .add-recruit input[type="text"]:focus, .add-recruit input[type="number"]:focus, .add-recruit textarea:focus, .add-recruit .stDateInput input:focus {
        outline: none;
        box-shadow: 0 0 5px #45a049; /* Glow effect */
        border-color: #45a049;
    }

    /* Delete Recruit Form - Red */
    .delete-recruit input[type="text"], .delete-recruit input[type="number"], .delete-recruit textarea, .delete-recruit .stDateInput input {
        border: 2px solid #FF5733; /* Red border */
        border-radius: 5px;
        padding: 5px;
    }
    .delete-recruit input[type="text"]:hover, .delete-recruit input[type="number"]:hover, .delete-recruit textarea:hover, .delete-recruit .stDateInput input:hover {
        border-color: #E74C3C; /* Darker red on hover */
    }
    .delete-recruit input[type="text"]:focus, .delete-recruit input[type="number"]:focus, .delete-recruit textarea:focus, .delete-recruit .stDateInput input:focus {
        outline: none;
        box-shadow: 0 0 5px #E74C3C; /* Glow effect */
        border-color: #E74C3C;
    }
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


# Add Recruit Form
with st.expander("✅ Add a new recruit", expanded=False):
    with st.container():
        st.markdown('<div class="add-recruit">', unsafe_allow_html=True)
        with st.form("add_recruit_form"):
            first_name = st.text_input("First Name")
            last_name = st.text_input("Last Name")
            phone_number = st.text_input("Phone Number")
            email = st.text_input("Email")
            date_of_birth = st.date_input(
                "Date of Birth",
                min_value=datetime.date(1900, 1, 1),
                max_value=datetime.date.today(),
            )
            age = st.number_input("Age", min_value=18, max_value=100, step=1)
            role_description = st.text_input("Role Description")
            description = st.text_area("Description")
            resume_file = st.file_uploader("Upload Resume (PDF)", type="pdf")
            if st.form_submit_button("Add Recruit"):
                payload = {
                    "first_name": first_name,
                    "last_name": last_name,
                    "phone_number": phone_number,
                    "email": email,
                    "date_of_birth": str(date_of_birth),
                    "age": age,
                    "role_description": role_description,
                    "description": description,
                }
                response = requests.post("http://backend:8000/potential_recruits/", json=payload)
                if response.status_code == 200:
                    recruit_id = response.json()["id"]
                    if resume_file:
                        upload_resume(recruit_id, resume_file)
                    st.success("Recruit added successfully!")
                    st.rerun()
                else:
                    st.error(f"Failed to add recruit: {response.text}")
        st.markdown('</div>', unsafe_allow_html=True)

# Delete Recruit Form
with st.expander("❌ Delete a Recruit through ID", expanded=False):
    with st.container():
        st.markdown('<div class="delete-recruit">', unsafe_allow_html=True)
        recruit_id = st.text_input("Recruit ID")
        if st.button("Delete Recruit"):
            if recruit_id:
                response = requests.delete(f"http://backend:8000/potential_recruits/{recruit_id}")
                if response.status_code == 200:
                    st.success("Recruit deleted successfully!")
                    st.rerun()  # Refresh the page to update the list
                else:
                    st.error(f"Failed to delete recruit: {response.text}")
            else:
                st.warning("Please enter a valid Recruit ID.")
        st.markdown('</div>', unsafe_allow_html=True)



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
                    <p>ID: <small style="color: gray;">{recruit['id']}</small></p>
                    <p><i>{recruit['role_description']}</i></p>
                    <p>{recruit['description']}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

            # Toggle for Resume Actions
            show_resume_options = st.toggle(f"📂 Slide me for Resume Options", key=f"resume_toggle_{recruit['id']}")

            if show_resume_options:
                uploaded_file = st.file_uploader(f"📤 Upload Resume", type="pdf", key=f"upload_{recruit['id']}")
                if uploaded_file and st.button(f"📤 Upload {recruit['first_name']}'s Resume", key=f"btn_upload_{recruit['id']}"):
                    upload_resume(recruit['id'], uploaded_file)

                st.markdown(
                    f'<a href="http://localhost:8000/potential_recruits/{recruit["id"]}/download_resume/" '
                    f'download="resume_{recruit["id"]}.pdf" '
                    f'style="text-decoration: none;">'
                    f'<button style="background-color: #007bff; color: white; padding: 10px; border-radius: 5px; border: none; cursor: pointer;">'
                    f'📥 Download {recruit["first_name"]}\'s Resume</button></a>',
                    unsafe_allow_html=True
                )

else:
    st.warning("No recruits found.")
