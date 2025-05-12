# Pydantic serialization and deserialization

from pydantic import BaseModel, Field, ConfigDict
from typing import List,Optional, Dict
from datetime import datetime

class Adress(BaseModel):
    street:str
    city:str
    zip_code:str
    
class User(BaseModel):
    id:int
    name:str
    email:str
    is_active:bool=True
    created_at:datetime
    adress: Adress
    tags:List[str]=[]
    
    model_congig=ConfigDict(
        json_encoders={
            datetime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S'),
        }
    )
    
user=User(
    id=1,
    name='John Doe',
    email="johndoe@gmail.com",
    is_active=True,
    created_at=datetime(2023,10,1,12,0,0),
    adress=Adress(
        street='123 Main St',
        city='New York',
        zip_code='10001'
    ),
    tags=["premium","subscriber"]
)

# using model_dump() method to serialize the model to a dictionary
pyton_dict=user.model_dump()
print(pyton_dict.keys())

print("====================")
# using model_dump_json() method to serialize the model to a json string
json_string=user.model_dump_json()  
print(json_string)