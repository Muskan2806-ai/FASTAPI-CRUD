
from sqlalchemy import Column, Integer, String, Date
from app.database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    student_name = Column(String)
    student_class = Column(String)
    student_section = Column(String)
    student_dob = Column(Date)

