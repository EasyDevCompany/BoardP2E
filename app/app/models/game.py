from app.db.base import Base

from sqlalchemy import Column, Integer, Enum, ForeignKey, DateTime, String, BigInteger
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy_imageattach.entity import Image, image_attachment

from uuid import uuid4


class Game(Base):
    __tablename__ = 'game'

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        index=True,
        default=uuid4
    )
    name_eng = Column(
        String,
        nullable=False,
    )
    name_ru = Column(
        String,
        nullable=False,
    )
    image = image_attachment("GamePicture")
    description_eng = Column(String, nullable=True)
    description_ru = Column(String, nullable=True)
    view_amount = Column(BigInteger, default=0)

    def __str__(self) -> str:
        return f"{self.id}"


class GamePicture(Base, Image):
    __tablename__ = 'game_picture'
    game_id = Column(UUID(as_uuid=True), ForeignKey('game.id'), primary_key=True)
    user = relationship('game')
