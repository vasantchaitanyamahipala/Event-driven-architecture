from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: int
    name: str
    email: str

class Ticket(BaseModel):
    id: int
    title: str
    description: str
    priority: str
    status: str = "Open"
    user_id: int
