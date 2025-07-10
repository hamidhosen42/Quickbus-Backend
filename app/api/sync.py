from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

class SyncPayload(BaseModel):
    device_id: str
    tickets: List[dict]  # You can define a proper TicketSyncModel if needed

@router.post("/offline")
async def sync_offline_data(payload: SyncPayload):
    # Save data to DB or process offline sync logic
    return {"message": "Offline tickets synced successfully"}

@router.get("/status")
async def sync_status():
    # Optionally return last sync time/device state
    return {"status": "online", "last_sync": "2025-07-10 10:00"}