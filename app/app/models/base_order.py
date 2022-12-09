from app.db.base import Base

from sqlalchemy import Column, Integer, Enum, ForeignKey, DateTime, String, BigInteger
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy_imageattach.entity import Image, image_attachment

from uuid import uuid4


class BaseOrder(Base):
    __tablename__ = 'baseorder'
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        index=True,
        default=uuid4
    )
    name_of_currency_eng = Column(
        String,
        nullable=False,
    )
    server_eng = Column(
        String,
        nullable=False
    )
    side_eng = Column(
        String,
        nullable=False
    )
    description_eng = Column(
        String,
        nullable=False
    )
    name_of_currency_ru = Column(
        String,
        nullable=False,
    )
    server_ru = Column(
        String,
        nullable=False
    )
    side_ru = Column(
        String,
        nullable=False
    )
    description_ru = Column(
        String,
        nullable=False
    )
    game_id = Column(
        UUID(as_uuid=True),
        ForeignKey("game.id"),
    )
    game = relationship(
        "Game",
        back_populates="game"
    )

    def __str__(self) -> str:
        return f"{self.id}"
