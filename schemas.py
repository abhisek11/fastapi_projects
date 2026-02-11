from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    name: str
    email: str
    phone: str
    password: str
    
class UserDisplay(BaseModel):
    username: str
    email: str

    class Config():
        from_attributes=True

class ErrorDisplay(BaseModel):
    msg: str
    code: str

    