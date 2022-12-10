import enum
import datetime

from app.db.base import Base

from sqlalchemy import Column, Integer, Enum, ForeignKey, DateTime, String, BigInteger
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from uuid import uuid4


class Order(Base):
    __tablename__ = "order"

    class OrderStatus(str, enum.Enum):
        active = {"ru": "активная", "eng": "active"}
        archived = {"ru": "архивированная", "eng": "archived"}
        draft = {"ru": "черновая", "eng": "draft"}
        deleted = {"ru": "удаленная", "eng": "deleted"}

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        index=True,
        default=uuid4
    )
    amount_of_selling_item = Column(BigInteger)
    price_for_one_currency = Column(BigInteger)
    view_amount = Column(BigInteger, default=0)
    server_eng = Column(String, nullable=True)
    side_eng = Column(String, nullable=True)
    description_eng = Column(String, nullable=True)
    name_of_currency_ru = Column(String, nullable=True,)
    server_ru = Column(String, nullable=True)
    side_ru = Column(String, nullable=True)
    description_ru = Column(String, nullable=True)
    author_of_deal_id = Column(
        UUID(as_uuid=True),
        ForeignKey("user.id"),
        index=True
    )
    category = Column(
        UUID(as_uuid=True),
        ForeignKey("category.id"),
        index=True
    )
    author_of_deal = relationship("User", lazy='joined')
    category = relationship("Category", lazy="joined")
    status = Column(Enum(OrderStatus), default=OrderStatus.archived)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    def __str__(self) -> str:
        return f"{self.id}"
