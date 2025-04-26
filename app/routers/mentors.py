from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app import schemas, crud

router = APIRouter()

@router.post("/", response_model=schemas.Mentor)
async def create_mentor(mentor: schemas.MentorCreate, db: AsyncSession = Depends(get_db)):
    try:
        db_mentor = await crud.create_mentor(db, mentor)
        return db_mentor
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{user_id}", response_model=schemas.Mentor)
async def read_mentor(user_id: str, db: AsyncSession = Depends(get_db)):
    db_mentor = await crud.get_mentor(db, user_id)
    if db_mentor is None:
        raise HTTPException(status_code=404, detail="Mentor not found")
    return db_mentor

@router.get("/", response_model=list[schemas.Mentor])
async def read_mentors(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    mentors = await crud.get_mentors(db, skip=skip, limit=limit)
    return mentors
