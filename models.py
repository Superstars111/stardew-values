from sqlalchemy import Column, Integer, String, ForeignKey, Table, Boolean, Text
from sqlalchemy.orm import relationship, backref
from app import db


class Crop(db.Model):
    __tablename__ = "crops"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    seed_cost = Column(Integer)
    maturation_days = Column(Integer)
    base_value = Column(Integer)
    silver_value = Column(Integer)
    gold_value = Column(Integer)
    iridium_value = Column(Integer)
    wine_id = Column(Integer, ForeignKey("wines.id"), unique=True)
    preserve_id = Column(Integer, ForeignKey("preserves.id"), unique=True)

    def net_values(self):
        if self.base_value:
            silver_net = self.silver_value - self.base_value
        else:
            silver_net = self.silver_value

        if self.silver_value:
            gold_net = self.gold_value - self.silver_value
        elif self.base_value:
            gold_net = self.gold_value - self.base_value
        else:
            gold_net = self.gold_value

        if self.gold_value:
            iridium_net = self.iridium_value - self.gold_value
        elif self.silver_value:
            iridium_net = self.iridium_value - self.silver_value
        elif self.base_value:
            iridium_net = self.iridium_value - self.base_value
        else:
            iridium_net = self.iridium_value

        return silver_net, gold_net, iridium_net


class Wine(db.Model):
    __tablename__ = "wines"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    production_days = Column(Integer)
    base_value = Column(Integer)
    silver_value = Column(Integer)
    gold_value = Column(Integer)
    iridium_value = Column(Integer)
    crop_id = Column(Integer, ForeignKey("crops.id"), unique=True)

    def net_values(self):
        if self.base_value:
            silver_net = self.silver_value - self.base_value
        else:
            silver_net = self.silver_value

        if self.silver_value:
            gold_net = self.gold_value - self.silver_value
        elif self.base_value:
            gold_net = self.gold_value - self.base_value
        else:
            gold_net = self.gold_value

        if self.gold_value:
            iridium_net = self.iridium_value - self.gold_value
        elif self.silver_value:
            iridium_net = self.iridium_value - self.silver_value
        elif self.base_value:
            iridium_net = self.iridium_value - self.base_value
        else:
            iridium_net = self.iridium_value

        return silver_net, gold_net, iridium_net


class Preserve(db.Model):
    __tablename__ = "preserves"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    production_days = Column(Integer)
    base_value = Column(Integer)
    silver_value = Column(Integer)
    gold_value = Column(Integer)
    iridium_value = Column(Integer)
    crop_id = Column(Integer, ForeignKey("crops.id"), unique=True)
