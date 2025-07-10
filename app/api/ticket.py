from fastapi import APIRouter, HTTPException
from bson import ObjectId
from app.db.mongo import db
from app.models.ticket import Ticket, TicketInDB

router = APIRouter()

@router.post("/book", response_model=TicketInDB)
async def book_ticket(ticket: Ticket):
    ticket_dict = ticket.dict()
    result = await db.tickets.insert_one(ticket_dict)
    return TicketInDB(**ticket_dict, id=str(result.inserted_id))

@router.get("/validate/{ticket_id}")
async def validate_ticket(ticket_id: str):
    ticket = await db.tickets.find_one({"_id": ObjectId(ticket_id)})
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    if ticket.get("used"):
        return {"status": "invalid", "message": "Ticket already used"}
    await db.tickets.update_one({"_id": ObjectId(ticket_id)}, {"$set": {"used": True}})
    return {"status": "valid", "ticket": ticket}
