import hmac
import os
import hashlib
from typing import Tuple

from app.repository.user import RepositoryUser
from app.models.user import User

from app.schemas.auth import RegUserIn


class RegistrationService:

    def __init__(
            self,
            repository_user: RepositoryUser,
    ):
        self._repository_user = repository_user

    @staticmethod
    def _hash_password(password: str) -> Tuple[bytes, bytes]:
        salt = os.urandom(16)
        hashed_password = hashlib.pbkdf2_hmac(
            hash_name='sha256',
            password=password.encode('utf-8'),
            salt=salt,
            iterations=100_000
        )

        return salt, hashed_password

    async def _send_ver_code(self):
        pass

    async def registration_user(self, user: RegUserIn):
        salt, hashed_password = self._hash_password(password=user.password)
        obj_in = {
            "login": user.login,
            "status": User.UserStatus.user_ru,
            "email": user.email,
            "password": hashed_password,
            "salt": salt,
        }
        # TODO изменить ошибки
        if self._repository_user.get(email=user.email):
            raise ValueError("Такой email уже зарегистрирован")
        if self._repository_user.get("login"):
            raise ValueError("Такой login уже зарегистрирован!")

        if user.image is not None:
            obj_in.update({"image": user.image})

        return self._repository_user.create(obj_in=obj_in)

    async def my_profile(self, user_id):
        return self._repository_user.get(id=user_id)
