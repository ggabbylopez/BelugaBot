import database
from entities import Base, UserEntity

# Reset Tables
Base.metadata.drop_all(database.engine)
Base.metadata.create_all(database.engine)

# Enter Mock Data
from sqlalchemy.orm import Session
session = Session(database.engine)

# TODO: Add a UserEntity to the database session and commit it.
user = UserEntity(pid = 730407925, first_name = "Gabriella", last_name ="Lopez")
session.add(user)
session.commit()