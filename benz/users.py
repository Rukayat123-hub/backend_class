from database import db
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel,Field
from sqlalchemy import text
import os
from dotenv import load_dotenv
import uvicorn
load_dotenv()
app =FastAPI(title="Simple App", version="1.0.0")

class Simple(BaseModel):
    name: str = Field(..., example="Sam Larry")
    email: str = Field(..., example="Sam@email.com")
    password: str = Field(..., example="Sam1223")
@app.post("/signup")
def signup(input:Simple):
    try:
        query = text(""""
             INSERT INTO USERS (name email,password)
             VALUES (name email,password) 
      """)
        salt = bcrypt.gensalt()
        hashedPassword =bcrypt.hashpw(input.password.encode('utf-8'),salt)
       db.execute(query, {"name": input.name, "email":input.email, "password": hashedPassword}) 

