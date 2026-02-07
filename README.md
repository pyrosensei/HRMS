# HRMS Lite - Full Stack Assessment

A lightweight Human Resource Management System built with modern web technologies. This project demonstrates a complete full-stack application with a RESTful API backend and a responsive frontend interface.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109-green.svg)
![SQLite](https://img.shields.io/badge/SQLite-3-blue.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple.svg)

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| **Backend** | FastAPI (Python) |
| **Database** | SQLite with SQLAlchemy ORM |
| **Frontend** | HTML5, Bootstrap 5, Vanilla JavaScript |
| **API Server** | Uvicorn (ASGI) |

---

## 📁 Project Structure

```
HRMS_Lite/
├── main.py            # FastAPI application & API endpoints
├── database.py        # Database connection & session management
├── models.py          # SQLAlchemy ORM models
├── requirements.txt   # Python dependencies
├── hrms.db            # SQLite database (auto-generated)
└── static/
    └── index.html     # Frontend UI
```

---

## 🚀 Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone or navigate to the project directory:**
   ```bash
   cd HRMS_Lite
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the development server:**
   ```bash
   uvicorn main:app --reload
   ```

4. **Access the application:**
   - **Frontend UI:** http://127.0.0.1:8000/static/index.html
   - **API Documentation (Swagger):** http://127.0.0.1:8000/docs
   - **Alternative API Docs (ReDoc):** http://127.0.0.1:8000/redoc

---

## 🌐 Live Deployment

- **Live Application:** [Add URL after deployment]
- **API Documentation:** [Your-Render-URL]/docs
- **Backend API:** [Your-Render-URL]

---

## 📡 API Documentation

### Employee Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/employees/` | Create a new employee |
| `GET` | `/employees/` | Retrieve all employees |
| `DELETE` | `/employees/{id}` | Delete an employee by ID |

#### Employee Schema
```json
{
  "name": "string",
  "email": "string",
  "department": "string"
}
```

### Attendance Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/attendance/` | Mark attendance for an employee |
| `GET` | `/attendance/` | Retrieve all attendance records |

#### Attendance Schema
```json
{
  "employee_id": "integer",
  "date": "YYYY-MM-DD",
  "status": "Present | Absent"
}
```

---

## 🗄️ Database Schema

### Employee Table
| Column | Type | Constraints |
|--------|------|-------------|
| id | INTEGER | Primary Key, Auto-increment |
| name | VARCHAR(100) | Not Null |
| email | VARCHAR(100) | Unique, Not Null |
| department | VARCHAR(100) | Not Null |

### Attendance Table
| Column | Type | Constraints |
|--------|------|-------------|
| id | INTEGER | Primary Key, Auto-increment |
| employee_id | INTEGER | Foreign Key → Employee.id |
| date | DATE | Not Null |
| status | VARCHAR(10) | Not Null (Present/Absent) |

---

## ⚠️ Disclaimer

> **Note:** This project uses **SQLite** as the database for simplicity and ease of setup during this assessment. For production environments, it is recommended to use a more robust database solution such as **PostgreSQL** or **MySQL**.

---

## 📝 License

This project is created for assessment purposes.

---

## 👤 Author

Created as part of a Full Stack Development Assessment.
