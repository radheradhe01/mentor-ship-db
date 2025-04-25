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

# Add similar CRUD functions for other tables
