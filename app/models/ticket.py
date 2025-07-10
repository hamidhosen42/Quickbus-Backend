from pydantic import BaseModel, Field
from typing import Optional

class Ticket(BaseModel):
    route: str
    bus_id: str
    seat_no: str
    passenger_name: Optional[str] = None
    payment_mode: str
    departure_time: str
    used: bool = False

class TicketInDB(Ticket):
    id: str = Field(default_factory=str)