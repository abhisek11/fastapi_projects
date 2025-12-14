from sqlalchemy.orm.session import Session
from schemas import UserBase
from db.model import DBUser
from db.hash import Hash


def create_user(db: Session, request: UserBase):
    new_user = DBUser(
        username = request.username,
        name = request.name,
        phone = request.phone,
        email = request.email,
        password = Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

def get_all_users(db: Session):
    return db.query(DBUser).all()

def get_user(db: Session, id: int):
    return db.query(DBUser).filter(DBUser.id == id).first()