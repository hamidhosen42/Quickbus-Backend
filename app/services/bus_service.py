from app.db.mongo import db
from app.models.bus import BusCreate, BusInDB, BusUpdate
from bson import ObjectId

async def get_all_buses():
    buses = []
    async for bus in db.buses.find():
        bus["_id"] = str(bus["_id"])
        buses.append(bus)
    return buses

async def create_bus(payload: BusCreate):
    result = await db.buses.insert_one(payload.dict())
    bus = await db.buses.find_one({"_id": result.inserted_id})
    return BusInDB(**bus)  

async def update_bus(bus_id: str, update_data: BusUpdate):
    result = await db.buses.update_one(
        {"_id": ObjectId(bus_id)},
        {"$set": update_data.dict()}
    )
    return result.modified_count > 0

async def delete_bus(bus_id: str):
    result = await db.buses.delete_one({"_id": ObjectId(bus_id)})
    return result.deleted_count > 0