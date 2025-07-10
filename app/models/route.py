from pydantic import BaseModel
from typing import List, Optional

class RouteBase(BaseModel):
    name: str
    from_location: str
    to_location: str
    distance_km: float
    duration_minutes: int
    fare: float
    stops: List[str]
    status: Optional[str] = "active"

class RouteCreate(RouteBase):
    pass

class RouteUpdate(BaseModel):
    name: Optional[str]
    from_location: Optional[str]
    to_location: Optional[str]
    distance_km: Optional[float]
    duration_minutes: Optional[int]
    fare: Optional[float]
    stops: Optional[List[str]]
    status: Optional[str]

class RouteInDB(RouteBase):
    id: str