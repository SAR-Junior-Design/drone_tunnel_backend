from PostgreSQL.declerations import Base
from sqlalchemy import Column, VARCHAR, TEXT, TIMESTAMP, func, FLOAT, Integer, JSON


class Drone_db(Base):
    """
    This is the main table for any kinds of clients, if the user is not on this table, it won't get authenticated!
    """
    __tablename__ = 'drones'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    username = Column(VARCHAR(66), primary_key=True)
    description = Column(TEXT, nullable=False)
    creation_date = Column(TIMESTAMP(0), server_default=func.now())

    latitude = Column(FLOAT) # TODO make sure that it doesn't round up!
    longitude = Column(FLOAT)
    altitude = Column(FLOAT)

    speed_x = Column(FLOAT)
    speed_y = Column(FLOAT)
    speed_z = Column(FLOAT)

    accel_x = Column(FLOAT)
    accel_y = Column(FLOAT)
    accel_z = Column(FLOAT)

    voltage = Column(FLOAT)
    consumption = Column(FLOAT)
    mAh_remaining = Column(FLOAT)

    connection_type = Column(VARCHAR(40))
    connection_ssid = Column(VARCHAR(60), default=0)
    connection_rssi = Column(Integer, default=0)

    current_action = Column(JSON)

    def __init__(self, username, description):
        self.username = username
        self.description = description

    @staticmethod
    def update_drone_info(username,location, speed, accel, battery, connection, current_action):
        drone = Drone_db.query.filter_by(filter=username).first()
        drone.lattitude = location["latitude"]
        drone.longtitude = location["longitude"]
        drone.altitude = location["altitude"]

        drone.speed_x = speed["speed_x"]
        drone.speed_y = speed["speed_y"]
        drone.speed_z = speed["speed_z"]

        drone.accel_x =  accel["accel_x"]
        drone.accel_y = accel["accel_y"]
        drone.accel_z = accel["accel_z"]

        drone.voltage = battery["voltage"]
        drone.consumption = battery["consumption"]
        drone.mAh_remaining = battery["mAh_remaining"]

        drone.connection_type = connection["connection_type"]
        drone.connection_ssid = connection["ssid"]
        drone.connection_rssi = connection["rssi"]

        drone.current_action = current_action


