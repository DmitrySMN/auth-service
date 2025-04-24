from typing import Annotated
from annotated_types import MaxLen, MinLen
from pydantic import BaseModel, ConfigDict, EmailStr


class UserBase(BaseModel):
    email: Annotated[str, EmailStr]
    name: Annotated[str, MinLen(3), MaxLen(12)]
    password: Annotated[str, MinLen(8)]


class User(UserBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


class UserCreate(BaseModel):
    pass
