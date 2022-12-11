from fastapi import HTTPException, status
from jose import jwt
from passlib.context import CryptContext
from app.models.user import User
from loguru import logger
from app.core.config import settings
from app.schemas.auth import RegUserIn
from app.repository.user import RepositoryUser

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class AuthService:
    ALGORITHM = "HS256"
    SECRET_KEY = settings.SECRET_KEY

    def __init__(
            self,
            repository_user: RepositoryUser,
    ):
        self._repository_user = repository_user

    def create_access_token(self, data: dict):
        to_encode = data.copy()
        encoded_jwt = jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)

        return encoded_jwt

    def _get_password_hash(self, password):
        return pwd_context.hash(password)

    def verify_password(self, input_password, hashed_password):
        return pwd_context.verify(input_password, hashed_password)

    async def registration(self, user: RegUserIn):
        user_login = self._repository_user.get(login=user.login)
        user_email = self._repository_user.get(email=user.email)
        if user_email is not None:
            raise ValueError("Такой email уже зарегистрирован.")
        if user_login is not None:
            raise ValueError("Такой логин уже зарегистрирован.")
        hashed_password = self._get_password_hash(password=user.password)
        access_token = self.create_access_token(data={"login": user.login})
        obj_in = {
            "token": access_token,
            "login": user.login,
            "email": user.email,
            "password": hashed_password,
            "secret_key": "secret"
        }
        logger.info(obj_in)
        return self._repository_user.create(obj_in=obj_in)

    async def login(self, form_data):
        credentials_exception = HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        user = self._repository_user.get(login=form_data.username)
        if not user:
            raise credentials_exception
        if not self.verify_password(
            input_password=form_data.password,
            hashed_password=user.password
        ):
            raise credentials_exception

        access_token = self.create_access_token(
            data={"login": user.login}
        )
        logger.info(access_token)
        return {"access_token": access_token, "token_type": "bearer"}

    # async def my_profile(self, user_id):
        # return self._repository_user.get(id=user_id)
