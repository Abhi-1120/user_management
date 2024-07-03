from datetime import date
from typing import Any, List, Optional
from pydantic import BaseModel, EmailStr


__all__ = ["DefaultResponseSchema", "UserRequestSchema", "UserSchema"]


class DefaultResponseSchema(BaseModel):
    ok: bool = True


class UserRequestSchema(BaseModel):
    id: Optional[int] = None
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    mobile_no: str = None
    project_id: int = None
    date_of_birth: date


class UserSchema(BaseModel):
    id: Optional[int] = None
    first_name: str
    last_name: str
    email: EmailStr
    mobile_no: str = None
    project_id: int = None
    date_of_birth: date
