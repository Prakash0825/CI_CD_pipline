from fastapi.testclient import TestClient
from api_manager.main import app
import polars as pl


client = TestClient(app)

data1 = {
  "message": "file uploaded successfully",
  "unique_id": "file_0_input_test.csv",
  "data": [
    {
      "name": 1,
      "age": 25,
      "city": "new york"
    },
    {
      "name": 2,
      "age": 30,
      "city": "los angeles"
    },
    {
      "name": 3,
      "age": 35,
      "city": "chicago"
    }
  ]
}
data2 = {
  "message": "file uploaded successfully",
  "data": [
    {
      "name": 1,
      "age": 25,
      "city": "new york"
    }
  ]
}

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "welcome to the pipeline dataframe project"}

def test_read_data():
    input_file_path = "files/inputs/input_test.csv"
    with open(input_file_path, "rb") as file:
        response = client.post("/read", files={"file": file})

    assert response.status_code == 200
    assert response.json() == data1

def test_filter_data():
    
    response = client.post(
        "/filter?unique_id=file_0_input_test.csv", 
        json={
            "filter_column": "name", 
            "filter_value": "1",  
            "filter_type": "equals"
        }
    )    
    assert response.status_code == 200
    assert response.json() == data2



