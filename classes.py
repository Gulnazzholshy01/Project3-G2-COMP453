# Gulnaz Zholshy - ORM Classes for Location and Employee
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

#END OF GULNAZ'S CODE BLOCK


# Adriana Esparza - ORM Classes for MenuItem and OrderItem
# For classes.py
from typing import List
from sqlalchemy import create_engine, ForeignKey, String, Integer, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

# Connect to PostgreSQL
engine = create_engine("postgresql+psycopg2://postgres:Holaholahola@localhost/postgres")

# Base class
class Base(DeclarativeBase):
    pass

# Define MenuItem
class MenuItem(Base):
    __tablename__ = "menu_item"

    menu_item_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    description: Mapped[str] = mapped_column(String(255))
    price: Mapped[float] = mapped_column(Float, nullable=False)
    category: Mapped[str] = mapped_column(String(50), nullable=False)

    order_items: Mapped[List["OrderItem"]] = relationship("OrderItem", back_populates="menu_item")

    def __repr__(self) -> str:
        return f"MenuItem(id={self.menu_item_id}, name={self.name}, price={self.price})"

# Define OrderItem
class OrderItem(Base):
    __tablename__ = "order_item"

    order_item_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    order_number: Mapped[int] = mapped_column(Integer, nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    menu_item_id: Mapped[int] = mapped_column(ForeignKey("menu_item.menu_item_id"), nullable=False)

    menu_item: Mapped["MenuItem"] = relationship("MenuItem", back_populates="order_items")

    def __repr__(self) -> str:
        return f"OrderItem(id={self.order_item_id}, menu_item_id={self.menu_item_id}, quantity={self.quantity})"

# Create tables
Base.metadata.create_all(engine)

#END OF ADRIANA'S CODE BLOCK


###ORM Classes for Customer and FoodOrder - Pranati Sukh
from typing import List
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, DECIMAL, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

##Connecting to PostgreSQL
engine = create_engine("postgresql+psycopg2://postgres:sql4me@localhost:5432/Project3")

##Defining the Classes
class Base(DeclarativeBase):
    pass

#Class - Customer
class Customer(Base):
    __tablename__ = "customer"

    id: Mapped[str] = mapped_column("cID", String(20), primary_key=True)
    phone_number: Mapped[str] = mapped_column("cPhoneNumber", String(20), nullable=False)
    name: Mapped[str] = mapped_column("cName", String(100), nullable=False)

    orders: Mapped[List["FoodOrder"]] = relationship("FoodOrder", back_populates="customer")

    def __repr__(self) -> str:
        return f"Customer(id={self.id!r}, name={self.name!r}, phone={self.phone_number!r})"

#Class - FoodOrder
class FoodOrder(Base):
    __tablename__ = "foodOrder"

    number: Mapped[int] = mapped_column("oNumber", Integer, primary_key=True)
    total_amount: Mapped[DECIMAL] = mapped_column("oTotalAmount", DECIMAL(10, 2))
    time: Mapped[DateTime] = mapped_column("oTime", DateTime)
    status: Mapped[str] = mapped_column("oStatus", String(20))
    customer_id: Mapped[str] = mapped_column("cID", ForeignKey("customer.cID"))
    truck_id: Mapped[str] = mapped_column("tID", String(20))

    customer: Mapped["Customer"] = relationship("Customer", back_populates="orders")

    def __repr__(self) -> str:
        return (f"FoodOrder(number={self.number!r}, total_amount={self.total_amount!r}, "
                f"status={self.status!r}, time={self.time!r}, customer_id={self.customer_id!r}, "
                f"truck_id={self.truck_id!r})")

##Creating both the Tables 
Base.metadata.create_all(engine)

###End Code Block - Pranati Sukh
