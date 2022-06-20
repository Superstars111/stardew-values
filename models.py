from sqlalchemy import Column, Integer, String, ForeignKey, Table, Boolean, Text
from sqlalchemy.orm import relationship, backref
from app import db


class Crop(db.Model):
    __tablename__ = "crops"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)
    seed_cost = Column(Integer)
    maturation_days = Column(Integer)
    base_value = Column(Integer)
    silver_value = Column(Integer)
    gold_value = Column(Integer)
    iridium_value = Column(Integer)
    wine_production_days = Column(Integer)
    wine_value = Column(Integer)
    silver_wine_value = Column(Integer)
    gold_wine_value = Column(Integer)
    iridium_wine_value = Column(Integer)
    preserve_production_days = Column(Integer)
    preserve_value = Column(Integer)
    silver_preserve_value = Column(Integer)
    gold_preserve_value = Column(Integer)
    iridium_preserve_value = Column(Integer)
