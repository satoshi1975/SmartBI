from sqlmodel import SQLModel, Field
from typing import Optional
from passlib.hash import bcrypt

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    hashed_password: str

    def verify_password(self, password: str):
        return bcrypt.verify(password, self.hashed_password)
