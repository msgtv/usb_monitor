from typing import Annotated, Literal

from fastapi import APIRouter, Path, Query, Depends
from fastapi_pagination import Page

from app.dependencies import SessionDepend
from app.comments.schemas import SComment
from app.comments.dao import CommentDAO
from app.comments.dependencies import CommentsSearchArgsDepend, CommentsAddArgsDepend
from app.comments.exceptions import CommentAddObjectNotFound
from app.auth.dependencies import DefaultUser


router = APIRouter(
    prefix="/comments",
    tags=["Комментарии"],
)


@router.get('', dependencies=[Depends(DefaultUser)])
async def get_comments(
        args: Annotated[CommentsSearchArgsDepend, Depends(CommentsSearchArgsDepend)],
        session: SessionDepend,
) -> Page[SComment]:
    comments = await CommentDAO.get_all_paginated(session=session, filters=args.filters)
    return comments


@router.post('', dependencies=[Depends(DefaultUser)])
async def add_comment(
        args: Annotated[CommentsAddArgsDepend, Depends(CommentsAddArgsDepend)],
        session: SessionDepend,
) -> SComment:
    comment = await CommentDAO.add_comment(session=session, **args.values)
    if comment:
        return comment
    raise CommentAddObjectNotFound(detail=f'No found object {args.object_type} with id {args.object_id}')
