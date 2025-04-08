# Gulnaz Zholshy - Query
from classes import engine, Location, Employee
from sqlalchemy.orm import  Session, sessionmaker
from sqlalchemy import select,  func

print("")
print("Q1. avgSalPerRoleInLoc - Student: Gulnaz Zholshy")
print("")
Session = sessionmaker(bind=engine)

with Session() as session:
    locations =(
        session.query(
            Location.id, 
            Location.location_address, 
            Employee.role,
            func.count(Employee.id).label("empNumPerRole"),
            func.round(func.avg(Employee.salary), 2).label("avgSalPerRole")
        )
        .join(Location)
        .group_by(Location.id, Location.location_address, Employee.role)
        .having(func.count(Employee.id) > 1)
        .order_by(Location.id)
        .all()
    )

for location_id, location_address, role, count, avg in locations:
    print(f"lID: {location_id}, lAddress: {location_address}, eRole: {role}, empNumPerRole: {count}, avgSalPerRole: {avg}")



# Adriana Esparza - ORM Classes for MenuItem and OrderItem
# For queries.py
from classes import engine, MenuItem, OrderItem
from sqlalchemy.orm import Session
from sqlalchemy import func

print("")
print("Q4b.topOrderedMenuItemsByQuantity – Student: Adriana Esparza")
print("")

with Session(engine) as session:
    results = (
        session.query(
            MenuItem.name,
            func.sum(OrderItem.quantity).label("total_quantity")
        )
        .join(OrderItem)
        .group_by(MenuItem.name)
        .order_by(func.sum(OrderItem.quantity).desc())
        .limit(10)
        .all()
    )

    print("Top Ordered Menu Items:")
    for name, quantity in results:
        print(f"{name}: {quantity} orders")

#END OF ADRIANA'S CODE BLOCK


###Query 3: topSpendingCustomersOver$35 - Pranati Sukh
##Using Customer and FoodOrder 
from ClassesPython import engine, Customer, FoodOrder
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import func

print("")
print("Q3. Customers with Order Total Over $35 and the Total Revenue from Them")
print("")

##Open a Session to Connect to the Database
Session = sessionmaker(bind=engine)

with Session() as session:
    #Query to Retrieve Customer Names, Orders, and Total Spent 
    customer_orders = (
        session.query(
            Customer.name,
            func.count(FoodOrder.number).label("orderCount"),  #Counts the Number of Orders Per Person
            func.round(func.sum(FoodOrder.total_amount), 2).label("totalSpent")
        )
        .join(FoodOrder, FoodOrder.customer_id == Customer.id)
        .filter(FoodOrder.total_amount > 35)  #Filtering to Only Retrieve Orders Over $35
        .group_by(Customer.name)    #Grouping the Results by Customer
        .order_by(func.sum(FoodOrder.total_amount).desc())
        .limit(10)   #Limiting the Data Retrieved by 10
        .all()
    )

##Return From Above Query 
if customer_orders:
    #Print Each Customer Result and Print Their Name and Total Spent
    for name, order_count, total_spent in customer_orders:
        print(f"Name: {name}, Total Spent: ${total_spent}")
    
    #Calculating the Total Revenue of the Customers Returned 
    total_revenue = sum(customer[2] for customer in customer_orders)
    print(f"Total Revenue from These Customers: ${total_revenue}")
else:
    #If No Customers Match the Resutls, Return This Message 
    print("No customers with orders over $35.")

###End Code Block - Pranati Sukh
