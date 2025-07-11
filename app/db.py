# app/db.py
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os
import urllib.parse

# Load environment variables
load_dotenv()

username = os.getenv("MONGO_USERNAME")
password = urllib.parse.quote_plus(os.getenv("MONGO_PASSWORD"))

MONGO_URI = (
    f"mongodb+srv://{username}:{password}"
    "@quickbus.6xdyrjc.mongodb.net/?retryWrites=true&w=majority&appName=quickbus"
)

# Initialize MongoDB client
client = AsyncIOMotorClient(MONGO_URI)
db = client["quickbus"]