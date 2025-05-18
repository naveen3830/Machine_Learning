from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

class Main():
    def __init__(self):
        self.app=FastAPI()
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
        )
        
        @self.app.get("/")
        async def root():
            return {"message":"The app is up and running"}
        
        
main_app=Main()
app=main_app.app