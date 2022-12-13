import enum
import datetime

from app.db.base import Base

from sqlalchemy import Column, Integer, Enum, ForeignKey, DateTime, String, BigInteger
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from uuid import uuid4


class SubFieldOrder(Base):
    __tablename__ = "subfield_order"
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        index=True,
        default=uuid4
    )
    value = Column(String, nullable=True)
    order_id = Column(
        UUID(as_uuid=True),
        ForeignKey("order.id"),
        index=True
    )
    order = relationship("Order", lazy='joined', backref="subfields")

    def __str__(self) -> str:
        return f"{self.id}"
