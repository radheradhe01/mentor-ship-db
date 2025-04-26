from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app import models, schemas
from sqlalchemy.exc import IntegrityError

async def create_user(db: AsyncSession, user: schemas.UserCreate):
    db_user = models.User(
        email=user.email,
        password_hash=user.password,  # Hash in production!
        name=user.name,
        avatar_url=user.avatar_url,
        user_type=user.user_type,
    )
    db.add(db_user)
    try:
        await db.commit()
        await db.refresh(db_user)
        return db_user
    except IntegrityError:
        await db.rollback()
        raise

async def get_user(db: AsyncSession, user_id):
    result = await db.execute(select(models.User).where(models.User.id == user_id))
    return result.scalar_one_or_none()

async def get_users(db: AsyncSession, skip=0, limit=100):
    result = await db.execute(select(models.User).offset(skip).limit(limit))
    return result.scalars().all()

async def create_mentor(db: AsyncSession, mentor: schemas.MentorCreate):
    db_mentor = models.Mentor(**mentor.dict())
    db.add(db_mentor)
    try:
        await db.commit()
        await db.refresh(db_mentor)
        return db_mentor
    except IntegrityError:
        await db.rollback()
        raise

async def get_mentor(db: AsyncSession, user_id):
    result = await db.execute(select(models.Mentor).where(models.Mentor.user_id == user_id))
    return result.scalar_one_or_none()

async def get_mentors(db: AsyncSession, skip=0, limit=100):
    result = await db.execute(select(models.Mentor).offset(skip).limit(limit))
    return result.scalars().all()

async def create_mentee(db: AsyncSession, mentee: schemas.MenteeCreate):
    db_mentee = models.Mentee(**mentee.dict())
    db.add(db_mentee)
    try:
        await db.commit()
        await db.refresh(db_mentee)
        return db_mentee
    except IntegrityError:
        await db.rollback()
        raise

async def get_mentee(db: AsyncSession, user_id):
    result = await db.execute(select(models.Mentee).where(models.Mentee.user_id == user_id))
    return result.scalar_one_or_none()

async def get_mentees(db: AsyncSession, skip=0, limit=100):
    result = await db.execute(select(models.Mentee).offset(skip).limit(limit))
    return result.scalars().all()

async def create_interest(db: AsyncSession, interest: schemas.InterestCreate):
    db_interest = models.Interest(**interest.dict())
    db.add(db_interest)
    try:
        await db.commit()
        await db.refresh(db_interest)
        return db_interest
    except IntegrityError:
        await db.rollback()
        raise

async def get_interest(db: AsyncSession, interest_id):
    result = await db.execute(select(models.Interest).where(models.Interest.id == interest_id))
    return result.scalar_one_or_none()

async def get_interests(db: AsyncSession, skip=0, limit=100):
    result = await db.execute(select(models.Interest).offset(skip).limit(limit))
    return result.scalars().all()

async def create_mentor_interest(db: AsyncSession, mentor_interest: schemas.MentorInterestCreate):
    db_mentor_interest = models.MentorInterest(**mentor_interest.dict())
    db.add(db_mentor_interest)
    try:
        await db.commit()
        await db.refresh(db_mentor_interest)
        return db_mentor_interest
    except IntegrityError:
        await db.rollback()
        raise

async def get_mentor_interest(db: AsyncSession, mentor_id, interest_id):
    result = await db.execute(select(models.MentorInterest).where(
        (models.MentorInterest.mentor_id == mentor_id) & (models.MentorInterest.interest_id == interest_id)
    ))
    return result.scalar_one_or_none()

async def get_mentor_interests(db: AsyncSession, skip=0, limit=100):
    result = await db.execute(select(models.MentorInterest).offset(skip).limit(limit))
    return result.scalars().all()

async def create_mentorship(db: AsyncSession, mentorship: schemas.MentorshipCreate):
    db_mentorship = models.Mentorship(**mentorship.dict())
    db.add(db_mentorship)
    try:
        await db.commit()
        await db.refresh(db_mentorship)
        return db_mentorship
    except IntegrityError:
        await db.rollback()
        raise

async def get_mentorship(db: AsyncSession, mentorship_id):
    result = await db.execute(select(models.Mentorship).where(models.Mentorship.id == mentorship_id))
    return result.scalar_one_or_none()

async def get_mentorships(db: AsyncSession, skip=0, limit=100):
    result = await db.execute(select(models.Mentorship).offset(skip).limit(limit))
    return result.scalars().all()

async def create_session(db: AsyncSession, session: schemas.SessionCreate):
    db_session = models.Session(**session.dict())
    db.add(db_session)
    try:
        await db.commit()
        await db.refresh(db_session)
        return db_session
    except IntegrityError:
        await db.rollback()
        raise

async def get_session(db: AsyncSession, session_id):
    result = await db.execute(select(models.Session).where(models.Session.id == session_id))
    return result.scalar_one_or_none()

async def get_sessions(db: AsyncSession, skip=0, limit=100):
    result = await db.execute(select(models.Session).offset(skip).limit(limit))
    return result.scalars().all()

async def create_review(db: AsyncSession, review: schemas.ReviewCreate):
    db_review = models.Review(**review.dict())
    db.add(db_review)
    try:
        await db.commit()
        await db.refresh(db_review)
        return db_review
    except IntegrityError:
        await db.rollback()
        raise

async def get_review(db: AsyncSession, review_id):
    result = await db.execute(select(models.Review).where(models.Review.id == review_id))
    return result.scalar_one_or_none()

async def get_reviews(db: AsyncSession, skip=0, limit=100):
    result = await db.execute(select(models.Review).offset(skip).limit(limit))
    return result.scalars().all()

async def create_job(db: AsyncSession, job: schemas.JobCreate):
    db_job = models.Job(**job.dict())
    db.add(db_job)
    try:
        await db.commit()
        await db.refresh(db_job)
        return db_job
    except IntegrityError:
        await db.rollback()
        raise

async def get_job(db: AsyncSession, job_id):
    result = await db.execute(select(models.Job).where(models.Job.id == job_id))
    return result.scalar_one_or_none()

async def get_jobs(db: AsyncSession, skip=0, limit=100):
    result = await db.execute(select(models.Job).offset(skip).limit(limit))
    return result.scalars().all()

async def create_ai_message(db: AsyncSession, ai_message: schemas.AIMessageCreate):
    db_ai_message = models.AIMessage(**ai_message.dict())
    db.add(db_ai_message)
    try:
        await db.commit()
        await db.refresh(db_ai_message)
        return db_ai_message
    except IntegrityError:
        await db.rollback()
        raise

async def get_ai_message(db: AsyncSession, ai_message_id):
    result = await db.execute(select(models.AIMessage).where(models.AIMessage.id == ai_message_id))
    return result.scalar_one_or_none()

async def get_ai_messages(db: AsyncSession, skip=0, limit=100):
    result = await db.execute(select(models.AIMessage).offset(skip).limit(limit))
    return result.scalars().all()
