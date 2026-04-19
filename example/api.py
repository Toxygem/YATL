from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class UserInfo(BaseModel):
    email: str
    phone: str


class User(BaseModel):
    name: str
    age: int
    info: UserInfo


app = FastAPI()

users = {
    1: {
        "name": "John Doe",
        "age": 30,
        "info": {"email": "john.doe@example.com", "phone": "1234567890"},
    }
}


@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return users[user_id]


@app.post("/users", status_code=201)
def create_user(user: User):
    user_id = len(users) + 1
    users[user_id] = user.dict()
    return users[user_id]


@app.get("/users")
def user_count():
    return {"count": len(users)}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
