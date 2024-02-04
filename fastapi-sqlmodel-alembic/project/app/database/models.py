from sqlmodel import SQLModel, Field
from typing import Optional

class SongBase(SQLModel):
    name: str
    artist: str
    year: Optional[int] = None

'''Company models'''
class Company(SQLModel, table = True):
    id: int = Field(default=None, nullable=False, primary_key=True)
    name: str = Field(nullable=False)
    

class Song(SongBase, table=True):
    id: int = Field(default=None, nullable=False, primary_key=True)


class SongCreate(SongBase):
    pass