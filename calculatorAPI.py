# @app.get("/")
# def read_root():
#     return {"message": "Hello World"}
from typing import List
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()


@app.get("/add")
def add(a: int,b: int):
    return {"result": a + b}

@app.get("/subtract")
def subtract(a: int,b: int):
    return {"result": a - b}

@app.get("/multiply")
def multiply(a: int,b: int):
    return {"result": a * b}
@app.get("/divide")
def divide(a: int,b: int):
    if b == 0:
        return {"result": "you can't divide by zero"}
    else:
         return {"result": a / b}

@app.post("/numbers")
def numbers_sum(numbers: List[int]):
    return {"result": sum(numbers)}
