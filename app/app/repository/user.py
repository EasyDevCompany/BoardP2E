from .base import RepositoryBase
from app.models.user import User
from app.models.user import UserToken


class RepositoryUser(RepositoryBase[User]):
    pass


class RepositoryUserToken(RepositoryBase[UserToken]):
    pass

