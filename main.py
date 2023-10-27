from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str

users = []

@app.get("/")
async def read_root():
    return {"Hello": "World"}

# Get all users
@app.get("/users")
async def get_users():
    return {"users": users}

# Get a single user
@app.get("/users/{user_id}")
async def get_single_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return {"user": user}
    return {"message": "No user found"}

# Add a user
@app.post("/users")
async def add_single_user(user: User):
    users.append(user)
    return {"users": users}

# Delete a user
@app.delete("/users")
async def delete_single_user(user_id: int):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return {"users": users}
    return {"message": "No user found"}