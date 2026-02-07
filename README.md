<div align="center">

# 🚀 HRMS Lite - Modern HR Management System

### *Streamline Your Workforce Management with Cutting-Edge Technology*

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109+-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![SQLite](https://img.shields.io/badge/SQLite-3-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![Deployed on Render](https://img.shields.io/badge/Deployed%20on-Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)](https://render.com/)

---

### ✨ A lightweight, high-performance Human Resource Management System built with modern web technologies

</div>

---

## 🌟 Key Features

<table>
  <tr>
    <td width="33%" align="center">
      <h3>👥 Employee Management</h3>
      <p>Effortlessly manage employee records with full CRUD operations. Add, view, and delete employee information with a clean and intuitive interface.</p>
    </td>
    <td width="33%" align="center">
      <h3>📊 Smart Attendance Tracking</h3>
      <p>Track employee attendance with date-based records. Mark Present/Absent status and maintain comprehensive attendance history.</p>
    </td>
    <td width="33%" align="center">
      <h3>⚡ High-Performance Architecture</h3>
      <p>Built on FastAPI and SQLAlchemy ORM for lightning-fast API responses and efficient database operations.</p>
    </td>
  </tr>
</table>

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|-------|------------|---------|
| **Backend Framework** | FastAPI | High-performance Python web framework with automatic API documentation |
| **Database** | SQLite | Lightweight, serverless SQL database with SQLAlchemy ORM |
| **Frontend** | Bootstrap 5 | Modern, responsive UI components with vanilla JavaScript |
| **Deployment** | Render | Cloud platform for seamless deployment and hosting |

---

## 🌐 Live Deployment

🎯 **Access the Live Application:**
- **Frontend UI:** [https://hrms-0zg8.onrender.com/static/index.html](https://hrms-0zg8.onrender.com/static/index.html)
- **Interactive API Docs:** [https://hrms-0zg8.onrender.com/docs](https://hrms-0zg8.onrender.com/docs)
- **Alternative API Docs:** [https://hrms-0zg8.onrender.com/redoc](https://hrms-0zg8.onrender.com/redoc)

---

## 📡 API Snapshot

### Employee Endpoints

| Method | Endpoint | Description | Request Body |
|--------|----------|-------------|--------------|
| `POST` | `/employees/` | Create a new employee | `{ "name": "string", "email": "string", "department": "string" }` |
| `GET` | `/employees/` | Retrieve all employees | - |
| `DELETE` | `/employees/{id}` | Delete an employee by ID | - |

### Attendance Endpoints

| Method | Endpoint | Description | Request Body |
|--------|----------|-------------|--------------|
| `POST` | `/attendance/` | Mark attendance for an employee | `{ "employee_id": int, "date": "YYYY-MM-DD", "status": "Present\|Absent" }` |
| `GET` | `/attendance/` | Retrieve all attendance records | - |

---

## 💻 Local Development Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/pyrosensei/HRMS.git
   cd HRMS
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the development server:**
   ```bash
   uvicorn main:app --reload
   ```

4. **Access the application locally:**
   - **Frontend UI:** http://127.0.0.1:8000/static/index.html
   - **API Documentation (Swagger):** http://127.0.0.1:8000/docs
   - **Alternative API Docs (ReDoc):** http://127.0.0.1:8000/redoc

---

## 📁 Project Structure

```
HRMS/
├── 📄 main.py              # FastAPI application & RESTful API endpoints
├── 🗄️ database.py          # Database connection & session management
├── 📋 models.py            # SQLAlchemy ORM models (Employee & Attendance)
├── 📦 requirements.txt     # Python dependencies
├── 🔧 render.yaml          # Render deployment configuration
├── 🗃️ hrms.db              # SQLite database (auto-generated)
├── 🧪 test_add_employee.py # Test suite for employee operations
├── ✅ verify_server.py     # Server verification script
└── 📂 static/
    └── 🌐 index.html       # Responsive frontend UI
```

---

## 🗄️ Database Schema

### Employee Table
| Column | Type | Constraints |
|--------|------|-------------|
| `id` | INTEGER | Primary Key, Auto-increment |
| `name` | VARCHAR(100) | Not Null |
| `email` | VARCHAR(100) | Unique, Not Null |
| `department` | VARCHAR(100) | Not Null |

### Attendance Table
| Column | Type | Constraints |
|--------|------|-------------|
| `id` | INTEGER | Primary Key, Auto-increment |
| `employee_id` | INTEGER | Foreign Key → Employee.id |
| `date` | DATE | Not Null |
| `status` | VARCHAR(10) | Not Null (Present/Absent) |

---

## 🎯 Features Highlights

- ✅ **RESTful API** - Clean and well-documented API endpoints
- ✅ **Automatic API Documentation** - Interactive Swagger UI and ReDoc
- ✅ **CORS Enabled** - Ready for frontend integration
- ✅ **Input Validation** - Pydantic schemas for data validation
- ✅ **Responsive Design** - Mobile-friendly Bootstrap 5 UI
- ✅ **Production Ready** - Deployed on Render with Gunicorn

---

## 📝 License

This project is created for demonstration and educational purposes.

---

<div align="center">

## 👨‍💻 Credits

**Developed by [pyrosensei](https://github.com/pyrosensei)**

*Built with ❤️ using FastAPI, SQLite, and Bootstrap*

---

### ⭐ If you find this project useful, please consider giving it a star!

</div>
