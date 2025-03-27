from typing import List
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, DECIMAL
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session
from sqlalchemy import select

engine = create_engine('postgresql+psycopg2://postgres:gulmpaag@localhost:5432/project3')

#Define Classes/Tables
class Base(DeclarativeBase):
    pass

class Location(Base):
    __tablename__ = "locations" 
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    location_address: Mapped[str] = mapped_column(String(60))
    employees: Mapped[List["Employee"]] = relationship("Employee", back_populates="location")

    def __repr__(self) -> str:
        return f"Location(id={self.id!r}, location_address={self.location_address!r})"
    

class Employee(Base):
    __tablename__ = "employees"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    role: Mapped[str] = mapped_column(String(30))
    salary: Mapped[DECIMAL] = Column(DECIMAL(10, 2))
    address: Mapped[str] = mapped_column(String(60))
    phone_number: Mapped[str] = mapped_column(String(20))
    location_id: Mapped[int]= mapped_column(ForeignKey("locations.id"))

    location: Mapped["Location"] = relationship("Location", back_populates="employees")

    def __repr__(self) -> str: 
        return (f"Employee(id={self.id!r}, " 
                f"eFirstName={self.first_name!r}, "
                f"eLastName={self.last_name!r}, "
                f"eRole={self.role}, "
                f"eSalary={self.salary}, "
                f"eAddress={self.address}, "
                f"ePhoneNumber={self.phone_number})")

#Create Tables
Base.metadata.create_all(engine)



