# app/core/dependencies.py

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from app.db.mongo import db
import os

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")
SECRET_KEY = os.getenv("JWT_SECRET", "secret")
ALGORITHM = "HS256"

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        user = await db.users.find_one({"username": username})
        if not user:
            raise HTTPException(status_code=401, detail="User not found")
        return user
    except JWTError:
        raise HTTPException(status_code=403, detail="Token verification failed")