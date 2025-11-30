from fastapi import FastAPI, status, Response
from enum import Enum
from typing import Optional



app = FastAPI()

@app.get('/hello')
def index():
    return {'message': 'Hello World'}


@app.get('/blogs/all')
def get_all_blog(page=1, page_size: Optional[int]=None):
    return {"message": f" All {page_size} blogs on page {page}"}


@app.get('/blog/{id}/comment/{comment_id}')
def get_blog_commentid(id: int, comment_id: int, valid: bool, username: Optional[str]=None):
    return {
        "message": {
        'blog_id': id,
        'comment_id': comment_id,
        'valid': valid,
        'username': username
    }}


class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'


@app.get('/blog/type/{type}')
def get_blog_type(type: BlogType):
    return {"message": f'Blog type is {type}'}


@app.get('/blog/{id}', status_code=status.HTTP_200_OK)
def get_blog(id: int, response: Response):
    if id>5 :
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f"Id not found "}
    else: 
        response.status_code = status.HTTP_200_OK
        return {"message": f"Blog ID {id}"}
