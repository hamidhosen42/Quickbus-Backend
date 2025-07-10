# app/services/route_service.py
from app.db.mongo import db
from app.models.route import RouteCreate, RouteUpdate, RouteInDB
from bson import ObjectId

def get_all_routes():
    routes = db.routes.find()
    return [RouteInDB(**r, id=str(r["_id"])) for r in routes]

def create_route(route: RouteCreate):
    route_dict = route.dict()
    result = db.routes.insert_one(route_dict)
    return RouteInDB(**route_dict, id=str(result.inserted_id))

def update_route(route_id: str, route: RouteUpdate):
    db.routes.update_one({"_id": ObjectId(route_id)}, {"$set": route.dict(exclude_unset=True)})
    updated = db.routes.find_one({"_id": ObjectId(route_id)})
    return RouteInDB(**updated, id=str(route_id))

def toggle_route_status(route_id: str):
    route = db.routes.find_one({"_id": ObjectId(route_id)})
    new_status = "inactive" if route["status"] == "active" else "active"
    db.routes.update_one({"_id": ObjectId(route_id)}, {"$set": {"status": new_status}})
    updated = db.routes.find_one({"_id": ObjectId(route_id)})
    return RouteInDB(**updated, id=str(route_id))

def delete_route(route_id: str):
    db.routes.delete_one({"_id": ObjectId(route_id)})