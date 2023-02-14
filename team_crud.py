from sqlalchemy.orm import Session
from models import Team
from schemas import TeamSchema 

def get_team(db:Session, skip: int=0, limit:int=100):
    return db.query(Team).offset(skip).limit(limit).all()

def get_team_by_id(db:Session, team_id: int):
    return db.query(Team).filter(Team.id == team_id).first()

def create_team(db:Session, team: TeamSchema):
    _team = Team(name=team.name, description=team.description)
    db.add(_team)
    db.commit()
    db.refresh(_team)
    return _team

def remove_team(db:Session, team_id:int):
    _team = get_team_by_id(db=db, team_id=team_id)
    db.delete(_team)
    db.commit()

def update_team(db:Session, team_id:int, name:str, description:str):
    _team = get_team_by_id(db=db, team_id=team_id)

    _team.name = name
    _team.description = description
    
    db.commit()
    db.refresh(_team)
    return _team