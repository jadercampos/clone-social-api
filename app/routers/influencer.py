from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.postgres import get_db
from app.schemas.postgres.influencer import (
    InfluencerCreate,
    InfluencerUpdate,
    InfluencerRead,
)
from app.services.influencer import (
    create_new_influencer,
    get_influencer,
    list_influencers,
    update_influencer,
    remove_influencer,
)

router = APIRouter(prefix="/influencers", tags=["Influencers"])

@router.post("/", response_model=InfluencerRead, status_code=201)
async def create(data: InfluencerCreate, db: AsyncSession = Depends(get_db)):
    return await create_new_influencer(db, data)

@router.get("/{influencer_id}", response_model=InfluencerRead)
async def read(influencer_id: str, db: AsyncSession = Depends(get_db)):
    result = await get_influencer(db, influencer_id)
    if not result:
        raise HTTPException(status_code=404, detail="Influencer not found")
    return result

@router.get("/", response_model=list[InfluencerRead])
async def read_all(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    return await list_influencers(db, skip, limit)

@router.put("/{influencer_id}", response_model=InfluencerRead)
async def update(influencer_id: str, data: InfluencerUpdate, db: AsyncSession = Depends(get_db)):
    updated = await update_influencer(db, influencer_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Influencer not found")
    return updated

@router.delete("/{influencer_id}", status_code=204)
async def delete(influencer_id: str, db: AsyncSession = Depends(get_db)):
    success = await remove_influencer(db, influencer_id)
    if not success:
        raise HTTPException(status_code=404, detail="Influencer not found")
