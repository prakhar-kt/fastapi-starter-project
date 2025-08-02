from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


from src.users import models as user_models
