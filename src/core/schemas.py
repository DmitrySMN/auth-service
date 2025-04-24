from typing import Annotated
from annotated_types import MaxLen, MinLen
from pydantic import BaseModel, EmailStr



class User(BaseModel):
    email: Annotated[str, EmailStr]
    name: Annotated[str, MinLen(3), MaxLen(12)]
    password: Annotated[str, MinLen(8)]