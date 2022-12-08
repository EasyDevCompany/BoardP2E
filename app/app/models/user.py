from app.db.base_class import Base
from sqlalchemy import (
    Column,
    BigInteger,
    Integer,
    DateTime,
    Enum,
    String,
)

import enum
import datetime


class User(Base):
    __tablename__ = "user"

    class UserType(str, enum.Enum):
        admin = "admin"
        default_user = "default_user"
        redactor = "redactor"

    class UserRole(str, enum.Enum):
        seller = "seller"
        buyer = "buyer"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(70))
    first_name = Column(String(70))
    last_name = Column(String(70))
    email = Column(String(50), unique=True)
    registration_date = Column(DateTime, default=datetime.datetime.utcnow())
    user_type = Column(Enum(UserType))
    user_role = Column(Enum(UserRole))

    def __repr__(self):
        return f"user: {self.username} email: {self.email}"