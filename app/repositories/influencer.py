from sqlalchemy.orm import Session
from app.models.postgres.influencer import Influencer
from app.schemas.postgres.influencer import InfluencerCreate, InfluencerUpdate

def create_influencer(db: Session, data: InfluencerCreate) -> Influencer:
    obj = Influencer(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def update_influencer(db: Session, influencer_id: str, data: InfluencerUpdate):
    obj = db.query(Influencer).filter(Influencer.id == influencer_id).first()
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def get_influencer_by_id(db: Session, influencer_id: str) -> Influencer:
    return db.query(Influencer).filter(Influencer.id == influencer_id).first()

def get_all_influencers(db: Session, skip=0, limit=100):
    return db.query(Influencer).offset(skip).limit(limit).all()

def delete_influencer(db: Session, influencer_id: str):
    obj = get_influencer_by_id(db, influencer_id)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False
