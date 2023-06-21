from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get('/')
async def root():
    return {"message": "It's working!"}


@app.post('/test')
async def test(data: list):
    print(data)


# @app.post('/registration')
# async def reg_user(user_data: list):
#     print(user_data)


if __name__ == "__main__":
    uvicorn.run("server:app", port=5000)
