from fastapi import APIRouter, HTTPException, Depends
from app.models.route import RouteCreate, RouteInDB, RouteUpdate, ApiResponse
from app.services.route_service import (
    get_all_routes,
    create_route,
    update_route,
    delete_route,
    toggle_route_status
)
from app.core.dependencies import get_current_user
from typing import List

router = APIRouter()

@router.get("/", response_model=ApiResponse[List[RouteInDB]], summary="List all routes")
async def list_routes():
    """
    Retrieve a list of all routes.
    """
    routes = get_all_routes()
    return {
        "statusCode": 200,
        "status": "SUCCESS",
        "message": "Fetched route list",
        "data": routes,
    }

@router.post("/", response_model=ApiResponse[RouteInDB], summary="Create a new route")
async def add_route(route: RouteCreate, user=Depends(get_current_user)):
    """
    Create a new route with the provided details.
    """
    new_route = create_route(route)
    return {
        "statusCode": 200,
        "status": "SUCCESS",
        "message": "Route created successfully",
        "data": new_route,
    }

@router.put("/{route_id}", response_model=ApiResponse[RouteInDB], summary="Update a route")
async def edit_route(route_id: str, route: RouteUpdate, user=Depends(get_current_user)):
    """
    Update an existing route by its ID.
    """
    updated_route = update_route(route_id, route)
    if not updated_route:
        raise HTTPException(status_code=404, detail="Route not found")
    return {
        "statusCode": 200,
        "status": "SUCCESS",
        "message": "Route updated successfully",
        "data": updated_route,
    }

@router.patch("/{route_id}/status", response_model=ApiResponse[RouteInDB], summary="Toggle route status")
async def change_status(route_id: str, user=Depends(get_current_user)):
    """
    Toggle the status of a route (e.g., active/inactive) by its ID.
    """
    toggled_route = toggle_route_status(route_id)
    if not toggled_route:
        raise HTTPException(status_code=404, detail="Route not found")
    return {
        "statusCode": 200,
        "status": "SUCCESS",
        "message": "Route status updated",
        "data": toggled_route,
    }

@router.delete("/{route_id}", response_model=ApiResponse[None], summary="Delete a route")
async def remove_route(route_id: str, user=Depends(get_current_user)):
    """
    Delete a route by its ID.
    """
    deleted = delete_route(route_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Route not found")
    return {
        "statusCode": 200,
        "status": "SUCCESS",
        "message": "Route deleted successfully",
        "data": None
    }