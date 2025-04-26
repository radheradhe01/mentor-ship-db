from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app import schemas, crud

router = APIRouter()

@router.post("/", response_model=schemas.Mentorship)
async def create_mentorship(mentorship: schemas.MentorshipCreate, db: AsyncSession = Depends(get_db)):
    try:
        db_mentorship = await crud.create_mentorship(db, mentorship)
        return db_mentorship
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{mentorship_id}", response_model=schemas.Mentorship)
async def read_mentorship(mentorship_id: str, db: AsyncSession = Depends(get_db)):
    db_mentorship = await crud.get_mentorship(db, mentorship_id)
    if db_mentorship is None:
        raise HTTPException(status_code=404, detail="Mentorship not found")
    return db_mentorship

@router.get("/", response_model=list[schemas.Mentorship])
async def read_mentorships(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    mentorships = await crud.get_mentorships(db, skip=skip, limit=limit)
    return mentorships
