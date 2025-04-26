from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app import schemas, crud

router = APIRouter()

@router.post("/", response_model=schemas.AIMessage)
async def create_ai_message(ai_message: schemas.AIMessageCreate, db: AsyncSession = Depends(get_db)):
    try:
        db_ai_message = await crud.create_ai_message(db, ai_message)
        return db_ai_message
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{ai_message_id}", response_model=schemas.AIMessage)
async def read_ai_message(ai_message_id: str, db: AsyncSession = Depends(get_db)):
    db_ai_message = await crud.get_ai_message(db, ai_message_id)
    if db_ai_message is None:
        raise HTTPException(status_code=404, detail="AIMessage not found")
    return db_ai_message

@router.get("/", response_model=list[schemas.AIMessage])
async def read_ai_messages(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    ai_messages = await crud.get_ai_messages(db, skip=skip, limit=limit)
    return ai_messages
