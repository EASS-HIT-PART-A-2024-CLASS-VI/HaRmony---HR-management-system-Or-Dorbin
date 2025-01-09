
# HaRmony
**Human Resources Management Interface System**

<img width="929" alt="image" src="https://github.com/user-attachments/assets/5411c39b-809f-4199-933d-ff3e88f84ba0" />
---

## Overview
HaRmony is a comprehensive web-based Human Resources management system. It provides tools for managing employee data, potential recruits, company events, and team-building activities. The project includes three main services:

1. **Backend:** Built with FastAPI to handle all server-side logic and database interactions.
2. **Frontend:** Developed with Streamlit for a user-friendly interface.
3. **Database:** PostgreSQL to store and manage all the HR-related data.

---

## Table of Contents
1. [Technologies Used](#technologies-used)
2. [Project Features](#project-features)
3. [Project Structure](#project-structure)
4. [Endpoints (Backend)](#endpoints-backend)
5. [How to Run the Project](#how-to-run-the-project)
6. [Future Work](#future-work)
7. [Contact Info](#contact-info)

---

## Technologies Used

### Backend:
- **Python 3.10+**
- **FastAPI** – A modern and fast web framework for building APIs.
- **SQLAlchemy** – ORM for database management.
- **PostgreSQL** – Relational database.
- **CORS Middleware** – To enable frontend-backend communication.

### Frontend:
- **Streamlit** – A Python-based web application framework for an interactive interface.

### Database:
- **PostgreSQL** – A powerful open-source relational database.

### Containerization:
- **Docker** – For creating isolated containers for the backend, frontend, and database.
- **Docker Compose** – To orchestrate multi-container services.

---

## Project Features

### Backend:
- User authentication and secure access.
- CRUD operations for potential recruits and employees.
- Management of team-building events and "Happy Hour" celebrations.

### Frontend:
- Interactive and user-friendly interface for HR management.
- Search and filter functionalities for employees and events.
- Calendar-based views for team-building activities.

### Database:
- Stores all user, employee, recruit, and event data.
- Manages relationships between users, events, and approved locations.

---

## Project Structure
```plaintext
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
```

---

## Endpoints (Backend)

### Formation Events:
- **`GET /formation_events/upcoming/`**  
  Returns a list of upcoming team-building events.

- **`GET /formation_events/past/`**  
  Returns a list of past team-building events.

- **`POST /formation_events/create_event/`**  
  Allows creating a new team-building event.

- **`GET /formation_events/approved_places/`**  
  Returns a list of approved places for team-building events.

- **`POST /formation_events/create_place/`**  
  Allows adding a new approved place.

---

## How to Run the Project

### Prerequisites:
- Docker and Docker Compose installed.

### Steps:
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/EASS-HIT-PART-A-2024-CLASS-VI/HaRmony---HR-management-system-Or-Dorbin.git
   cd HaRmony
   ```

2. **Build and Run Containers:**
   ```bash
   docker-compose up --build
   ```
   - Backend available at: [http://localhost:8000](http://localhost:8000)
   - Frontend available at: [http://localhost:8501](http://localhost:8501)

3. **Use the Application:**
   - Access the frontend at [http://localhost:8501](http://localhost:8501) and explore HR features.

---

## Future Work

1. Implement advanced analytics for employee performance and recruit tracking.
2. Add roles and authentication features to the frontend.
3. Integrate real-time notifications for event updates.

---

## Contact Info

- **Project Author:** Or Dorbin  
- **Email:** ordorbin13@gmail.com  
- **GitHub:** [Or Dorbin](https://github.com/Ordorbin)
