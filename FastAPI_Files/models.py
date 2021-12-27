from typing import List, Optional
from pydantic import BaseModel
from uuid import UUID, uuid4 
from enum import Enum

class Gender(str,Enum):
    male = "MALE"
    female = "FEMALE" 

class Role(str,Enum):
    admin = "ADMIN"
    student = "STUDENT" 
    teacher ="TEACHER"
    user = "USER"

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    gender: Gender
    roles: List[Role]
