import enum
import datetime

from uuid import uuid4

from sqlalchemy import Column, Integer, Enum, ForeignKey, DateTime, String, BigInteger, Float, LargeBinary
from sqlalchemy.orm import relationship, validates
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy_imageattach.entity import Image, image_attachment

from app.db.base import Base
from app.utils.bytes_field import HexByteString


class User(Base):
    __tablename__ = 'user'

    class UserStatus(str, enum.Enum):
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
        String(15),
        nullable=False,
        unique=True
    )
    status = Column(Enum(UserStatus), default=UserStatus.user_ru)
    email = Column(String)
    balance = Column(BigInteger, default=0)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    # TODO Сделать хэш паролей
    password = Column(HexByteString)
    salt = Column(HexByteString)
    raiting = Column(Float(precision=1), default=0)
    review_amount = Column(Integer, default=0)
    image = image_attachment("UserPicture")


class UserPicture(Base, Image):
    __tablename__ = 'user_picture'
    user_id = Column(UUID(as_uuid=True), ForeignKey('user.id'), primary_key=True)
    user = relationship('user')


class UserToken(Base):
    __tablename__ = 'user_token'

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey('user.id'), primary_key=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)



