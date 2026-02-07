from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Employee(Base):
    """Employee table - stores employee information"""
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False, index=True)
    department = Column(String(100), nullable=False)

    # Relationship with Attendance
    attendances = relationship("Attendance", back_populates="employee", cascade="all, delete-orphan")


class Attendance(Base):
    """Attendance table - stores attendance records"""
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"), nullable=False)
    date = Column(Date, nullable=False)
    status = Column(String(10), nullable=False)  # 'Present' or 'Absent'

    # Relationship with Employee
    employee = relationship("Employee", back_populates="attendances")
