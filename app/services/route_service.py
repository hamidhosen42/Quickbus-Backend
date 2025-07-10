from typing import List, Optional
from uuid import uuid4
from app.models.route import RouteCreate, RouteInDB, RouteUpdate

# In-memory storage for demonstration purposes
routes_db: List[RouteInDB] = []

def get_all_routes() -> List[RouteInDB]:
    return routes_db

def create_route(route: RouteCreate) -> RouteInDB:
    new_route = RouteInDB(id=str(uuid4()), **route.dict())
    routes_db.append(new_route)
    return new_route

def update_route(route_id: str, route: RouteUpdate) -> Optional[RouteInDB]:
    for index, existing_route in enumerate(routes_db):
        if existing_route.id == route_id:
            updated_data = existing_route.dict()
            update_fields = route.dict(exclude_unset=True)
            updated_data.update(update_fields)
            updated_route = RouteInDB(**updated_data)
            routes_db[index] = updated_route
            return updated_route
    return None

def toggle_route_status(route_id: str) -> Optional[RouteInDB]:
    for index, route in enumerate(routes_db):
        if route.id == route_id:
            new_status = "inactive" if route.status == "active" else "active"
            updated_route = route.copy(update={"status": new_status})
            routes_db[index] = updated_route
            return updated_route
    return None

def delete_route(route_id: str) -> bool:
    global routes_db
    original_len = len(routes_db)
    routes_db = [r for r in routes_db if r.id != route_id]
    return len(routes_db) != original_len
