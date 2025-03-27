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

print("")
print("Q2 - Student: ")
print("")

print("")
print("Q3 - Student: ")
print("")

print("")
print("Q4 - Student: ")
print("")
