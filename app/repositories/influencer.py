from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.postgres.influencer import Influencer
from app.schemas.postgres.influencer import InfluencerCreate, InfluencerUpdate
from typing import List, Optional


async def create_influencer(db: AsyncSession, data: InfluencerCreate) -> Influencer:
    obj = Influencer(**data.dict())
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj


async def update_influencer(
    db: AsyncSession, influencer_id: UUID, data: InfluencerUpdate
) -> Optional[Influencer]:
    result = await db.execute(select(Influencer).filter(Influencer.id == influencer_id))
    obj = result.scalar_one_or_none()
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    await db.commit()
    await db.refresh(obj)
    return obj


async def get_influencer_by_id(db: AsyncSession, influencer_id: UUID) -> Optional[Influencer]:
    result = await db.execute(select(Influencer).filter(Influencer.id == influencer_id))
    return result.scalar_one_or_none()


async def get_all_influencers(db: AsyncSession, skip: int = 0, limit: int = 100) -> List[Influencer]:
    result = await db.execute(select(Influencer).offset(skip).limit(limit))
    return result.scalars().all()


async def delete_influencer(db: AsyncSession, influencer_id: UUID) -> bool:
    obj = await get_influencer_by_id(db, influencer_id)
    if obj:
        await db.delete(obj)
        await db.commit()
        return True
    return False
