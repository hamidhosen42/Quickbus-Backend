# app/api/route.py
from fastapi import APIRouter, HTTPException, Depends
from app.models.route import RouteCreate, RouteInDB, RouteUpdate
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

@router.get("/", response_model=List[RouteInDB])
def list_routes():
    return get_all_routes()

@router.post("/", response_model=RouteInDB)
def add_route(route: RouteCreate, user=Depends(get_current_user)):
    return create_route(route)

@router.put("/{route_id}", response_model=RouteInDB)
def edit_route(route_id: str, route: RouteUpdate, user=Depends(get_current_user)):
    return update_route(route_id, route)

@router.patch("/{route_id}/status", response_model=RouteInDB)
def change_status(route_id: str, user=Depends(get_current_user)):
    return toggle_route_status(route_id)

@router.delete("/{route_id}")
def remove_route(route_id: str, user=Depends(get_current_user)):
    delete_route(route_id)
    return {"message": "Route deleted successfully"}