from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app import schemas, crud

router = APIRouter()

@router.post("/", response_model=schemas.Mentee)
async def create_mentee(mentee: schemas.MenteeCreate, db: AsyncSession = Depends(get_db)):
    try:
        db_mentee = await crud.create_mentee(db, mentee)
        return db_mentee
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{user_id}", response_model=schemas.Mentee)
async def read_mentee(user_id: str, db: AsyncSession = Depends(get_db)):
    db_mentee = await crud.get_mentee(db, user_id)
    if db_mentee is None:
        raise HTTPException(status_code=404, detail="Mentee not found")
    return db_mentee

@router.get("/", response_model=list[schemas.Mentee])
async def read_mentees(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    mentees = await crud.get_mentees(db, skip=skip, limit=limit)
    return mentees
