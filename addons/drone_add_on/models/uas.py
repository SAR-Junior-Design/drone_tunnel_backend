import json


class UAS(object):

    def __init__(self, id, connection):
        """
        Unmanned Aerial System Object
        :param id: id of the system
        :param connection: connection that we are interacting with the system
        """
        self.id = id
        self.location = Location(None, None, None)
        self.battery_status = Battery(self.id + "-Battery")
        self.socket_connection = connection
        self.drone_connection = None

        self.open_tasks = {}
        self.current_behaviour = None
        self.velocity = Velocity(None, None, None)

    def update_info(self, payload):
        parsed_json_object = json.loads(payload)

        #drone_id = parsed_json_object["id"]

        battery_info_object = parsed_json_object["battery_info"]

        self.battery_status.voltage = battery_info_object["voltage"]
        self.battery_status.consumption = battery_info_object["consumption"]
        self.battery_status.mAh_remaining = battery_info_object["mAh_remaining"]
        self.battery_status.total_mAh = battery_info_object["total_mAh"]

        location_object = parsed_json_object["location"]

        self.location.latitude = location_object["latitude"]
        self.location.longitude = location_object["longitude"]
        self.location.altitude = location_object["altitude"]

        velocity_object = parsed_json_object["velocity"]
        self.velocity.x = velocity_object["x"]
        self.velocity.y = velocity_object["y"]
        self.velocity.z = velocity_object["z"]

        self.drone_connection = parsed_json_object["connection"]

    def to_dict(self):
        return_dict = {
            "id": self.id,
            "battery_info": {
                "voltage": self.battery_status.voltage,
                "consumption": self.battery_status.consumption,
                "mAh_remaining": self.battery_status.mAh_remaining,
                "total_mAh": self.battery_status.total_mAh
            },
            "location": {
                "latitude": self.location.latitude,
                "longitude": self.location.longitude,
                "altitude": self.location.altitude
            },
            "velocity": {
                "x": self.velocity.x,
                "y": self.velocity.y,
                "z": self.velocity.z

            },
            "connection": self.drone_connection
        }
        return return_dict


class Battery(object):
    """
    This class is for keeping the data about battery organized, in future it can have fancy features
    """
    def __init__(self, id):
        self.id = id
        self.voltage = None
        self.total_mAh = None
        self.consumption = None
        self.mAh_remaining = None


class Location(object):
    """
    This class is for keeping location information organized
    """

    def __init__(self, latitude, longitude, altitude):

        self.altitude = altitude
        self.latitude = latitude
        self.longitude = longitude


class Velocity(object):
    """
    This class is for keeping Velocity information organized
    """
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

