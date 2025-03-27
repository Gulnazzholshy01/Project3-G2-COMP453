
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
