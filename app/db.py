# app/db.py
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os
import urllib.parse
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()
username = os.getenv("MONGO_USERNAME")
password = urllib.parse.quote_plus(os.getenv("MONGO_PASSWORD"))

MONGO_URI = (
    f"mongodb+srv://{username}:{password}"
    "@quickbus.6xdyrjc.mongodb.net/?retryWrites=true&w=majority&appName=quickbus"
)

try:
    client = AsyncIOMotorClient(
        MONGO_URI,
        tls=True,
        tlsAllowInvalidCertificates=False,
        serverSelectionTimeoutMS=30000
    )
    logger.info("Connected to MongoDB with URI: %s", MONGO_URI)
    db = client["quickbus"]
    # Test connection
    client.admin.command('ping')
except Exception as e:
    logger.error("Failed to connect to MongoDB: %s", e)
    raise