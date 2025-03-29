
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
