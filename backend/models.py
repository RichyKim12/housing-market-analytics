from database import Base
from sqlalchemy import Integer, String, Date, Numeric, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date


class DimRegion(Base):
    __tablename__ = "dim_region"
    region_id: Mapped[int] = mapped_column(Integer, primary_key = True)
    size_rank: Mapped[int | None] = mapped_column(Integer, nullable=True)
    region_name: Mapped[str | None] = mapped_column(String(100))
    region_type: Mapped[str] = mapped_column(String(50))	
    state_name: Mapped[str | None] = mapped_column(String(50), nullable=True)


class FactHomeValues(Base):
    __tablename__ = "fact_home_values"
    region_id: Mapped[int] = mapped_column(Integer, ForeignKey("dim_region.region_id"), primary_key=True)
    date: Mapped[date] = mapped_column(Date, primary_key=True)
    value: Mapped[float | None] = mapped_column(Numeric)
