from unittest import async_case
from urllib import response
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database import *

from model import Blog

app = FastAPI()


origins = ["localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = ["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.post("/api/create",response_model = Blog)
async def create_one(user:Blog):
    result = await create_blog(user.dict())
    if result:
        return result
    raise HTTPException(400,"Error not found")
    

@app.get("/api/get/")
async def get_one():
    try:
        result = await fetch_all()
        
        if result:
            return result
    except Exception as msg:
        raise HTTPException(400,msg)
    