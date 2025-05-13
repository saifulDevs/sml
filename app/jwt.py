import jwt
import os
from datetime import datetime, timedelta
from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from typing import Optional
from fastapi import Depends

SECRET_KEY = os.getenv("SECRET_KEY", "mysecretkey")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
   if expires_delta:
       expire = datetime.utcnow() + expires_delta
   else:
       expire = datetime.utcnow() + timedelta(minutes=15)
   to_encode = data.copy()
   to_encode.update({"exp": expire})
   encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
   return encoded_jwt

def verify_token(token: str = Depends(oauth2_scheme)):
   try:
       payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
       return payload
   except jwt.PyJWTError:
       raise HTTPException(
           status_code=status.HTTP_401_UNAUTHORIZED,
           detail="Invalid token",
       )