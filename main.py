from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Data(BaseModel):
    id: int
    patient_name: str
    appointment_date: str

datas = []

@app.get("/datas", response_model=List[Data])
async def read_datas():
    return datas

@app.post("/datas", response_model=Data)
async def create_datas(data: Data):
    datas.append(data)
    return data

@app.put("/datas/{data_id}", response_model=Data)
async def update_datas(data_id: int, data: Data):
    try:
        if data_id - 1 < len(datas):
            datas[data_id - 1] = data  # Update the existing data with the new one
            return data
        else:
            raise HTTPException(status_code=404, detail="Data not found")
    except IndexError:
        raise HTTPException(status_code=404, detail="Data not found")

@app.delete("/datas/{data_id}")
async def delete_data(data_id: int):
    try:
        if data_id - 1 < len(datas):
            del datas[data_id - 1]  # Adjusting index to match the list's index
            return {"message": "Data deleted"}
        else:
            raise HTTPException(status_code=404, detail="Data not found")
    except IndexError:
        raise HTTPException(status_code=404, detail="Data not found")