from fastapi import APIRouter, Request, Response, Query, Body, Path
from pydantic import BaseModel
from typing import Optional, List


router = APIRouter(
    prefix='/blog',
    tags=['blog']
)

class BlogModel(BaseModel):
    title: str
    content: str
    published: Optional[bool]
    no_of_comments: int

@router.post('/new/{id}')
def create_post(request: Request, blog: BlogModel, id: int, version: int=1):
    print(request.headers)
    print(blog.title)
    return {
        "id": id,
        "data": blog,
        "version": version
        }

@router.post("/new/{id}/comment")
def create_comment(blog: BlogModel, id: int,
                comment_title: str = Query(
                    title="Id of the commnet",
                    description= "Some description for comment_Title",
                    alias="commentTitle",
                ),
                content=Body(...,
                            min_length=10,
                            max_length=12,
                            regex='^[a-z\s]*$'
                ),
                v: Optional[List[str]] = Query(['1.0', '1.1', '1.2'])
            ):
    return {
        "id": id,
        "blog": blog,
        "comment_title": comment_title, 
        "content": content,
        "v": v
        }
