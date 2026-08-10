from fastapi import APIRouter
from tickets import TicketCreate

router = APIRouter(
    prefix="/tickets",
    tags=["tickets"] # Tags sirven mas que nada para la documentación de la API (OpenAPI)
)

@router.get("/")
def get_tickets():
    return {"message": "List of tickets"} # provisional hasta que se guarde en bd

@router.post("/")
def create_ticket(ticket: TicketCreate):
    return {"message": "Ticket created", "ticket": ticket} # provisional hasta que se guarde en bd

@router.get("/{ticket_id}")
def get_ticket(ticket_id: int):
    return {"message": f"Details of ticket {ticket_id}"} # provisional hasta que se guarde en bd

@router.put("/{ticket_id}")
def update_ticket(ticket_id: int, ticket: TicketCreate):
    return {"message": f"Ticket {ticket_id} updated", "ticket": ticket} # provisional hasta que se guarde en bd

@router.delete("/{ticket_id}")
def delete_ticket(ticket_id: int):
    return {"message": f"Ticket {ticket_id} deleted"} # provisional hasta que se guarde en bd