from sqlalchemy.orm import sessionmaker

from PostgreSQL.core_database_models import Users
from PostgreSQL.declerations import Base
from PostgreSQL.declerations import engine

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

new_user = Users("username1", "superpass2", "test device", "botnet")
session.add(new_user)
session.commit()
