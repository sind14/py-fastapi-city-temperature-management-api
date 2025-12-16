from datetime import datetime, timezone

from sqlalchemy import Column, Integer, ForeignKey, DateTime, Float

from settings import Base


class Temperature(Base):
    __tablename__ = "temperature"
    id = Column(Integer, primary_key=True)
    city_id = Column(Integer, ForeignKey("city.id"), nullable=False)
    date_time = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False)
    temperature = Column(Float, nullable=False)
