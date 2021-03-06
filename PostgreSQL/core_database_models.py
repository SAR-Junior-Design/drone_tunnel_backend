from sqlalchemy import Column, VARCHAR, TEXT, TIMESTAMP, func

from PostgreSQL.declerations import Base


class User(Base):
    """
    This is the main table for any kinds of clients, if the user is not on this table, it won't get authenticated!
    """
    __tablename__ = 'users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    username = Column(VARCHAR(66), primary_key=True)
    password = Column(VARCHAR(66), nullable=False)
    description = Column(TEXT, nullable=False)
    user_type = Column(VARCHAR(66), nullable=False)
    creation_date = Column(TIMESTAMP(0), server_default=func.now())

    def __init__(self, username, password, description, user_type):
        self.username = username
        self.password = password
        self.description = description
        self.user_type = user_type

    @staticmethod
    def authenticate_user(username, password):
        """
        This method authenticates the user
        :param username: the username of the user
        :param password: the password of the user
        :return: if user fails to authenticate returns false, if it succeeds returns true
        """
        db_user = User.query.filter_by(username=username, password=password).first()
        if db_user is not None and (db_user.password == password and db_user.username == username):
            return True
        else:
            return False

class Connected_user(Base):
    """
    This table is for checking the currently online clients, my intial goal was to have theese in a memory database like
    mnesia, however right now they are on disk...
    """
    __tablename__ = 'connected_users'
    username = Column(VARCHAR(66), primary_key=True)
    connection_date = Column(TIMESTAMP(0), server_default=func.now())
    last_ping = Column(TIMESTAMP(0), server_default=func.now())

    def __init__(self, username):
        self.username = username

    def update_last_ping(self, last_ping):
        """
        Updates the last ping of the user
        :param last_ping:
        :return:
        """
        self.last_ping = last_ping

    def clear_table(self):
        """
        Clears the whole table, its for booting up and stuff.
        :return:
        """
        pass

class Event(Base):
    """
    Actually I have to name this table in a better way, it is just connection and disconnection events, ping timeouts
    and such, I was also planning to put violations here...
    """
    __tablename__ = 'events'
    event_name = Column(VARCHAR(100), nullable=False)
    date = Column(TIMESTAMP(0), server_default=func.now())
    who = Column(VARCHAR(66), primary_key=True)

    def __init__(self, event_name, who):
        self.who = who
        self.event_name = event_name
