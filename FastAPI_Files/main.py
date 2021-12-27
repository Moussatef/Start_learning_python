from typing import List, Optional
from uuid import uuid4

from fastapi import FastAPI
from models import User, Gender, Role

app = FastAPI()

db: List[User] = [
    User(id=uuid4(),
         first_name='John',
         last_name='Moussatef',
         gender=Gender.male,
         roles=[Role.user, Role.teacher])
]

# class User:
#     def __init__(self, name, email, country, city, company):
#         self.name = name
#         self.email = email
#         self.country = country
#         self.city = city
#         self.company = company

# othman = User("Moussatef Othman", "othman.moussatef@gmail.com", "Morocco",
#               "Safi", "CGDEM")


@app.get("/")
async def read_root():
    return {"Welcome": "To my FastApi application"}


@app.get("/api/users")
async def fetchUsers():
    return db


@app.post("/api/add/user")
async def addUser(user: User):
    db.append(user)
    return {"Message": "User add successfully", "ID": user.id}


# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: Optional[str] = None):
#     return {
#         "item_id": item_id,
#         "name": othman.name,
#         "email": othman.email,
#         "country": othman.country,
#         "city": othman.city,
#         "company": othman.company,
#     }
