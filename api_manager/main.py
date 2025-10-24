from fastapi import FastAPI,UploadFile
from pydantic import BaseModel
from api_manager.config import config
from pathlib import Path
import os
import pandas as pd
from orchestrator.stream import Manipulation  # Now importing directly from stream module



unique_id = {"unique_id": 0}
app = FastAPI()

# Initialize stream
stream = Manipulation()

class Items(BaseModel):
    filter_column: str
    filter_value: str
    filter_type: str


@app.get("/")
async def root():
    return {"message": "welcome to the pipeline dataframe project"}

@app.post('/read')
async def read_data(file: UploadFile):
    safe_filename = Path(f"file_{unique_id['unique_id']}_{file.filename}").name
    file_path = os.path.join(config.import_paths['uploads'], safe_filename)
    # Ensure upload directory exists
    os.makedirs(config.import_paths['uploads'], exist_ok=True)
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())
    df = await stream.read_data(file_path)
    df = df.to_pandas()
    print(df)
    unique_id['unique_id'] += 1
    return {"message": "file uploaded successfully","unique_id" :safe_filename, "data": df.to_dict(orient='records')}

@app.post('/filter')
async def filter_data(unique_id: str,item : Items):
    file_path = os.path.join(config.import_paths['uploads'], unique_id)
    df = await stream.read_data(file_path)
    df = await stream.filter_data(df, item.filter_column, item.filter_value, item.filter_type)
    df = df.to_pandas()
    return {"message": "file uploaded successfully", "data": df.to_dict(orient='records')}

    
