from sqlalchemy import Column, Integer, String, Float, Enum
import enum

from database import Base

class EspecieEnum(enum.Enum):
    perro = "perro"
    gato = "gato"

class RazaEnum(enum.Enum):
    criollo = "criollo"
    fino = "fino"

class Animals(Base):
    __tablename__ = "animales"
    id = Column(Integer, primary_key=True, index=True)
    especie = Column(Enum(EspecieEnum), nullable=False)
    raza = Column(Enum(RazaEnum), nullable=False)
    nombre = Column(String(255), nullable=False)
    edad = Column(Integer, nullable=False)
    peso = Column(Float, nullable=False)
