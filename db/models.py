from sqlalchemy import Column, Integer, String, Enum
from db.database import Base
from enum import Enum as en

class Juiz(Base):
    __tablename__ = "juiz"
    id = Column(Integer, primary_key=True)
    full_name = Column(String)

class Sentencas(en):
    prison = 'prison'
    life_imprisonment = 'life_imprisonment'
    death = 'death'

class Sentenciado(Base):
    __tablename__ = "sentenciado"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    felony = Column(String)
    sentence = Column(Enum(Sentencas))

