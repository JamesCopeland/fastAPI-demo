from fastapi import APIRouter, HTTPException, Path, Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import PersonSchema, Request, RequestPerson, Response
import person_crud

person_router = APIRouter()

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()

@person_router.post('/create')
async def create(request:RequestPerson, db:Session=Depends(get_db)):
    person_crud.create_person(db, person=request.parameter)
    return Response(code=200,status="Ok",message="Person created").dict(exclude_none=True)

@person_router.get("/")
async def get(db:Session=Depends(get_db)):
    _persons = person_crud.get_person(db,0,100)
    return Response(code=200, status="Ok",message="Got list of people", result=_persons).dict(exclude_none=True)

@person_router.get("/{id}")
async def get_by_id(id:int, db:Session = Depends(get_db)):
    _person = person_crud.get_person_by_id(db,id)
    return Response(code=200, status="Ok", message="Got person", result=_person).dict(exclude_none=True)

@person_router.patch("/update")
async def update_person(request: RequestPerson, db:Session = Depends(get_db)):
    _person = person_crud.update_person(db,person_id=request.parameter.id,title=request.parameter.title,description=request.parameter.description,firstName=request.parameter.firstName,lastName=request.parameter.lastName,team_id=request.parameter.team_id)
    return Response(code=200, status="Ok", message="Updated person data", result=_person)

@person_router.delete("/{id}")
async def delete(id:int, db:Session = Depends(get_db)):
    person_crud.remove_person(db, person_id=id)
    return Response(code=200, status="Ok", message="Delete person").dict(exclude_none=True)
