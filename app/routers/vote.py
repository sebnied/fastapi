from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import models, schemas, oath2, database
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List, Optional
import pprint

router = APIRouter(
    prefix="/vote",
    tags=['Vote']
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.Vote, db: Session = Depends(database.get_db),
         current_user: int = Depends(oath2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id {vote.post_id} does not exists")

    vote_query = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id,
                                              models.Vote.user_id == current_user.id)
    found_vote = vote_query.first()

    if vote.dir == 1:
        if found_vote:
            if vote.vote_type == found_vote.vote_type:
                raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                    detail=f"user {current_user.id} already {vote.vote_type}d post {vote.post_id}")
            else:
                vote_query.update({'vote_type': vote.vote_type}, synchronize_session=False)
                db.commit()
                return {"message": f"successfully changed vote to {vote.vote_type}"}
        new_vote = models.Vote(post_id=vote.post_id, user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        return {"message": "successfully added vote"}
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"vote does not exist")
        vote_query.delete(synchronize_session=False)
        db.commit()
        return {"message": "successfully removed  vote"}


@router.get("/{id}", response_model=List[schemas.Votes])
def view_votes(id: int, db: Session = Depends(get_db),
               current_user: int = Depends(oath2.get_current_user)):
    votes_query = db.query(models.Vote).join(
        models.User, models.Vote.user_id == models.User.id).add_columns(models.User.email).filter(
        models.Vote.post_id == id)
    votes = votes_query.all()

    if not votes:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'no votes associated with post id {id}')
    return votes
