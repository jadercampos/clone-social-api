from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class InfluencerBase(BaseModel):
    name: str
    username: str
    email: Optional[EmailStr] = None
    avatar_url: Optional[str] = None

class InfluencerCreate(InfluencerBase):
    pass

class InfluencerUpdate(InfluencerBase):
    pass

class InfluencerRead(InfluencerBase):
    id: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True  # se estiver no Pydantic v2 (ex: pydantic-settings)
