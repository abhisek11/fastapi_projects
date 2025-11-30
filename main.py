from fastapi import FastAPI
from enum import Enum
from typing import Optional


app = FastAPI()

@app.get('/hello')
def index():
    return {'message': 'Hello World'}

@app.get('/blogs/all')
def get_all_blog(page=1, page_size: Optional[int]=None):
    return {"message": f" blogs {page} page and {page_size} page size"}

class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'

@app.get('/blog/type/{type}')
def get_blog_type(type: BlogType):
    return {"message": f'Blog type is {type}'}


@app.get('/blog/{id}')
def get_blog(id: int):
    return {"message": f"Blog ID {id}"}