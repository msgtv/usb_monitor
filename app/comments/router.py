from typing import Annotated, Literal

from fastapi import APIRouter, Path, Query, Depends
from fastapi_pagination import Page

from app.comments.schemas import SComment
from app.comments.dao import CommentDAO
from app.comments.dependencies import CommentsSearchArgsDepend, CommentsAddArgsDepend
from app.comments.exceptions import CommentAddObjectNotFound


router = APIRouter(
    prefix="/comments",
    tags=["Комментарии"],
)


@router.get('')
async def get_comments(
        args: Annotated[CommentsSearchArgsDepend, Depends(CommentsSearchArgsDepend)]
) -> Page[SComment]:
    comments = await CommentDAO.get_all_paginated(args.filters)

    return comments


@router.post('')
async def add_comment(
        args: Annotated[CommentsAddArgsDepend, Depends(CommentsAddArgsDepend)]
) -> SComment:
    comment = await CommentDAO.add_comment(**args.values)
    if comment:
        return comment
    raise CommentAddObjectNotFound(detail=f'No found object {args.object_type} with id {args.object_id}')
