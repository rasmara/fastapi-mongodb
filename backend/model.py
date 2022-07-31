from pydantic import BaseModel, EmailStr
from typing import Optional,



class Blog(BaseModel):
    title : str
    description: str
    author: str


class User(BaseModel):
    name : str
    email : EmailStr 
    
    
    