from app.db.base_class import Base
from sqlalchemy import Column, Integer, Enum, ForeignKey, DateTime, String, BigInteger
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from uuid import uuid4
import datetime
import enum


class Deal(Base):
    __tablename__ = "deal"

    class DealStatus(str, enum.Enum):
        created_waiting_to_transfer = "created_waiting_to_transfer"
        waiting_for_transfer_confirmation = "waiting_for_confirmation"
        confirmed = "confirmed"
        cancelled = "cancelled"

        controversial_situation = "controversial_situation"
        decided_in_favor_of_the_buyer = "decided_in_favor_of_the_buyer"
        decided_in_favor_of_the_seller = "decided_in_favor_of_the_seller"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        index=True,
        default=uuid4
    )
    last_update = Column(DateTime,  onupdate=datetime.datetime.utcnow, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    # Какое колличество денег нужно снять с кошелька продавца.
    # Высчитывается через колличество покупаемых предметов * цена за один элемент
    count_of_money = Column(Integer)
    # Какое колличетсов элементов покупается
    currency_count = Column(BigInteger)
    status = Column(Enum(DealStatus))

    buyer_id = Column(
        UUID(as_uuid=True), ForeignKey("user.id") # покупатель
    )
    seller_id = Column(
        UUID(as_uuid=True), ForeignKey("user.id") # продавец
    )
    order_id = Column(UUID(as_uuid=True), ForeignKey("order.id"))
    buyer = relationship("User", foreign_keys=[buyer_id])
    seller = relationship("User", foreign_keys=[seller_id])
    order = relationship("Order")
