from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app import schemas, crud

router = APIRouter()

@router.post("/", response_model=schemas.Interest)
async def create_interest(interest: schemas.InterestCreate, db: AsyncSession = Depends(get_db)):
    try:
        db_interest = await crud.create_interest(db, interest)
        return db_interest
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{interest_id}", response_model=schemas.Interest)
async def read_interest(interest_id: int, db: AsyncSession = Depends(get_db)):
    db_interest = await crud.get_interest(db, interest_id)
    if db_interest is None:
        raise HTTPException(status_code=404, detail="Interest not found")
    return db_interest

@router.get("/", response_model=list[schemas.Interest])
async def read_interests(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    interests = await crud.get_interests(db, skip=skip, limit=limit)
    return interests
