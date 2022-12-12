from fastapi import HTTPException, status
from jose import jwt
from passlib.context import CryptContext
from app.models.user import User
from loguru import logger
from app.core.config import settings
from app.schemas.auth import RegUserIn
from app.repository.user import RepositoryUser


class UserService:

    def __init__(
            self,
            repository_user: RepositoryUser,
    ):
        self._repository_user = repository_user
