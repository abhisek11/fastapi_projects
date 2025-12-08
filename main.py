from fastapi import FastAPI, status, Response
from router import blog_get
from router import blog_post


app = FastAPI(
    summary="Blogging API",
    description="An API for creating and managing blogs",
    version="1.0.0"
)

app.include_router(blog_get.router)
app.include_router(blog_post.router)

@app.get('/hello')
def index():
    return {'message': 'Hello World'}
