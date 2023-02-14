from sqlalchemy.orm import Session
from models import Person
from schemas import PersonSchema 

def get_person(db:Session, skip: int=0, limit:int=100):
    return db.query(Person).offset(skip).limit(limit).all()

def get_person_by_id(db:Session, person_id: int):
    return db.query(Person).filter(Person.id == person_id).first()

def create_person(db:Session, person: PersonSchema):
    _person = Person(title=person.title, description=person.description, firstName=person.firstName, lastName=person.lastName, team_id=person.team_id)
    db.add(_person)
    db.commit()
    db.refresh(_person)
    return _person

def remove_person(db:Session, person_id:int):
    _person = get_person_by_id(db=db, person_id=person_id)
    db.delete(_person)
    db.commit()

def update_person(db:Session, person_id:int, title:str, description:str, firstName:str, lastName:str, team_id:int):
    _person = get_person_by_id(db=db, person_id=person_id)

    if title is not None:
        _person.title = title
    if description is not None:
        _person.description = description
    if firstName is not None:
        _person.firstName = firstName
    if lastName is not None:
        _person.lastName = lastName
    if team_id is not None:
        _person.team_id = team_id

    db.commit()
    db.refresh(_person)
    return _person