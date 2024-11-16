from fastapi.security.api_key import APIKeyCookie
from fastapi import HTTPException, status

from jose import jwt
from passlib.context import CryptContext
from datetime import timedelta, datetime
from typing import Annotated
from db import get_user_from_db, check_exist

secret_key = 'ifuioeruoiwurioewurioweuoiruewoi'
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_HOUR = 24


get_cookie = APIKeyCookie(name='auth_cookie')
password_hash = CryptContext(schemes='bcrypt', deprecated="auto")


def create_token(data: dict,):
    user = data.copy()
    expire = datetime.utcnow() + timedelta(hours=ACCESS_TOKEN_EXPIRE_HOUR)
    user.update({'exp': expire})
    encoded_jwt = jwt.encode(claims=user, key=secret_key, algorithm=ALGORITHM )
    return encoded_jwt


def verify_password(password, db_password):
    if password_hash.verify(password,db_password):
        return True


def authenticate_form_db(username: object, password: object) -> object:
    db_data = get_user_from_db(username)
    if not db_data:
        return False
    if not verify_password(password, db_data['hashed_pass']):
        return False
    return True


def current_user(token: Annotated[str, get_cookie ]):
    if not token:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    try:
        encoded_token = jwt.decode(token=token, algorithms=ALGORITHM, key=secret_key)
    except HTTPException:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    username = encoded_token.get('sub')
    print('####', username)
    return check_exist(username)


