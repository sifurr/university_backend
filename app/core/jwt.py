from datetime import datetime, timedelta
from jose import jwt, JWTError
from app.core.config import settings


ALGORITHM = "HS256"


def create_access_token(data: dict):
    """_
    Create short-lived access token
    """
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({"exp": expire})

    return jwt.encode(
        to_encode,
        settings.SECRET_KEY, 
        algorithm=ALGORITHM
    )


def create_refresh_token(data: dict):
    """
     Create long-lived refresh token.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(
        days=settings.REFRESH_TOKEN_EXPIRE_DAYs
    )

    to_encode.update({"exp": expire})

    return jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=ALGORITHM
    )


def decode_token(token: str):
    """
    Decode and validate JWT
    """
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        return payload
    except JWTError:
        return None
    