from datetime import datetime, timezone
from typing import Union
from uuid import uuid4

from pydantic import BaseModel, EmailStr, Field


class Customer(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()), alias="_id")
    firstName: str
    lastName: str
    email: EmailStr
    cpf: str
    createdAt: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updatedAt: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    lastPurchaseAt: Union[datetime, None] = None
    birthDate: Union[datetime, None] = None
    phoneNumber: Union[str, None] = None
