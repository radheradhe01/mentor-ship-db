from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app import schemas, crud

router = APIRouter()

@router.post("/", response_model=schemas.Session)
async def create_session(session: schemas.SessionCreate, db: AsyncSession = Depends(get_db)):
    try:
        db_session = await crud.create_session(db, session)
        return db_session
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{session_id}", response_model=schemas.Session)
async def read_session(session_id: str, db: AsyncSession = Depends(get_db)):
    db_session = await crud.get_session(db, session_id)
    if db_session is None:
        raise HTTPException(status_code=404, detail="Session not found")
    return db_session

@router.get("/", response_model=list[schemas.Session])
async def read_sessions(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    sessions = await crud.get_sessions(db, skip=skip, limit=limit)
    return sessions
