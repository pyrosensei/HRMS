<div align="center">

# 🚀 HRMS Lite - Modern Human Resource Management System

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109+-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![SQLite](https://img.shields.io/badge/SQLite-3-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![Render](https://img.shields.io/badge/Deployed_on-Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)](https://render.com/)

**A lightweight, high-performance Human Resource Management System built with cutting-edge web technologies**

[🌐 Live Demo](https://hrms-0zg8.onrender.com/static/index.html) • [📚 API Docs](https://hrms-0zg8.onrender.com/docs) • [📖 ReDoc](https://hrms-0zg8.onrender.com/redoc)

</div>

---

## ✨ Key Features

<table>
<tr>
<td width="33%" align="center">

### 👥 Employee Management
Complete CRUD operations for employee records with email validation and duplicate prevention

</td>
<td width="33%" align="center">

### 📊 Smart Attendance Tracking
Efficient attendance management system with date-based tracking and status monitoring

</td>
<td width="33%" align="center">

### ⚡ High-Performance Architecture
Built on FastAPI with async support, SQLAlchemy ORM, and optimized database queries

</td>
</tr>
</table>

---

## 🛠️ Tech Stack

<div align="center">

| **Layer** | **Technology** | **Purpose** |
|-----------|----------------|-------------|
| **Backend Framework** | FastAPI | High-performance async web framework |
| **Database** | SQLite | Lightweight relational database |
| **ORM** | SQLAlchemy 2.0+ | Database modeling and queries |
| **Frontend** | Bootstrap 5.3 | Responsive UI framework |
| **Deployment** | Render | Cloud hosting platform |
| **ASGI Server** | Uvicorn | Lightning-fast ASGI server |

</div>

---

## 🌐 Live Deployment

<div align="center">

### 🎯 **Application URL**
**[https://hrms-0zg8.onrender.com/static/index.html](https://hrms-0zg8.onrender.com/static/index.html)**

### 📚 **API Documentation**
- **Interactive Swagger UI:** [/docs](https://hrms-0zg8.onrender.com/docs)
- **ReDoc Interface:** [/redoc](https://hrms-0zg8.onrender.com/redoc)

</div>

---

## 📡 API Snapshot

<div align="center">

### Employee Management

| **Method** | **Endpoint** | **Description** | **Request Body** | **Response Body** |
|:----------:|--------------|-----------------|------------------|-------------------|
| `POST` | `/employees/` | Create new employee | `{ "name": "string", "email": "string", "department": "string" }` | `{ "id": int, "name": "string", "email": "string", "department": "string" }` |
| `GET` | `/employees/` | List all employees | None | `[{ "id": int, "name": "string", "email": "string", "department": "string" }, ...]` |
| `DELETE` | `/employees/{id}` | Delete employee | None | `{ "message": "string" }` |

### Attendance Tracking

| **Method** | **Endpoint** | **Description** | **Request Body** | **Response Body** |
|:----------:|--------------|-----------------|------------------|-------------------|
| `POST` | `/attendance/` | Mark attendance | `{ "employee_id": int, "date": "YYYY-MM-DD", "status": "Present/Absent" }` | `{ "id": int, "employee_id": int, "date": "YYYY-MM-DD", "status": "string" }` |
| `GET` | `/attendance/` | View all records | None | `[{ "id": int, "employee_id": int, "date": "YYYY-MM-DD", "status": "string" }, ...]` |

</div>

---

## 🚀 Local Development Setup

### Prerequisites
```bash
✅ Python 3.8 or higher
✅ pip (Python package manager)
```

### Installation Steps

1️⃣ **Clone the repository**
```bash
git clone https://github.com/pyrosensei/HRMS.git
cd HRMS
```

2️⃣ **Install dependencies**
```bash
pip install -r requirements.txt
```

3️⃣ **Run the development server**
```bash
uvicorn main:app --reload
```

4️⃣ **Access the application**
- 🎨 **Frontend UI:** http://127.0.0.1:8000/static/index.html
- 📚 **API Documentation (Swagger):** http://127.0.0.1:8000/docs
- 📖 **Alternative API Docs (ReDoc):** http://127.0.0.1:8000/redoc

---

## 📁 Project Structure

```
HRMS/
├── 📄 main.py              # FastAPI application & REST API endpoints
├── 🗄️ database.py          # Database connection & session management
├── 📋 models.py            # SQLAlchemy ORM models (Employee, Attendance)
├── 📦 requirements.txt     # Python dependencies
├── 🔧 render.yaml          # Render deployment configuration
├── 🗃️ hrms.db              # SQLite database (auto-generated)
├── 🧪 test_add_employee.py # Employee creation tests
├── ✅ verify_server.py     # Server verification script
└── 📂 static/
    └── 🎨 index.html       # Responsive Bootstrap frontend
```

---

## 🗄️ Database Schema

<div align="center">

### Employee Table
| Column | Type | Constraints |
|--------|------|-------------|
| `id` | INTEGER | PRIMARY KEY, AUTO INCREMENT |
| `name` | VARCHAR(100) | NOT NULL |
| `email` | VARCHAR(100) | UNIQUE, NOT NULL |
| `department` | VARCHAR(100) | NOT NULL |

### Attendance Table
| Column | Type | Constraints |
|--------|------|-------------|
| `id` | INTEGER | PRIMARY KEY, AUTO INCREMENT |
| `employee_id` | INTEGER | FOREIGN KEY → employees.id |
| `date` | DATE | NOT NULL |
| `status` | VARCHAR(10) | NOT NULL (Present/Absent) |

</div>

---

## 🎯 API Features

- ✅ **RESTful Design** - Clean, intuitive API endpoints
- ✅ **Data Validation** - Pydantic schemas ensure data integrity
- ✅ **Error Handling** - Comprehensive HTTP exception handling
- ✅ **CORS Enabled** - Cross-Origin Resource Sharing configured
- ✅ **Auto Documentation** - Interactive Swagger UI & ReDoc
- ✅ **ORM Relationships** - Cascade delete for data consistency

---

## 💡 Technical Highlights

- 🚀 **Async/Await Support** - Asynchronous request handling for better performance
- 🔒 **Email Validation** - Prevents duplicate employee records
- 🔗 **Foreign Key Constraints** - Maintains referential integrity
- 📱 **Responsive Design** - Mobile-friendly Bootstrap interface
- ⚡ **Fast Startup** - SQLite for quick development cycles
- 🎨 **Static File Serving** - Integrated frontend with FastAPI

---

## ⚠️ Production Notes

> **Database:** This project uses **SQLite** for simplicity and rapid development. For production environments, consider migrating to **PostgreSQL** or **MySQL** for better scalability and concurrent access handling.

---

## 📝 License

This project is created for educational and assessment purposes.

---

## 👨‍💻 Credits

<div align="center">

**Developed by [pyrosensei](https://github.com/pyrosensei)**

⭐ **Star this repo if you find it helpful!** ⭐

</div>

---

<div align="center">

**Built with ❤️ using FastAPI and Modern Web Technologies**

</div>
