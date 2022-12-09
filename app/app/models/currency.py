import enum
import datetime

from app.db.base import Base

from sqlalchemy import Column, Integer, Enum, ForeignKey, DateTime, String, BigInteger
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy_imageattach.entity import Image, image_attachment

from uuid import uuid4

from app.app.models.base_deal import BaseDeal


class Currency(BaseDeal):
    __tablename__ = "currency"

    category = Column(String)

    def __str__(self) -> str:
        return f"{self.id}"
