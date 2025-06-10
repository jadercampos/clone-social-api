from app.repositories.influencer import (
    create_influencer,
    get_influencer_by_id,
    get_all_influencers,
    delete_influencer,
    update_influencer
)

def create_new_influencer(db, data):
    return create_influencer(db, data)

def get_influencer(db, influencer_id):
    return get_influencer_by_id(db, influencer_id)

def list_influencers(db, skip, limit):
    return get_all_influencers(db, skip, limit)

def remove_influencer(db, influencer_id):
    return delete_influencer(db, influencer_id)

def update_influencer(db, influencer_id: str, data):
    return update_influencer(db, influencer_id, data)
