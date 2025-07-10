from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import auth, ticket, summary

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/auth")
app.include_router(ticket.router, prefix="/ticket")
app.include_router(summary.router, prefix="/summary")