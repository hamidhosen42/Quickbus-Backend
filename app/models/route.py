from pydantic import BaseModel, Field
from typing import List, Optional, Generic, TypeVar
from pydantic.generics import GenericModel

T = TypeVar("T")  # Generic type for data field

# Shared base for route input
class RouteBase(BaseModel):
    name: str = Field(..., example="City Centre Express")
    from_location: str = Field(..., example="City Centre")
    to_location: str = Field(..., example="Airport")
    distance_km: float = Field(..., example=25.0)
    duration_minutes: int = Field(..., example=45)
    fare: float = Field(..., example=150.0)
    stops: List[str] = Field(..., example=["Central Mall", "Tech Park", "Hospital", "Airport"])
    status: Optional[str] = Field(default="active", example="active")

# For creating a new route
class RouteCreate(RouteBase):
    pass

# For updating an existing route (partial fields allowed)
class RouteUpdate(BaseModel):
    name: Optional[str] = None
    from_location: Optional[str] = None
    to_location: Optional[str] = None
    distance_km: Optional[float] = None
    duration_minutes: Optional[int] = None
    fare: Optional[float] = None
    stops: Optional[List[str]] = None
    status: Optional[str] = None

# Output format (includes id)
class RouteInDB(RouteBase):
    id: str = Field(..., example="uuid-string-1234")

class ApiResponse(GenericModel, Generic[T]):
    statusCode: int
    status: str
    message: str
    data: T