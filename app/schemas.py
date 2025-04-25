import uuid
from typing import Optional, List, Any
from pydantic import BaseModel, EmailStr
import datetime

class UserBase(BaseModel):
    email: EmailStr
    name: str
    avatar_url: Optional[str]
    user_type: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: uuid.UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    class Config:
        orm_mode = True

class MentorBase(BaseModel):
    title: Optional[str]
    bio: Optional[str]
    rating: Optional[float]
    review_count: Optional[int]
    hourly_rate: Optional[int]
    qualifications: Optional[Any]
    is_verified: Optional[bool]
    ai_profile_vector: Optional[Any]

class MentorCreate(MentorBase):
    user_id: uuid.UUID

class Mentor(MentorBase):
    user_id: uuid.UUID
    class Config:
        orm_mode = True

class MenteeBase(BaseModel):
    bio: Optional[str]
    interests: Optional[List[int]]
    ai_profile_vector: Optional[Any]

class MenteeCreate(MenteeBase):
    user_id: uuid.UUID

class Mentee(MenteeBase):
    user_id: uuid.UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    class Config:
        orm_mode = True

# Add similar schemas for other tables as needed
