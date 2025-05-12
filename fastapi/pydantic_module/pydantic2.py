# Different types of validators in pydantic
from pydantic import BaseModel, Field, field_validator, model_validator, computed_field
from typing import Optional, List, Dict

class User(BaseModel):
    username:str
    
    # field_validator is used to validate the value of a field
    # It is used to validate the value of a field after it has been parsed
    @field_validator('username')
    def username(cls,v):
        if len(v)<4:
            raise ValueError('Username must be at least 4 characters long')
        return v
        0
class SignupData(BaseModel):
    password:str
    confirm_password:str
    
    # if mode="after" then it will be called after all the fields have been validated
    @model_validator(mode='after')
    def password_match(cls,values):
        if values.password!=values.confirm_password:
            raise ValueError('Password and confirm password do not match')
        return values
    
class Product(BaseModel):
    price=float
    quantity:int
    
    # computed_field is used to create a field that is computed from other fields
    @computed_field
    @property
    def total_price(self):
        return self.price*self.quantity
    
class Booking(BaseModel):
    user_id:int
    room_id:int
    nigths:int=Field(...,ge=1)
    rate_per_night:float
    
    @computed_field
    @property
    def total_amount(self)-> float:
        return self.nigths*self.rate_per_night