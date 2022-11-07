from enum import Enum

from pydantic import BaseModel, EmailStr, conint
from datetime import datetime
from typing import Optional, Literal


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class UserPost(BaseModel):
    email: EmailStr

    class Config:
        orm_mode=True


class UserOut(UserPost):
    id: int
    created_at: datetime


class Post(PostBase):
    created_at: datetime
    id: int
    owner: UserPost

    class Config:
        orm_mode=True


class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode=True


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None


class VoteTypes(str, Enum):
    like = 'like'
    love = 'love'
    dislike = 'dislike'


class BaseVote(BaseModel):
    vote_type: Optional[VoteTypes] = VoteTypes.like

    class Config:
        orm_mode=True


class Vote(BaseVote):
    post_id: int
    dir:  conint(le=1)


class Votes(BaseModel):
    email: EmailStr
    Vote: BaseVote

    class Config:
        orm_mode=True