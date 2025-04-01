
from typing import List
from classes import engine, Location, Employee
from sqlalchemy.orm import  Session

#Insert data
with Session(engine) as session:
    l1 = Location(location_address = '123 Main St, Springfield, IL')
    l2 = Location(location_address = '456 Oak St, Riverton, IL')
    l3 = Location(location_address = '789 Maple St, Lincoln, IL')
    l4 = Location(location_address = '101 Pine St, Pleasantville, IL')
    l5 = Location(location_address = '202 Cedar St, Oakdale, IL')
    l6 = Location(location_address = '303 Birch St, Fairview, IL')
    l7 = Location(location_address = '404 Elm St, Greenfield, IL')
    l8 = Location(location_address = '505 Willow St, Brookville, IL')
    session.add_all([l1,l2,l3,l4,l5,l6,l7,l8])
    session.commit()

employees_data = [
    {"first_name": "John", "last_name": "Doe", "role": "Chef", "salary": 40300.00, "address": "123 Main St, Springfield, IL", "phone_number": "312-123-4567", "location_id": 1},
    {"first_name": "Jane", "last_name": "Smith", "role": "Server", "salary": 28500.00, "address": "456 Oak St, Riverton, IL", "phone_number": "213-234-5678", "location_id": 2},
    {"first_name": "Mike", "last_name": "Johnson", "role": "Manager", "salary": 45600.00, "address": "789 Maple St, Lincoln, IL", "phone_number": "917-345-6789", "location_id": 3},
    {"first_name": "Emily", "last_name": "Davis", "role": "Chef", "salary": 37120.00, "address": "101 Pine St, Pleasantville, IL", "phone_number": "305-456-7890", "location_id": 4},
    {"first_name": "Chris", "last_name": "Brown", "role": "Server", "salary": 29200.00, "address": "202 Cedar St, Oakdale, IL", "phone_number": "408-567-8901", "location_id": 5},
    {"first_name": "Laura", "last_name": "Wilson", "role": "Manager", "salary": 48550.00, "address": "303 Birch St, Fairview, IL", "phone_number": "818-678-9012", "location_id": 6},
    {"first_name": "David", "last_name": "Moore", "role": "Chef", "salary": 36440.00, "address": "404 Elm St, Greenfield, IL", "phone_number": "720-789-0123", "location_id": 7},
    {"first_name": "Olivia", "last_name": "Taylor", "role": "Server", "salary": 30440.00, "address": "505 Willow St, Brookville, IL", "phone_number": "415-890-1234", "location_id": 8},
    {"first_name": "Lucas", "last_name": "Anderson", "role": "Server", "salary": 28230.00, "address": "123 Main St, Springfield, IL", "phone_number": "202-901-2345", "location_id": 1},
    {"first_name": "Mia", "last_name": "Martinez", "role": "Chef", "salary": 35230.00, "address": "456 Oak St, Riverton, IL", "phone_number": "213-012-3456", "location_id": 2},
    {"first_name": "Ethan", "last_name": "Garcia", "role": "Manager", "salary": 45450.00, "address": "789 Maple St, Lincoln, IL", "phone_number": "347-123-4567", "location_id": 3},
    {"first_name": "Sophia", "last_name": "Harris", "role": "Server", "salary": 31430.00, "address": "101 Pine St, Pleasantville, IL", "phone_number": "312-234-5678", "location_id": 4},
    {"first_name": "Jack", "last_name": "Miller", "role": "Chef", "salary": 36430.00, "address": "202 Cedar St, Oakdale, IL", "phone_number": "503-345-6789", "location_id": 5},
    {"first_name": "Ava", "last_name": "Young", "role": "Manager", "salary": 49120.00, "address": "303 Birch St, Fairview, IL", "phone_number": "312-456-7890", "location_id": 6},
    {"first_name": "Mason", "last_name": "Scott", "role": "Server", "salary": 32000.00, "address": "404 Elm St, Greenfield, IL", "phone_number": "614-567-8901", "location_id": 7},
    {"first_name": "Isabella", "last_name": "King", "role": "Chef", "salary": 35500.00, "address": "505 Willow St, Brookville, IL", "phone_number": "707-678-9012", "location_id": 8},
    {"first_name": "Benjamin", "last_name": "Wright", "role": "Manager", "salary": 47000.00, "address": "123 Main St, Springfield, IL", "phone_number": "303-789-0123", "location_id": 1},
    {"first_name": "Charlotte", "last_name": "Lopez", "role": "Server", "salary": 33000.00, "address": "456 Oak St, Riverton, IL", "phone_number": "202-890-1234", "location_id": 2},
    {"first_name": "James", "last_name": "Gonzalez", "role": "Chef", "salary": 38000.00, "address": "789 Maple St, Lincoln, IL", "phone_number": "424-901-2345", "location_id": 3},
    {"first_name": "Amelia", "last_name": "Adams", "role": "Manager", "salary": 46000.00, "address": "101 Pine St, Pleasantville, IL", "phone_number": "503-012-3456", "location_id": 4},
    {"first_name": "William", "last_name": "Nelson", "role": "Server", "salary": 34000.00, "address": "202 Cedar St, Oakdale, IL", "phone_number": "305-123-4567", "location_id": 5},
    {"first_name": "Harper", "last_name": "Carter", "role": "Chef", "salary": 37500.00, "address": "303 Birch St, Fairview, IL", "phone_number": "847-234-5678", "location_id": 6},
    {"first_name": "Elijah", "last_name": "Mitchell", "role": "Manager", "salary": 48800.00, "address": "404 Elm St, Greenfield, IL", "phone_number": "619-345-6789", "location_id": 7},
    {"first_name": "Ella", "last_name": "Perez", "role": "Server", "salary": 35800.00, "address": "505 Willow St, Brookville, IL", "phone_number": "734-456-7890", "location_id": 8},
    {"first_name": "Logan", "last_name": "Roberts", "role": "Chef", "salary": 36800.00, "address": "123 Main St, Springfield, IL", "phone_number": "505-567-8901", "location_id": 1},
    {"first_name": "Zoe", "last_name": "Walker", "role": "Manager", "salary": 49700.00, "address": "456 Oak St, Riverton, IL", "phone_number": "415-678-9012", "location_id": 2},
    {"first_name": "Jackson", "last_name": "Hall", "role": "Server", "salary": 33700.00, "address": "789 Maple St, Lincoln, IL", "phone_number": "718-789-0123", "location_id": 3},
    {"first_name": "Lily", "last_name": "Allen", "role": "Chef", "salary": 35700.00, "address": "101 Pine St, Pleasantville, IL", "phone_number": "206-890-1234", "location_id": 4},
    {"first_name": "Alexander", "last_name": "Sanchez", "role": "Manager", "salary": 46000.00, "address": "202 Cedar St, Oakdale, IL", "phone_number": "412-901-2345", "location_id": 5},
    {"first_name": "Amos", "last_name": "Gomez", "role": "Server", "salary": 32500.00, "address": "303 Birch St, Fairview, IL", "phone_number": "314-012-3456", "location_id": 6},
    {"first_name": "Amina", "last_name": "Muhammad", "role": "Server", "salary": 31400.00, "address": "303 Birch St, Fairview, IL", "phone_number": "314-012-3456", "location_id": 6},
    {"first_name": "Lisa", "last_name": "Hamdan", "role": "Server", "salary": 34400.00, "address": "202 Cedar St, Oakdale, IL", "phone_number": "305-123-4567", "location_id": 5},
    {"first_name": "Jojo", "last_name": "Moyez", "role": "Server", "salary": 32300.00, "address": "456 Oak St, Riverton, IL", "phone_number": "202-890-1234", "location_id": 2}
    ]

employees = [
    Employee(
        first_name=employee_data["first_name"],
        last_name=employee_data["last_name"],
        role=employee_data["role"],
        salary=employee_data["salary"],
        address=employee_data["address"],
        phone_number=employee_data["phone_number"],
        location_id=employee_data["location_id"]
    )
    for employee_data in employees_data
]

with Session(engine) as session:
    session.add_all(employees)
    session.commit()

# Adriana Esparza - ORM Classes for MenuItem and OrderItem
# For objects.py
from classes import engine, MenuItem, OrderItem
from sqlalchemy.orm import Session

# Sample Menu Items
menu_items = [
    MenuItem(menu_item_id=1, name='Cheese Burger', description='Beef burger with cheese', price=8.99, category='Burgers'),
    MenuItem(menu_item_id=2, name='Veggie Burger', description='Vegan burger with vegetables', price=7.99, category='Burgers'),
    MenuItem(menu_item_id=3, name='Fries', description='Crispy fries', price=3.49, category='Sides'),
    MenuItem(menu_item_id=4, name='Hot Dog', description='Classic hot dog with mustard', price=5.00, category='Hot Dogs'),
    MenuItem(menu_item_id=5, name='Tacos', description='Beef or chicken tacos', price=6.75, category='Mexican'),
    MenuItem(menu_item_id=6, name='Lemonade', description='Fresh lemonade', price=2.00, category='Beverages'),
    MenuItem(menu_item_id=7, name='Pizza Slice', description='Pepperoni pizza slice', price=4.00, category='Pizza'),
    MenuItem(menu_item_id=8, name='Chicken Wrap', description='Grilled chicken wrap', price=6.50, category='Wraps'),
    MenuItem(menu_item_id=9, name='Caesar Salad', description='Lettuce with Caesar dressing', price=5.50, category='Salads'),
    MenuItem(menu_item_id=10, name='Ice Cream', description='Vanilla or chocolate', price=3.00, category='Desserts'),
]

# Sample Order Items
order_items = [
    OrderItem(order_item_id=1, order_number=1001, quantity=1, menu_item_id=1),
    OrderItem(order_item_id=2, order_number=1001, quantity=1, menu_item_id=3),
    OrderItem(order_item_id=3, order_number=1002, quantity=2, menu_item_id=2),
    OrderItem(order_item_id=4, order_number=1003, quantity=1, menu_item_id=1),
    OrderItem(order_item_id=5, order_number=1004, quantity=3, menu_item_id=3),
    OrderItem(order_item_id=6, order_number=1005, quantity=2, menu_item_id=4),
    OrderItem(order_item_id=7, order_number=1006, quantity=1, menu_item_id=5),
    OrderItem(order_item_id=8, order_number=1007, quantity=1, menu_item_id=6),
    OrderItem(order_item_id=9, order_number=1008, quantity=1, menu_item_id=7),
    OrderItem(order_item_id=10, order_number=1009, quantity=1, menu_item_id=8),
    OrderItem(order_item_id=11, order_number=1010, quantity=2, menu_item_id=9),
    OrderItem(order_item_id=12, order_number=1011, quantity=1, menu_item_id=10),
]

# Insert into database
with Session(engine) as session:
    session.query(OrderItem).delete()
    session.query(MenuItem).delete()
    session.commit()

    session.add_all(menu_items)
    session.add_all(order_items)
    session.commit()

# END OF ADRIANA'S CODE BLOCK


###Insert Customer and FoodOrder - Pranati Sukh 
from typing import List
from ClassesPython import engine, Customer, FoodOrder
from sqlalchemy.orm import Session
from datetime import datetime

##Inserting Sample Data into Both Tables
with Session(engine) as session:
    #Clearing Orders for Testing
    session.query(FoodOrder).delete()  #Clear FoodOrder first because Customer References It
    session.query(Customer).delete()    

    #Inserting into Customer
    c1 = Customer(id="C01", phone_number="6475803436", name="Guy")
    c2 = Customer(id="C02", phone_number="6781917295", name="Drew")
    c3 = Customer(id="C03", phone_number="9867457932", name="Martha")
    c4 = Customer(id="C04", phone_number="1124567890", name="Gertrude")
    c5 = Customer(id="C05", phone_number="0972468907", name="James")
    c6 = Customer(id="C06", phone_number="1247542347", name="Leo")
    c7 = Customer(id="C07", phone_number="9567235656", name="Luke")
    c8 = Customer(id="C08", phone_number="2346753456", name="Amy")
    c9 = Customer(id="C09", phone_number="1234565899", name="Jake")
    c10 = Customer(id="C10", phone_number="4564562237", name="Arnold")
    c11 = Customer(id="C11", phone_number="1119964434", name="Armie")
    c12 = Customer(id="C12", phone_number="9875214578", name="Angel")
    c13 = Customer(id="C13", phone_number="1234899533", name="Trent")
    c14 = Customer(id="C14", phone_number="8245678945", name="Penelope")
    c15 = Customer(id="C15", phone_number="2345783455", name="Drake")
    c16 = Customer(id="C16", phone_number="0764213466", name="Kendrick")
    c17 = Customer(id="C17", phone_number="5623123673", name="Dante")
    c18 = Customer(id="C18", phone_number="2843456787", name="Margot")
    c19 = Customer(id="C19", phone_number="3468007445", name="Mateo")
    c20 = Customer(id="C20", phone_number="2346845323", name="Henry")
    c21 = Customer(id="C21", phone_number="1039457683", name="Alan")
    c22 = Customer(id="C22", phone_number="4568783427", name="Sara")
    c23 = Customer(id="C23", phone_number="4572444773", name="Sarah")
    c24 = Customer(id="C24", phone_number="8652456236", name="Jeff")
    c25 = Customer(id="C25", phone_number="689301903", name="Kyle")
    c26 = Customer(id="C26", phone_number="6475146577", name="Oliver")
    c27 = Customer(id="C27", phone_number="6785029476", name="Nick")
    c28 = Customer(id="C28", phone_number="1238652438", name="Liam")
    c29 = Customer(id="C29", phone_number="0987654357", name="John")
    c30 = Customer(id="C30", phone_number="6677743566", name="Maria")
    c31 = Customer(id="C31", phone_number="8675333006", name="Andrea")
    c32 = Customer(id="C32", phone_number="4678920345", name="Evan")
    c33 = Customer(id="C33", phone_number="7789032345", name="Brian")
    c34 = Customer(id="C34", phone_number="4453321665", name="Yasmine")
    c35 = Customer(id="C35", phone_number="3334412277", name="Stella")

    session.add_all([c1, c2, c3, c4, c5, c6, c7, c8, c9, c10,
                     c11, c12, c13, c14, c15, c16, c17, c18, c19, c20,
                     c21, c22, c23, c24, c25, c26, c27, c28, c29, c30,
                     c31, c32, c33, c34, c35])
    session.commit()

#Inserting into FoodOrder
with Session(engine) as session:
    o1 = FoodOrder(number=1001, total_amount=25.50, time=datetime(2025, 3, 11, 9, 30), status="pending", customer_id="C01", truck_id="FT001")
    o2 = FoodOrder(number=1002, total_amount=32.75, time=datetime(2025, 3, 11, 10, 0), status="preparing", customer_id="C02", truck_id="FT002")
    o3 = FoodOrder(number=1003, total_amount=40.00, time=datetime(2025, 3, 11, 10, 30), status="ready", customer_id="C03", truck_id="FT003")
    o4 = FoodOrder(number=1004, total_amount=22.25, time=datetime(2025, 3, 11, 11, 0), status="canceled", customer_id="C04", truck_id="FT004")
    o5 = FoodOrder(number=1005, total_amount=28.50, time=datetime(2025, 3, 11, 11, 30), status="pending", customer_id="C05", truck_id="FT005")
    o6 = FoodOrder(number=1006, total_amount=35.00, time=datetime(2025, 3, 11, 12, 0), status="ready", customer_id="C06", truck_id="FT006")
    o7 = FoodOrder(number=1007, total_amount=30.40, time=datetime(2025, 3, 11, 12, 30), status="preparing", customer_id="C07", truck_id="FT007")
    o8 = FoodOrder(number=1008, total_amount=50.25, time=datetime(2025, 3, 11, 13, 0), status="pending", customer_id="C08", truck_id="FT008")
    o9 = FoodOrder(number=1009, total_amount=22.15, time=datetime(2025, 3, 11, 13, 30), status="ready", customer_id="C09", truck_id="FT009")
    o10 = FoodOrder(number=1010, total_amount=29.50, time=datetime(2025, 3, 11, 14, 0), status="pending", customer_id="C10", truck_id="FT010")
    o11 = FoodOrder(number=1011, total_amount=26.00, time=datetime(2025, 3, 11, 14, 30), status="preparing", customer_id="C11", truck_id="FT001")
    o12 = FoodOrder(number=1012, total_amount=33.50, time=datetime(2025, 3, 11, 15, 0), status="ready", customer_id="C12", truck_id="FT002")
    o13 = FoodOrder(number=1013, total_amount=45.00, time=datetime(2025, 3, 11, 15, 30), status="canceled", customer_id="C13", truck_id="FT003")
    o14 = FoodOrder(number=1014, total_amount=23.75, time=datetime(2025, 3, 11, 16, 0), status="pending", customer_id="C14", truck_id="FT004")
    o15 = FoodOrder(number=1015, total_amount=31.90, time=datetime(2025, 3, 11, 16, 30), status="ready", customer_id="C15", truck_id="FT005")
    o16 = FoodOrder(number=1016, total_amount=27.00, time=datetime(2025, 3, 11, 17, 0), status="pending", customer_id="C16", truck_id="FT006")
    o17 = FoodOrder(number=1017, total_amount=39.50, time=datetime(2025, 3, 11, 17, 30), status="preparing", customer_id="C17", truck_id="FT007")
    o18 = FoodOrder(number=1018, total_amount=41.25, time=datetime(2025, 3, 11, 18, 0), status="ready", customer_id="C18", truck_id="FT008")
    o19 = FoodOrder(number=1019, total_amount=29.80, time=datetime(2025, 3, 11, 18, 30), status="pending", customer_id="C19", truck_id="FT009")
    o20 = FoodOrder(number=1020, total_amount=34.10, time=datetime(2025, 3, 11, 19, 0), status="ready", customer_id="C20", truck_id="FT010")

    session.add_all([o1, o2, o3, o4, o5, o6, o7, o8, o9, o10,
                     o11, o12, o13, o14, o15, o16, o17, o18, o19, o20])
    session.commit()

###End Code Block - Pranati Sukh
