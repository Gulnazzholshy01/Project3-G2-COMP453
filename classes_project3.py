from typing import List
from sqlalchemy import ForeignKey, String, Integer, Float, Time, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session
from sqlalchemy import select
from datetime import time


engine = create_engine("postgresql+psycopg2://postgres:22971609@localhost:5432/project3")

class Base(DeclarativeBase):
    pass

class FoodTruck(Base):
    __tablename__ = "FoodTruck"
    
    tID: Mapped[str] = mapped_column(String, primary_key=True)
    tStartTime: Mapped[str] = mapped_column(Time)
    tEndTime: Mapped[str] = mapped_column(Time)
    tRegistrationNumber: Mapped[str] = mapped_column(String(20))
    tLicencePlateNumber: Mapped[str] = mapped_column(String(20))
    lID: Mapped[str] = mapped_column(String(10)) 

    MenuItems: Mapped[List["MenuItem"]] = relationship("MenuItem", back_populates="food_truck", cascade="all, delete-orphan")
    
    def __repr__(self) -> str: 
        return f"FoodTruck(id={self.tID!r}, start={self.tStartTime}, end={self.tEndTime})"

class MenuItem(Base):
    __tablename__ = "MenuItem"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    menuItemName: Mapped[str] = mapped_column(String(50))
    menuItemDescription: Mapped[str] = mapped_column(String(255))
    menuItemPrice: Mapped[float] = mapped_column(Float)
    menuItemCategory: Mapped[str] = mapped_column(String(30))
    
    food_truck_id: Mapped[str] = mapped_column("food_truck_id", String, ForeignKey("FoodTruck.tID"))  
    food_truck: Mapped["FoodTruck"] = relationship("FoodTruck", back_populates="MenuItems")

    def __repr__(self) -> str:
        return f"MenuItem(name={self.menuItemName!r}, price={self.menuItemPrice}, category={self.menuItemCategory})"

#Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
 
from sqlalchemy.orm import Session
from datetime import time

with Session(engine) as session:
    food_truck_1 = FoodTruck(
        tID='FT001',
        tStartTime=time(8, 0),
        tEndTime=time(19, 0),
        tRegistrationNumber='REG123',
        tLicencePlateNumber='ABC123',
        lID='L001',
        MenuItems=[
            MenuItem(menuItemName='Cheese Burger', menuItemDescription='Delicious beef burger with cheese', menuItemPrice=8.99, menuItemCategory='Burgers'),
            MenuItem(menuItemName='Fries', menuItemDescription='Crispy golden fries', menuItemPrice=3.49, menuItemCategory='Sides'),
            MenuItem(menuItemName='Coke', menuItemDescription='Refreshing Coca-Cola', menuItemPrice=1.50, menuItemCategory='Beverages'),
        ]
    )
    food_truck_2 = FoodTruck(
        tID='FT002',
        tStartTime=time(9, 0),
        tEndTime=time(20, 0),
        tRegistrationNumber='REG124',
        tLicencePlateNumber='DEF124',
        lID='L002',
        MenuItems=[
            MenuItem(menuItemName='Onion Rings', menuItemDescription='Crispy battered onion rings', menuItemPrice=4.50, menuItemCategory='Sides'),
            MenuItem(menuItemName='Veggie Burger', menuItemDescription='Vegan burger with fresh vegetables', menuItemPrice=7.99, menuItemCategory='Burgers'),
            MenuItem(menuItemName='Chicken Nuggets', menuItemDescription='Crispy fried chicken nuggets', menuItemPrice=4.99, menuItemCategory='Sides'),
            MenuItem(menuItemName='Cheese Burger', menuItemDescription='Delicious beef burger with cheese', menuItemPrice=8.99, menuItemCategory='Burgers'),
        ]
    )
    food_truck_3 = FoodTruck(
        tID='FT003',
        tStartTime=time(7, 0),
        tEndTime=time(21, 0),
        tRegistrationNumber='REG125',
        tLicencePlateNumber='GHI125',
        lID='L003',
        MenuItems=[
            MenuItem(menuItemName='Lemonade', menuItemDescription='Freshly squeezed lemonade', menuItemPrice=2.00, menuItemCategory='Beverages'),
            MenuItem(menuItemName='Coke', menuItemDescription='Refreshing Coca-Cola', menuItemPrice=1.50, menuItemCategory='Beverages'),
            MenuItem(menuItemName='Veggie Burger', menuItemDescription='Vegan burger with fresh vegetables', menuItemPrice=7.99, menuItemCategory='Burgers'),
            MenuItem(menuItemName='Cheese Burger', menuItemDescription='Delicious beef burger with cheese', menuItemPrice=8.99, menuItemCategory='Burgers'),
        ]
    )
    food_truck_4 = FoodTruck(
        tID='FT004',
        tStartTime=time(10, 0),
        tEndTime=time(21, 0),
        tRegistrationNumber='REG126',
        tLicencePlateNumber='JKL126',
        lID='L004',
        MenuItems=[
            MenuItem(menuItemName='Hot Dog', menuItemDescription='Classic hot dog with mustard', menuItemPrice=5.00, menuItemCategory='Hot Dogs'),
            MenuItem(menuItemName='Coke', menuItemDescription='Refreshing Coca-Cola', menuItemPrice=1.50, menuItemCategory='Beverages'),
            MenuItem(menuItemName='Lemonade', menuItemDescription='Freshly squeezed lemonade', menuItemPrice=2.00, menuItemCategory='Beverages'),
        ]
    )    
    food_truck_5 = FoodTruck(
        tID='FT005',
        tStartTime=time(8, 30),
        tEndTime=time(16, 30),
        tRegistrationNumber='REG127',
        tLicencePlateNumber='MNO127',
        lID='L005',
        MenuItems=[
            MenuItem(menuItemName='Chicken Wrap', menuItemDescription='Grilled chicken in a wrap with sauce', menuItemPrice=6.50, menuItemCategory='Wraps'),
            MenuItem(menuItemName='Caesar Salad', menuItemDescription='Crisp romaine lettuce with Caesar dressing', menuItemPrice=5.50, menuItemCategory='Salads'),
            MenuItem(menuItemName='Coke', menuItemDescription='Refreshing Coca-Cola', menuItemPrice=1.50, menuItemCategory='Beverages'),
        ]
    )    
    food_truck_6 = FoodTruck(
        tID='FT006',
        tStartTime=time(11, 0),
        tEndTime=time(22, 0),
        tRegistrationNumber='REG128',
        tLicencePlateNumber='PQR128',
        lID='L006',
        MenuItems=[
            MenuItem(menuItemName='Tacos', menuItemDescription='Soft shell tacos with beef or chicken', menuItemPrice=6.75, menuItemCategory='Mexican'),
            MenuItem(menuItemName='Lemonade', menuItemDescription='Freshly squeezed lemonade', menuItemPrice=2.00, menuItemCategory='Beverages'),

        ]
    )    
    food_truck_7 = FoodTruck(
        tID='FT007',
        tStartTime=time(6, 0),
        tEndTime=time(15, 0),
        tRegistrationNumber='REG129',
        tLicencePlateNumber='STU129',
        lID='L007',
        MenuItems=[
            MenuItem(menuItemName='Pulled Pork Sandwich', menuItemDescription='Tender pulled pork in a sandwich', menuItemPrice=7.50, menuItemCategory='Sandwiches'),
            MenuItem(menuItemName='Fries', menuItemDescription='Crispy golden fries', menuItemPrice=3.49, menuItemCategory='Sides'),
            MenuItem(menuItemName='Chicken Nuggets', menuItemDescription='Crispy fried chicken nuggets', menuItemPrice=4.99, menuItemCategory='Sides'),
        ]
    )    
    food_truck_8 = FoodTruck(
        tID='FT008',
        tStartTime=time(7, 30),
        tEndTime=time(15, 30),
        tRegistrationNumber='REG130',
        tLicencePlateNumber='VWX130',
        lID='L008',
        MenuItems=[
            MenuItem(menuItemName='Fish and Chips', menuItemDescription='Crispy fish fillets with fries', menuItemPrice=8.25, menuItemCategory='Seafood'),
            MenuItem(menuItemName='Coke', menuItemDescription='Refreshing Coca-Cola', menuItemPrice=1.50, menuItemCategory='Beverages'),
        ]
    )    
    food_truck_9 = FoodTruck(
        tID='FT009',
        tStartTime=time(9, 0),
        tEndTime=time(19, 0),
        tRegistrationNumber='REG131',
        tLicencePlateNumber='YZ1234',
        lID='L001',
        MenuItems=[
            MenuItem(menuItemName='Pizza Slice', menuItemDescription='Pepperoni pizza slice', menuItemPrice=4.00, menuItemCategory='Pizza'),
        ]
    )
    food_truck_10 = FoodTruck(
        tID='FT010',
        tStartTime=time(8, 0),
        tEndTime=time(20, 0),
        tRegistrationNumber='REG132',
        tLicencePlateNumber='ABC567',
        lID='L008',
        MenuItems=[
            MenuItem(menuItemName='Ice Cream', menuItemDescription='Vanilla, chocolate, or strawberry', menuItemPrice=3.00, menuItemCategory='Desserts'),
            MenuItem(menuItemName='Chicken Nuggets', menuItemDescription='Crispy fried chicken nuggets', menuItemPrice=4.99, menuItemCategory='Sides'),
        ]
    )
    
    session.add_all([food_truck_1, food_truck_2, food_truck_3, food_truck_4, 
                         food_truck_5, food_truck_6, food_truck_7, food_truck_8, 
                         food_truck_9, food_truck_10])
    session.commit()

# Simple Queries
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
#from classes_project3 import engine, FoodTruck, MenuItem
from sqlalchemy.orm import Session
from sqlalchemy import select

print("")
print("Q2: Food Trucks and the Menu Items sold - Student: Angelina Carcione")
print("This query will output the truck, the location, what category of food it is, how many items fall into the category (must be > 1), and the average price of that type of item.")
print("")

with Session(engine) as session:
    result = (
        session.query(
            FoodTruck.tID,
            FoodTruck.lID,
            MenuItem.menuItemCategory,
            func.count(MenuItem.id).label("numItems"),
            func.avg(MenuItem.menuItemPrice).label("avgPrice")
        )
        .select_from(FoodTruck)
        .join(MenuItem)
        .group_by(FoodTruck.tID, FoodTruck.lID, MenuItem.menuItemCategory) 
        .having(func.count(MenuItem.id) > 1) # count of the AMOUNT of items that fall into that category but only if they have more than 1 of that type
        .order_by(FoodTruck.tID) # the item has to come from the same food truck 
        .all()
    )

    for row in result:
        print(f"Truck ID     : {row.tID}")
        print(f"Location ID  : {row.lID}")
        print(f"Category     : {row.menuItemCategory}")
        print(f"Items Count  : {row.numItems}")
        print(f"Avg Price    : ${row.avgPrice:.2f}\n")  


