from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId

class BusBase(BaseModel):
    bus_number: str
    model: str
    capacity: int
    seat_layout: str
    driver_name: str
    conductor_name: str
    assigned_route: Optional[str] = None
    status: str

class BusCreate(BusBase):
    pass

class BusUpdate(BusBase):
    pass

class BusInDB(BusBase):
    id: str = Field(alias="_id")

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

from pydantic import BaseModel

class BusInDB(BaseModel):
    bus_number: str
    model: str
    capacity: int
    seat_layout: str
    driver_name: str
    conductor_name: str
    assigned_route: str
    status: str