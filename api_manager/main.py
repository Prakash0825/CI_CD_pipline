from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class items(BaseModel):
    file_path: str
    filter_column: str
    filter_value: str
    filter_type: str


@app.get("/")
async def root():
    return {"message": "welcome to the pipeline dataframe project"}

@app.post('/read')
async def read_data(item: items):
    
