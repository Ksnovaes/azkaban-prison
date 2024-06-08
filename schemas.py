from pydantic import BaseModel
from enum import Enum

class SentencasEnum(str, Enum):
    prison = 'prison'
    life_imprisionment = 'life_imprisonment'
    death = 'death'

class JuizBase(BaseModel):
    full_name: str

class JuizCreate(JuizBase):
    pass

class Juiz(JuizBase):
    id: int

    class Config:
        orm_mode: True



class SentenciadoBase(BaseModel):
    name: str
    felony: str
    sentence: SentencasEnum

class SentenciadoCreate(SentenciadoBase):
    pass

class Sentenciado(SentenciadoBase):
    id: int

    class Config:
        orm_mode: True

