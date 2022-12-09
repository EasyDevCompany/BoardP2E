import enum
import datetime

from app.db.base import Base

from sqlalchemy import Column, Integer, Enum, ForeignKey, DateTime, String, BigInteger
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy_imageattach.entity import Image, image_attachment

from uuid import uuid4


class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        index=True,
        default=uuid4
    )
    login = Column(String(15), nullable=False,)
    email = Column(String)
    phone_number = Column(String(12))
    text = Column(
        String(2000),
        nullable=True
    )