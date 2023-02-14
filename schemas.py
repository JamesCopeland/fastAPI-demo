from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')

class PersonSchema(BaseModel):
    id: Optional[int]=None
    title: Optional[str]=None
    description: Optional[str]=None
    firstName: Optional[str]=None
    lastName: Optional[str]=None
    team_id: Optional[int]=None

    class Config: 
        orm_mode = True

class TeamSchema(BaseModel):
    id: Optional[int]=None
    name: Optional[str]=None
    description: Optional[str]=None

    class Config: 
        orm_mode = True

class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)

class RequestTeam(BaseModel):
    parameter: TeamSchema = Field(...)

class RequestPerson(BaseModel):
    parameter: PersonSchema = Field(...)

class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]