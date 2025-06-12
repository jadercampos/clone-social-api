from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.influencer import (
    create_influencer,
    get_influencer_by_id,
    get_all_influencers,
    delete_influencer,
    update_influencer,
)
from app.schemas.postgres.influencer import InfluencerCreate, InfluencerUpdate

async def create_new_influencer(db: AsyncSession, data: InfluencerCreate):
    return await create_influencer(db, data)

async def get_influencer(db: AsyncSession, influencer_id: str):
    return await get_influencer_by_id(db, influencer_id)

async def list_influencers(db: AsyncSession, skip: int, limit: int):
    return await get_all_influencers(db, skip, limit)

async def remove_influencer(db: AsyncSession, influencer_id: str):
    return await delete_influencer(db, influencer_id)

async def update_influencer(db: AsyncSession, influencer_id: str, data: InfluencerUpdate):
    return await update_influencer(db, influencer_id, data)
