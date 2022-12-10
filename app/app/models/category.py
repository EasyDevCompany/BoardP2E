from app.db.base import Base

from sqlalchemy import Column, Integer, Enum, ForeignKey, DateTime, String, BigInteger
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from uuid import uuid4


class Category(Base):
    __tablename__ = 'category'
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        index=True,
        default=uuid4
    )
    name_of_currency_eng = Column(String, nullable=False)
    game_id = Column('game_id', UUID(as_uuid=True), ForeignKey('game.id'), primary_key=True)
    game = relationship(
        "Game",
        back_populates="game"
    )

    def __str__(self) -> str:
        return f"{self.id}"
