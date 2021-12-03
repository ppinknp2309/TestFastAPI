from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id:int
    name:str
    age:Optional[int] = None
    score:float
app = FastAPI()

@app.post("/users/")
async def create_item(User:User):
    return user