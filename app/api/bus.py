from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_buses():
    return {"message": "List of buses"}