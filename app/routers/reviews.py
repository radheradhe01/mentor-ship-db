from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app import schemas, crud

router = APIRouter()

@router.post("/", response_model=schemas.Review)
async def create_review(review: schemas.ReviewCreate, db: AsyncSession = Depends(get_db)):
    try:
        db_review = await crud.create_review(db, review)
        return db_review
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{review_id}", response_model=schemas.Review)
async def read_review(review_id: str, db: AsyncSession = Depends(get_db)):
    db_review = await crud.get_review(db, review_id)
    if db_review is None:
        raise HTTPException(status_code=404, detail="Review not found")
    return db_review

@router.get("/", response_model=list[schemas.Review])
async def read_reviews(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    reviews = await crud.get_reviews(db, skip=skip, limit=limit)
    return reviews
