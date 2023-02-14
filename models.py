from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config import Base

class Team(Base):
    __tablename__ = "team"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    people = relationship("Person")

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    firstName = Column(String)
    lastName = Column(String)
    description = Column(String)
    team_id = Column(Integer, ForeignKey("team.id"))
