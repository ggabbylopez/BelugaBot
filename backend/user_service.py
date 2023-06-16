from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from database import db_session
from models import User
from entities import UserEntity


class UserService:

    _session: Session

    def __init__(self, session: Session = Depends(db_session)):
        self._session = session

    def all(self) -> list[User]:
        query = select(UserEntity)
        entities = self._session.scalars(query).all()
        return [entity.to_model() for entity in entities]

    def create(self, user: User) -> User:
        user_in_table = self._session.get(UserEntity, user.pid)
        if user_in_table:
            raise Exception("User with this pid already registered")
        else:
            u_entity: UserEntity = UserEntity.from_model(user)
            self._session.add(u_entity)
            self._session.commit()
            return u_entity.to_model()

    def get(self, pid: int) -> User | None:
        user = self._session.get(UserEntity, pid)
        if user:
            return user.to_model()
        else:
            raise ValueError(f"no user found with pid: {pid}.")

    def delete(self, pid: int) -> None:
        user = self._session.get(UserEntity,pid)
        if user:
            self._session.delete(user)
            self._session.commit()
        else:
            raise ValueError(f"User not found with pid: {pid}")