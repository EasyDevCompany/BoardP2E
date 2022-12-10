from app.db.base import Base

from sqlalchemy import Column, Integer, Enum, ForeignKey, DateTime, String, BigInteger
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

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
    description_eng = Column(String, nullable=True)
    description_ru = Column(String, nullable=True)
    view_amount = Column(BigInteger, default=0)
    image_name = Column(String, nullable=True)

    def __str__(self) -> str:
        return f"{self.id}"
