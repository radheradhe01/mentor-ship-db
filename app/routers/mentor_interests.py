from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app import schemas, crud

router = APIRouter()

@router.post("/", response_model=schemas.MentorInterest)
async def create_mentor_interest(mentor_interest: schemas.MentorInterestCreate, db: AsyncSession = Depends(get_db)):
    try:
        db_mentor_interest = await crud.create_mentor_interest(db, mentor_interest)
        return db_mentor_interest
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list[schemas.MentorInterest])
async def read_mentor_interests(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    mentor_interests = await crud.get_mentor_interests(db, skip=skip, limit=limit)
    return mentor_interests

@router.get("/{mentor_id}/{interest_id}", response_model=schemas.MentorInterest)
async def read_mentor_interest(mentor_id: str, interest_id: int, db: AsyncSession = Depends(get_db)):
    mentor_interest = await crud.get_mentor_interest(db, mentor_id, interest_id)
    if mentor_interest is None:
        raise HTTPException(status_code=404, detail="MentorInterest not found")
    return mentor_interest
