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

class InterestBase(BaseModel):
    name: str
    category: str

class InterestCreate(InterestBase):
    pass

class Interest(InterestBase):
    id: int
    class Config:
        orm_mode = True

class MentorInterestBase(BaseModel):
    mentor_id: uuid.UUID
    interest_id: int

class MentorInterestCreate(MentorInterestBase):
    pass

class MentorInterest(MentorInterestBase):
    class Config:
        orm_mode = True

class MentorshipBase(BaseModel):
    mentor_id: uuid.UUID
    mentee_id: uuid.UUID
    status: str
    started_at: Optional[datetime.datetime]
    ended_at: Optional[datetime.datetime]
    ai_notes: Optional[Any]

class MentorshipCreate(MentorshipBase):
    pass

class Mentorship(MentorshipBase):
    id: uuid.UUID
    class Config:
        orm_mode = True

class SessionBase(BaseModel):
    mentorship_id: uuid.UUID
    scheduled_at: datetime.datetime
    duration_minutes: int
    notes: Optional[str]
    ai_summary: Optional[Any]

class SessionCreate(SessionBase):
    pass

class Session(SessionBase):
    id: uuid.UUID
    class Config:
        orm_mode = True

class ReviewBase(BaseModel):
    mentorship_id: uuid.UUID
    reviewer_id: uuid.UUID
    rating: int
    comment: Optional[str]

class ReviewCreate(ReviewBase):
    pass

class Review(ReviewBase):
    id: uuid.UUID
    created_at: datetime.datetime
    class Config:
        orm_mode = True

class JobBase(BaseModel):
    title: str
    description: str
    company: str
    posted_by: uuid.UUID

class JobCreate(JobBase):
    pass

class Job(JobBase):
    id: int
    created_at: datetime.datetime
    class Config:
        orm_mode = True

class AIMessageBase(BaseModel):
    mentorship_id: Optional[uuid.UUID]
    sender_id: Optional[uuid.UUID]
    message: str
    message_type: str
    ai_metadata: Optional[Any]

class AIMessageCreate(AIMessageBase):
    pass

class AIMessage(AIMessageBase):
    id: uuid.UUID
    created_at: datetime.datetime
    class Config:
        orm_mode = True
