from fastapi import FastAPI



app = FastAPI()

@app.get("/greet")
async def greet():
    return "Hello World"

@app.get("/items")
def get_items():
    return  "all items"










@app.get("/")
def hello():
    return "hii Ali"