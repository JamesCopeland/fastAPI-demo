from fastapi import APIRouter, HTTPException, Path, Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import TeamSchema, Request, RequestTeam, Response
import team_crud

team_router = APIRouter()

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()

@team_router.post('/create')
async def create(request:RequestTeam, db:Session=Depends(get_db)):
    team_crud.create_team(db, team=request.parameter)
    return Response(code=200,status="Ok",message="Team created").dict(exclude_none=True)

@team_router.get("/")
async def get(db:Session=Depends(get_db)):
    _teams = team_crud.get_team(db,0,100)
    return Response(code=200, status="Ok",message="Got list of teams", result=_teams).dict(exclude_none=True)

@team_router.get("/{id}")
async def get_by_id(id:int, db:Session = Depends(get_db)):
    _team = team_crud.get_team_by_id(db,id)
    return Response(code=200, status="Ok", message="Got team", result=_team).dict(exclude_none=True)

@team_router.patch("/update")
async def update_team(request: RequestTeam, db:Session = Depends(get_db)):
    _team = team_crud.update_team(db,team_id=request.parameter.id,name=request.parameter.name,description=request.parameter.description)
    return Response(code=200, status="Ok", message="Updated team data", result=_team)

@team_router.delete("/{id}")
async def delete(id:int, db:Session = Depends(get_db)):
    team_crud.remove_team(db, team_id=id)
    return Response(code=200, status="Ok", message="Delete team").dict(exclude_none=True)
