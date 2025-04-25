import uuid
import enum
import datetime
from sqlalchemy import (
    Column, String, Enum, DateTime, ForeignKey, Integer, Float, Boolean, JSON, Table, ARRAY, Text
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class UserTypeEnum(str, enum.Enum):
    mentor = "mentor"
    mentee = "mentee"

class MentorshipStatusEnum(str, enum.Enum):
    pending = "pending"
    active = "active"
    completed = "completed"
    cancelled = "cancelled"

class MessageTypeEnum(str, enum.Enum):
    user = "user"
    ai = "ai"
    system = "system"

class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    name = Column(String, nullable=False)
    avatar_url = Column(String)
    user_type = Column(Enum(UserTypeEnum), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    mentor = relationship("Mentor", uselist=False, back_populates="user")
    mentee = relationship("Mentee", uselist=False, back_populates="user")

class Mentor(Base):
    __tablename__ = "mentors"
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), primary_key=True)
    title = Column(String)
    bio = Column(String)
    rating = Column(Float)
    review_count = Column(Integer)
    hourly_rate = Column(Integer)
    qualifications = Column(JSON)
    is_verified = Column(Boolean, default=False)
    ai_profile_vector = Column(JSON)
    user = relationship("User", back_populates="mentor")
    interests = relationship("MentorInterest", back_populates="mentor")

class Mentee(Base):
    __tablename__ = "mentees"
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), primary_key=True)
    bio = Column(String)
    interests = Column(ARRAY(Integer))
    ai_profile_vector = Column(JSON)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    user = relationship("User", back_populates="mentee")

class Interest(Base):
    __tablename__ = "interests"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    category = Column(String)

class MentorInterest(Base):
    __tablename__ = "mentor_interests"
    mentor_id = Column(UUID(as_uuid=True), ForeignKey("mentors.user_id"), primary_key=True)
    interest_id = Column(Integer, ForeignKey("interests.id"), primary_key=True)
    mentor = relationship("Mentor", back_populates="interests")
    interest = relationship("Interest")

class Mentorship(Base):
    __tablename__ = "mentorships"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    mentor_id = Column(UUID(as_uuid=True), ForeignKey("mentors.user_id"))
    mentee_id = Column(UUID(as_uuid=True), ForeignKey("mentees.user_id"))
    status = Column(Enum(MentorshipStatusEnum), default=MentorshipStatusEnum.pending)
    started_at = Column(DateTime)
    ended_at = Column(DateTime)
    ai_notes = Column(JSON)

class Session(Base):
    __tablename__ = "sessions"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    mentorship_id = Column(UUID(as_uuid=True), ForeignKey("mentorships.id"))
    scheduled_at = Column(DateTime)
    duration_minutes = Column(Integer)
    notes = Column(String)
    ai_summary = Column(JSON)

class Review(Base):
    __tablename__ = "reviews"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    mentorship_id = Column(UUID(as_uuid=True), ForeignKey("mentorships.id"))
    reviewer_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    rating = Column(Integer)
    comment = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class Job(Base):
    __tablename__ = "jobs"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    description = Column(String)
    company = Column(String)
    posted_by = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class AIMessage(Base):
    __tablename__ = "ai_messages"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    mentorship_id = Column(UUID(as_uuid=True), ForeignKey("mentorships.id"), nullable=True)
    sender_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)
    message = Column(Text)
    message_type = Column(Enum(MessageTypeEnum))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    ai_metadata = Column(JSON)  # Renamed from 'metadata' to 'ai_metadata'
