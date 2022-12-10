import hashlib
import hmac
import secrets

from loguru import logger
from fastapi import Header, Depends, Response, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from dependency_injector.wiring import inject, Provide
from app.core.containers import Container
from functools import wraps
from app.db.session import scope
from uuid import uuid4, UUID

from app.repository.user import RepositoryUser

security = HTTPBasic()


@inject
def get_current_user_auth(
        credentials: HTTPBasicCredentials = Depends(security),
        rep_user: RepositoryUser = Depends(Provide[Container.repository_user])

):
    current_username_bytes = credentials.username
    logger.info(f"{current_username_bytes}")
    current_password_bytes = credentials.password
    logger.info(f"{current_password_bytes}")
    user = rep_user.get(login=current_username_bytes)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неправильный логин или пароль!",
            headers={"WWW-Authenticate": "Basic"},
        )
    hashed_current_password = hashlib.pbkdf2_hmac(
        hash_name="sha256",
        password=current_password_bytes,
        salt=user.salt,
        iterations=100_000
    )
    is_correct_username = secrets.compare_digest(
        user.login, current_username_bytes
    )
    is_correct_password = hmac.compare_digest(
        user.password, hashed_current_password
    )
    if not (is_correct_password and is_correct_username):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неправильный логин или пароль!",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


@inject
async def create_session():
    scope.set(str(uuid4()))


@inject
def commit_and_close_session(func):

    @wraps(func)
    @inject
    async def wrapper(db=Depends(Provide[Container.db]), *args, **kwargs,):
        scope.set(str(uuid4()))
        try:
            result = await func(*args, **kwargs)
            db.session.commit()
            return result
        except Exception as e:
            db.session.rollback()
            raise e
        finally:
            # db.session.expunge_all()
            db.scoped_session.remove()

    return wrapper
