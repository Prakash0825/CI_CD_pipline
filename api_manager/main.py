from fastapi import FastAPI,UploadFile
from pydantic import BaseModel
from config import config
from orchestrator.stream import Stream  # Now importing directly from stream module

app = FastAPI()

# Initialize stream
stream = Stream()

class items(BaseModel):
    file_path: str
    filter_column: str
    filter_value: str
    filter_type: str


@app.get("/")
async def root():
    return {"message": "welcome to the pipeline dataframe project"}

@app.post('/read')
async def read_data(file: UploadFile):
    file_path = f"../uploads/{file.filename}"
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())
    df = await stream.read_data(file_path)
    print(df)
    return {"message": "file uploaded successfully", "data": df['Port Name'].to_list()}


    
