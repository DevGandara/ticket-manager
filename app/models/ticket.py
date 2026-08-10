from pydantic import BaseModel
from datetime import datetime
from typing import Literal, Field # Literal sirve para limitar opciones, Field sirve para validaciones

class TicketCreate(BaseModel):
    title: str
    priority: Literal["low", "medium", "high"]
    description: str
    created_by: str
    assigned_to: str | None = None

class Ticket(BaseModel):
    id: int
    title: str
    priority: Literal["low", "medium", "high"]
    description: str
    created_at: datetime = Field(default_factory=datetime.now) # Si no recibe fecha, se asigna la fecha actual
    created_by: str
    assigned_to: str | None = None
    