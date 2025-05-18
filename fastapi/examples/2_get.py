from fastapi import FastAPI,Path,HTTPException
import json

app=FastAPI()


def load_data():
    with open("patients.json","r") as f:
        data=json.load(f)
        
    return data

@app.get("/")
def hello():
    return {"message":"Patient Management System"}

@app.get("/about")
def about():
    return {"message":"This is a patient management system built with FastAPI."}

@app.get('/view/{patient_id}')
def view(patient_id:str=Path(...,description="The ID of the patient to view",example='P001')):
    data=load_data()
    
    if patient_id in data:
        return data[patient_id]
    return HTTPException(status_code=404,detail="Patient not found")