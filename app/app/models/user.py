import enum
import datetime

from app.db.base import Base

from sqlalchemy import Column, Integer, Enum, ForeignKey, DateTime, String, BigInteger, Float
from sqlalchemy.orm import relationship, validates
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy_imageattach.entity import Image, image_attachment

from uuid import uuid4


class User(Base):
    __tablename__ = 'user'

    class UserStatus(enum.Enum):
        user_eng = "user"
        moderator_eng = "moderator"
        admin_eng = "admin"
        user_ru = "пользователь"
        moderator_ru = "модератор"
        admin_ru = "админ"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        index=True,
        default=uuid4
    )
    login = Column(
        String,
        nullable=False,
    )
    status = Column(Enum(UserStatus))
    email = Column(String)
    balance = Column(BigInteger)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    # TODO Сделать хэш паролей
    password = Column(String(30))
    raiting = Column(Float(precision=1))
    review_amount = Column(Integer)
    image = image_attachment("UserPicture")

    @validates("email")
    def validate_email(self, key, address):
        if "@" not in address:
            raise ValueError("failed simple email validation")
        return address


class UserPicture(Base, Image):
    __tablename__ = 'user_picture'
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    user = relationship('user')
