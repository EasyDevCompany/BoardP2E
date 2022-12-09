import datetime

from app.db.base_class import Base

from sqlalchemy import (
    Column,
    ForeignKey,
    String,
    Float,
    DateTime
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from uuid import uuid4


class Review(Base):
    __tablename__ = "review"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        index=True,
        default=uuid4
    )
    text = Column(String(500), nullable=True)
    publication_date = Column(DateTime, default=datetime.datetime.utcnow)
    raiting = Column(Float(precision=1))
    author_of_review_id = Column(
        UUID(as_uuid=True),
        ForeignKey("user.id")
    )
    reviewed_user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("user.id")
    )
    deal_id = Column(
        UUID(as_uuid=True),
        ForeignKey("deal.id"),
    )
    deals = relationship("Deal")
