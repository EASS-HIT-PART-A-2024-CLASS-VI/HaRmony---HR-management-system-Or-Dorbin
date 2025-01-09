
<img width="929" alt="image" src="https://github.com/user-attachments/assets/5411c39b-809f-4199-933d-ff3e88f84ba0" />



HaRmony
Human Resources Management Interface System

Overview
HaRmony is a comprehensive web-based Human Resources management system. It provides tools for managing employee data, potential recruits, company events, and team-building activities. The project includes a backend developed with FastAPI and a frontend using Streamlit, fully containerized for deployment with Docker.

Table of Contents
Technologies Used
Project Features
Project Structure
Endpoints (Backend)
How to Run the Project
Future Work
Contact Info
Technologies Used
Backend:
Python 3.10+
FastAPI – A modern and fast web framework for building APIs.
SQLAlchemy – ORM for database management.
PostgreSQL – Relational database.
CORS Middleware – To enable frontend-backend communication.
Frontend:
Streamlit – A Python-based web application framework for a user-friendly interface.
Containerization:
Docker – For creating isolated containers for the backend and frontend.
Docker Compose – To orchestrate multi-container services.
Project Features
Backend:
Management of potential recruits with CRUD operations.
Tracking and management of team-building events.
Employee data management, including department-wise filtering and birthday celebrations.
Supports authentication and user roles for secure access.
Frontend:
Interactive UI for HR tasks.
Display and search functionalities for employees and events.
Calendar-based views for team-building events.
Confetti effects for "Happy Hour" celebrations.
Project Structure
graphql
Copy code
HaRmony/
├── backend/
│   ├── app/
│   │   ├── main.py              # Entry point for the FastAPI application
│   │   ├── crud.py              # Contains CRUD functions
│   │   ├── database.py          # Database connection and session management
│   │   ├── models.py            # SQLAlchemy models for DB tables
│   │   ├── schemas.py           # Pydantic schemas for data validation
│   │   ├── routes/
│   │   │   ├── login.py         # Authentication routes
│   │   │   ├── register.py      # User registration routes
│   │   │   ├── employees.py     # Employee management routes
│   │   │   ├── happy_hour.py    # Routes for Happy Hour management
│   │   │   ├── formation_events.py # Routes for team-building events
│   │   │   ├── potential_recruits.py # Routes for potential recruits
│   ├── requirements.txt         # Backend dependencies
│   ├── Dockerfile               # Backend container configuration
├── frontend/
│   ├── login.py                 # Streamlit-based frontend entry point
│   ├── package.json             # Frontend dependencies
│   ├── package-lock.json        # Dependency tree lock
│   ├── Dockerfile               # Frontend container configuration
├── docker-compose.yml           # Multi-container orchestration
└── README.md                    # Project documentation
Endpoints (Backend)
Formation Events:
GET /formation_events/upcoming/
Returns a list of upcoming team-building events.

GET /formation_events/past/
Returns a list of past team-building events.

POST /formation_events/create_event/
Allows creating a new team-building event.

GET /formation_events/approved_places/
Returns a list of approved places for team-building events.

POST /formation_events/create_place/
Allows adding a new approved place.

How to Run the Project
Prerequisites:
Docker and Docker Compose installed.
Steps:
Clone the Repository:

bash
Copy code
git clone https://github.com/your-repo-link.git
cd HaRmony
Build and Run Containers:

bash
Copy code
docker-compose up --build
Backend available at: http://localhost:8000
Frontend available at: http://localhost:8501
Use the Application:

Access the frontend at http://localhost:8501 and explore HR features.
Future Work
Implement advanced analytics for employee performance and recruit tracking.
Add user authentication and roles to the frontend.
Integrate real-time notifications for event updates.
Contact Info
Project Author: Or Dorbin
Email: ordorbin13@gmail.com
GitHub: Or Dorbin

