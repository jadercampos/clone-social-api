from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.dependencies import get_db
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
def create(data: InfluencerCreate, db: Session = Depends(get_db)):
    return create_new_influencer(db, data)

@router.get("/{influencer_id}", response_model=InfluencerRead)
def read(influencer_id: str, db: Session = Depends(get_db)):
    result = get_influencer(db, influencer_id)
    if not result:
        raise HTTPException(status_code=404, detail="Influencer not found")
    return result

@router.get("/", response_model=list[InfluencerRead])
def read_all(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return list_influencers(db, skip, limit)

@router.put("/{influencer_id}", response_model=InfluencerRead)
def update(influencer_id: str, data: InfluencerUpdate, db: Session = Depends(get_db)):
    updated = update_influencer(db, influencer_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Influencer not found")
    return updated

@router.delete("/{influencer_id}", status_code=204)
def delete(influencer_id: str, db: Session = Depends(get_db)):
    if not remove_influencer(db, influencer_id):
        raise HTTPException(status_code=404, detail="Influencer not found")
