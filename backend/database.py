from http import client
from typing import Collection
from unittest import result
from xml.dom.minidom import Document
from model import Blog

import motor.motor_asyncio


client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")

database = client.BLOG_PROJECT


collection = database.blogs


async def create_blog(blog):
    document = blog
    result = await collection.insert_one(blog)
    return document

async def fetch_all() -> dict:
    result = []
    document = collection.find({})
    async for data in document:
        result.append(Blog(**data))
    return result