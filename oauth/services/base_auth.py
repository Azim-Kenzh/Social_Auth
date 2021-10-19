
from datetime import timedelta, datetime

import jwt

from core import settings


def create_token(user_id: int) -> dict:
    """Создание Токена"""
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        'user_id': user_id,
        'access_token': create_access_token(
            data={'user_id': user_id}, exires_delta=access_token_expires
        ),
        'token_type': 'Token'
    }


def create_access_token(data: dict, exires_delta: timedelta = None): #или можно указать timedelta =  15
    """Создание аксес токена"""
    to_encode = data.copy()
    if exires_delta is not None:
        expire = datetime.utcnow() + exires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({'exp': expire, 'sub': 'access'})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt
