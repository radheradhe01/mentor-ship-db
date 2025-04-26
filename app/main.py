from fastapi import FastAPI
from app.routers import users, mentors, mentees, interests, mentor_interests, mentorships, sessions, reviews, jobs, ai_messages

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(mentors.router, prefix="/mentors", tags=["mentors"])
app.include_router(mentees.router, prefix="/mentees", tags=["mentees"])
app.include_router(interests.router, prefix="/interests", tags=["interests"])
app.include_router(mentor_interests.router, prefix="/mentor_interests", tags=["mentor_interests"])
app.include_router(mentorships.router, prefix="/mentorships", tags=["mentorships"])
app.include_router(sessions.router, prefix="/sessions", tags=["sessions"])
app.include_router(reviews.router, prefix="/reviews", tags=["reviews"])
app.include_router(jobs.router, prefix="/jobs", tags=["jobs"])
app.include_router(ai_messages.router, prefix="/ai_messages", tags=["ai_messages"])
# Add other routers as you implement them
