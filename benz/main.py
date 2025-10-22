from fastapi import FastAPI
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import uvicorn
import os

# Load environment variables from .env file
load_dotenv()

# Initialize the FastAPI app
app = FastAPI(title="Simple FastAPI App", version="1.0.0")

# Sample in-memory data
data = [
    {"name": "Sam Lary", "age": 20, "track": "AI Developer"},
    {"name": "Bahubili", "age": 25, "track": "AI Frontend"},
    {"name": "Perpetual", "age": 30, "track": "AI Backend"},
]

# Data model
class Item(BaseModel):
    name: str = Field(..., example="Perpetual")
    age: int = Field(..., example=25)
    track: str = Field(..., example="Fullstack Developer")


@app.get("/", description="This endpoint just returns a welcome message")
def root():
    return {"message": "Welcome to my FastAPI Application 🚀"}


@app.get("/get-data", description="Retrieve all data entries")
def get_data():
    return data


@app.post("/create-data", description="Add a new entry to the data list")
def create_data(req: Item):
    data.append(req.dict())
    return {"message": "Data received successfully ", "data": data}


@app.patch("/update-data/{id}", description="Update an existing entry by its index")
def update_data(id: int, req: Item):
    if 0 <= id < len(data):
        data[id] = req.dict()
        return {"message": f"Data at index {id} updated successfully ", "data": data}
    return {"error": "Invalid ID — no data found at that index."}


if __name__ == "__main__":
    host = os.getenv("HOST", "127.0.0.1")
    port = int(os.getenv("PORT", 8000))
    print(f"🚀 Starting server on http://{host}:{port}")
    uvicorn.run(app, host=host, port=port)
