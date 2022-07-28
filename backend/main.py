from unittest import async_case
from urllib import response
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database import *

from model import User

app = FastAPI()


origins = ["localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = ["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.post("/api/create",response_model = User)
async def create_one(user:User):
    result = await create_blog(user.dict())
    if result:
        return result
    raise HTTPException(400,"Error not found")
    

@app.get("/api/get/{id}",response_model = User)
async def get_one(id:str):
    import pdb;pdb.set_trace()
    result = await fetch_one(id)
    if result:
        return result
    raise HTTPException(400,"Error not found")
    