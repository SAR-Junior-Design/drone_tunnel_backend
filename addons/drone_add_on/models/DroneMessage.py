from enum import Enum


class DroneMessage(object):

    def __init__(self):
        self.type = None
        self.data = None


class DroneMessageType(Enum):

    def __str__(self):
        return str(self.value)

    status_update = "status_update"
    event = "event"
    action = "action"
    provide_info = "provide_info"

