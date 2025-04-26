from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app import schemas, crud

router = APIRouter()

@router.post("/", response_model=schemas.Job)
async def create_job(job: schemas.JobCreate, db: AsyncSession = Depends(get_db)):
    try:
        db_job = await crud.create_job(db, job)
        return db_job
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{job_id}", response_model=schemas.Job)
async def read_job(job_id: int, db: AsyncSession = Depends(get_db)):
    db_job = await crud.get_job(db, job_id)
    if db_job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return db_job

@router.get("/", response_model=list[schemas.Job])
async def read_jobs(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    jobs = await crud.get_jobs(db, skip=skip, limit=limit)
    return jobs
