from fastapi import FastAPI, Path, Query, HTTPException, status
from fastapi.responses import RedirectResponse
from typing import Optional
from pydantic import BaseModel
import models
from config import engine
from person_route import person_router
from team_route import team_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get('/')
def home():
    return RedirectResponse(url='/docs')

app.include_router(person_router,prefix="/person",tags=["person"])

app.include_router(team_router,prefix="/team",tags=["team"])