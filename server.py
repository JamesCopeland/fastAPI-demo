from fastapi import FastAPI, Path, Query, HTTPException, status
from typing import Optional
from pydantic import BaseModel
import model
from config import engine
from routes import router

model.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get('/')
def home():
    return {"Data": "Test"}

@app.get('/about')
def about():
    return {"Data": "About"}

app.include_router(router,prefix="/book",tags="[book]")