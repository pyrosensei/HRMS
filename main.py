from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr
from datetime import date
from typing import List, Optional
from pathlib import Path

from database import engine, get_db, Base
from models import Employee, Attendance

# Create all database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="HRMS Lite",
    description="A lightweight Human Resource Management System",
    version="1.0.0"
)

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Setup path for static files
BASE_DIR = Path(__file__).resolve().parent
static_path = BASE_DIR / "static"

# Mount static files for frontend
app.mount("/static", StaticFiles(directory=str(static_path)), name="static")


# ==================== Pydantic Schemas ====================

class EmployeeCreate(BaseModel):
    name: str
    email: str
    department: str


class EmployeeResponse(BaseModel):
    id: int
    name: str
    email: str
    department: str

    class Config:
        orm_mode = True
        from_attributes = True  # For v2 compatibility


class AttendanceCreate(BaseModel):
    employee_id: int
    date: date
    status: str  # 'Present' or 'Absent'


class AttendanceResponse(BaseModel):
    id: int
    employee_id: int
    date: date
    status: str

    class Config:
        orm_mode = True
        from_attributes = True  # For v2 compatibility


# ==================== Employee Endpoints ====================

@app.post("/employees/", response_model=EmployeeResponse)
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    """Add a new employee"""
    # Check if email already exists
    existing = db.query(Employee).filter(Employee.email == employee.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    db_employee = Employee(
        name=employee.name,
        email=employee.email,
        department=employee.department
    )
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee


@app.get("/employees/", response_model=List[EmployeeResponse])
def list_employees(db: Session = Depends(get_db)):
    """List all employees"""
    employees = db.query(Employee).all()
    return employees


@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    """Remove an employee by ID"""
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    db.delete(employee)
    db.commit()
    return {"message": f"Employee {employee_id} deleted successfully"}


# ==================== Attendance Endpoints ====================

@app.post("/attendance/", response_model=AttendanceResponse)
def mark_attendance(attendance: AttendanceCreate, db: Session = Depends(get_db)):
    """Mark attendance for an employee"""
    # Validate status
    if attendance.status not in ["Present", "Absent"]:
        raise HTTPException(status_code=400, detail="Status must be 'Present' or 'Absent'")
    
    # Check if employee exists
    employee = db.query(Employee).filter(Employee.id == attendance.employee_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    db_attendance = Attendance(
        employee_id=attendance.employee_id,
        date=attendance.date,
        status=attendance.status
    )
    db.add(db_attendance)
    db.commit()
    db.refresh(db_attendance)
    return db_attendance


@app.get("/attendance/", response_model=List[AttendanceResponse])
def list_attendance(db: Session = Depends(get_db)):
    """View all attendance records"""
    records = db.query(Attendance).all()
    return records


# ==================== Root Endpoint ====================

@app.get("/")
def read_root():
    """Root endpoint - Serves the frontend"""
    return FileResponse(BASE_DIR / 'static/index.html')


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
