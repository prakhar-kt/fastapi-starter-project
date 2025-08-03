from src.db.config import SessionLocal
from src.users.models import User
from sqlalchemy import select


# Insert or Create User
def create_user(name: str, email: str):

    with SessionLocal() as session:
        user = User(name=name, email=email)
        session.add(user)
        session.commit()


# Get all users
def get_all_users():
    with SessionLocal() as session:
        stmt = select(User)
        users = session.scalars(stmt)
        return users.all()


# Get single user by id
def get_single_user(id: int):

    with SessionLocal() as session:
        stmt = select(User).where(User.id == id)
        user = session.scalars(stmt).first()
        return user
