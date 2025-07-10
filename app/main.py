from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import auth, bus, route, summary, sync, ticket

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth")
app.include_router(bus.router, prefix="/bus")
app.include_router(route.router, prefix="/route")
app.include_router(summary.router, prefix="/summary")
app.include_router(sync.router, prefix="/sync")
app.include_router(ticket.router, prefix="/ticket")