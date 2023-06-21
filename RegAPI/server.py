from fastapi import FastAPI
import uvicorn
from db_logic import *

app = FastAPI()


@app.get('/')
async def root():
    return {"message": "It's working!"}


@app.post('/registration')
async def reg_user(user_data: list):
    id = len(get_all_users())
    username = user_data[0]['username']
    name = user_data[0]['name']
    email = user_data[0]['email']
    age = user_data[0]['age']
    add_user(id, username, name, email, age)


@app.get('/getUsers')
async def get_users():
    return {"status": 200, "data": get_all_users()}


if __name__ == "__main__":
    uvicorn.run("server:app", port=5000)
