from fastapi import APIRouter
from app.db.mongo import db

router = APIRouter()

@router.get("/daily")
async def daily_summary():
    count = await db.tickets.count_documents({})
    return {"total_tickets": count}