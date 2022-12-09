import enum
import datetime

from app.db.base import Base

from sqlalchemy import Column, Integer, Enum, ForeignKey, DateTime, String, BigInteger
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy_imageattach.entity import Image, image_attachment

from uuid import uuid4

from app.models.base_order import BaseOrder


class BaseDeal(BaseOrder):
    __tablename__ = "deal"

    class DealStatus(enum.Enum):
        active = "active"
        archived = "archived"
        draft = "draft"
        deleted = "deleted"

    amount_of_selling_item = Column(BigInteger)
    price_for_one_cyptocurrency = Column(BigInteger)
    view_amount = Column(BigInteger, default=0)
    author_of_deal_id = Column(
        UUID(as_uuid=True),
        ForeignKey("user.id"),
        index=True
    )
    author_of_deal = relationship("User", lazy='joined')
    status = Column(Enum(DealStatus))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    def __str__(self) -> str:
        return f"{self.id}"
