from fastapi import APIRouter, HTTPException, Depends, status
from pydantic import BaseModel
from app.db import db
from app.core.security import verify_password, create_access_token, hash_password
from datetime import datetime

router = APIRouter()

def now():
    return datetime.utcnow().isoformat()

# Request Models
class LoginRequest(BaseModel):
    username: str
    password: str

class SignUpRequest(BaseModel):
    username: str
    password: str
    full_name: str
    role: str = "STAFF"

# 🚀 Signup
@router.post("/signup")
async def signup(payload: SignUpRequest):
    existing_user = await db["users"].find_one({"username": payload.username})  # Corrected line
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    hashed = hash_password(payload.password)

    user_data = {
        "username": payload.username,
        "full_name": payload.full_name,
        "password": hashed,
        "role": payload.role
    }

    await db["users"].insert_one(user_data)  # Corrected line

    return {
        "statusCode": 201,
        "time": now(),
        "message": "User registered successfully",
        "status": "SUCCESS",
        "data": {
            "userName": payload.username,
            "name": payload.full_name,
            "userRole": payload.role
        }
    }

# 🚀 Login
@router.post("/login")
async def login(data: LoginRequest):
    db_user = await db["users"].find_one({"username": data.username})  # Corrected line
    if not db_user or not verify_password(data.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": db_user["username"]})

    return {
        "statusCode": 200,
        "time": now(),
        "message": "Login successful",
        "status": "SUCCESS",
        "data": {
            "token": token,
            "userName": db_user["username"],
            "name": db_user["full_name"],
            "userRole": db_user.get("role", "")
        }
    }

# 🚀 Get Profile
@router.get("/me")
async def get_me(current_user=Depends()):
    return {
        "statusCode": 200,
        "time": now(),
        "message": "User fetched successfully",
        "status": "SUCCESS",
        "data": {
            "userName": current_user["username"],
            "name": current_user.get("full_name", ""),
            "userRole": current_user.get("role", "")
        }
    }