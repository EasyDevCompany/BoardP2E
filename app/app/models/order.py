import enum
import datetime

from app.db.base import Base

from sqlalchemy import Column, Integer, Enum, ForeignKey, DateTime, String, BigInteger
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy_imageattach.entity import Image, image_attachment

from uuid import uuid4


class Order(Base):
    __tablename__ = "order"

    class OrderStatus(enum.Enum):
        active_eng = "active"
        archived_eng = "archived"
        draft_eng = "draft"
        deleted_eng = "deleted"
        active_ru = "активная"
        archived_ru = "архивированная"
        draft_ru = "черновая"
        deleted_ru = "удаленная"

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
    status = Column(Enum(OrderStatus))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    def __str__(self) -> str:
        return f"{self.id}"
