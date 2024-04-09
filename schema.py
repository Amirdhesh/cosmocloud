from pydantic import BaseModel
from typing import Optional


class Address(BaseModel):
    city: str
    country: str


class Student(BaseModel):
    name: str
    age: int
    address: Address


class UpdateAddress(BaseModel):
    city: Optional[str]
    country: Optional[str]


class UpdateStudent(BaseModel):
    name: Optional[str]
    age: Optional[int]
    address: Optional[Address]
