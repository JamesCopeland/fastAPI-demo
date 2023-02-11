from fastapi import FastAPI, Path, Query, HTTPException, status
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def home():
    return {"Data": "Test"}

@app.get('/about')
def about():
    return {"Data": "About"}