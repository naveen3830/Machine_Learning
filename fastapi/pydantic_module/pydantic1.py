from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    id:int
    name:str
    is_active:bool
    
input_data={'id':1,"name":"Naveen","is_active":True}

user=User(**input_data)
print(user)

class Product(BaseModel):
    id:int
    name:str
    price:float
    in_stock:bool
    
# Pydantic needs to know which value corresponds to which field
product=Product(id='1',name='mobile phones',price='1000.00',in_stock='True')
print(product)

from typing import Optional, List, Dict

class Cart(BaseModel):
    user_id:int
    items:List[str]
    quantities:Dict[str,int]
    
class BlogPost(BaseModel):
    title:str
    content:str
    image_url:Optional[str]=None
    
from pydantic import Field
class Employee(BaseModel):
    id:int
    name:str=Field(...,min_length=3,max_length=100)
    department:Optional[str]="General"
    salary:int=Field(...,gt=10000,lt=1000000)
