from http import client
from typing import Collection
from unittest import result
from xml.dom.minidom import Document
from model import User

import motor.motor_asyncio


client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")

database = client.User


collection = database.User_data


async def create_blog(blog):
    document = blog
    result = await collection.insert_one(blog)
    return document

async def fetch_one(user):
    document = await collection.find_one({"name":user})
    return document