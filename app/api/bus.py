from fastapi import APIRouter, HTTPException
from app.models.bus import BusCreate, BusUpdate
from app.services import bus_service

router = APIRouter()

@router.get("/", summary="List all buses")
async def list_buses():
    buses = await bus_service.get_all_buses()
    return {
        "statusCode": 200,
        "status": "SUCCESS",
        "message": "Fetched bus list",
        "data": buses,
    }

@router.post("/", summary="Register a new bus")
async def register_bus(payload: BusCreate):
    # Save bus and return full object back
    inserted_bus = await bus_service.create_bus(payload)

    return {
        "statusCode": 200,
        "status": "SUCCESS",
        "message": "Bus registered successfully",
        "data": {
            "bus_number": inserted_bus.bus_number,
            "model": inserted_bus.model,
            "capacity": inserted_bus.capacity,
            "seat_layout": inserted_bus.seat_layout,
            "driver_name": inserted_bus.driver_name,
            "conductor_name": inserted_bus.conductor_name,
            "assigned_route": inserted_bus.assigned_route,
            "status": inserted_bus.status
        }
    }


@router.put("/{bus_id}", summary="Update bus")
async def edit_bus(bus_id: str, payload: BusUpdate):
    updated = await bus_service.update_bus(bus_id, payload)
    if not updated:
        raise HTTPException(status_code=404, detail="Bus not found")
    return {
        "statusCode": 200,
        "status": "SUCCESS",
        "message": "Bus updated successfully",
    }

@router.delete("/{bus_id}", summary="Delete bus")
async def delete_bus(bus_id: str):
    deleted = await bus_service.delete_bus(bus_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Bus not found")
    return {
        "statusCode": 200,
        "status": "SUCCESS",
        "message": "Bus deleted successfully",
    }