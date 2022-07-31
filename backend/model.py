from pydantic import BaseModel, EmailStr




class Blog(BaseModel):
    title : str
    description: str
    author: str


class User(BaseModel):
    name : str
    email : EmailStr 
    
    
    