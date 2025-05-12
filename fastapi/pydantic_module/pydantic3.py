# Model reference and nested models

from pydantic import BaseModel, Field
from typing import List, Optional, Dict

class Adress(BaseModel):
    street:str
    city:str
    postal_code:str
    
# Nested model reference
class User(BaseModel):
    id:int
    name:str
    adress:Adress

class Comment(BaseModel):
    id:int
    content:str
    replies:Optional[List['Comment']]=None
    
Comment.model_rebuild()
# This is used to resolve the forward reference of the Comment model

adress=Adress(street='123 Main St', city='New York', postal_code='10001')
user=User(id=1, name='John Doe', adress=adress)
print(user)

comment=Comment(id=1, content='This is a comment',
                replies=[Comment(id=2,content="reply 1"),
                        Comment(id=3,content="reply 2")
                        ])

print(comment)

# Example 
class Lesson(BaseModel):
    lesson_id:int
    lesson_name:str
    
class Module(BaseModel):
    module_id:int
    module_name:str
    lessons:List[Lesson]
    
class Course(BaseModel):
    course_id:int
    course_name:str
    modules:List[Module]



