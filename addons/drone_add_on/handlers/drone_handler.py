"""
This module is for handling drone releated messages
Author: Kaan Goksal
Copyright: Kaan Goksal
Date: 4 September 2017

"""

import json

from addons.drone_add_on.models.uas import UAS
from models.Message import Message
from models.Message import MessageType


class DroneHandler(object):
    def __init__(self, server=None):
        # self.utility_handlers = {}
        self.server = server
        self.drones = {}
        self.logger = None

    def register_drone(self, drone):
        self.drones[drone.id] = drone

    def initialize(self,server):
        self.server = server
        if self.server is not None:
            self.logger = self.server.logger
        else:
            print("ERROR! DroneHandler is not initialized properly")

    def handle_message(self, message):
        """
        {
            "payload": "{\"type\": \"login\"}",
            "sender": "uas-321",
            "to": "server",
            "type": "drone"
        }
        """
        payload = message.payload
        payload_type = payload["type"]

        if payload_type == "login":
            new_uas = UAS(message.sender, None)
            self.drones[message.sender] = new_uas
        elif payload_type == "status_update":
            retrieved_uas = self.drones[message.sender]
            payload_data = payload["data"]
            retrieved_uas.update_info(payload_data)
        elif payload_type == "provide_info":
            self.provide_info(message)
        else:
            pass

    def provide_info(self, message):
        """
                {   "id": 112223,
                    "payload": "{\"type\": \"provide_info\",
                                "command": { "name":"fetch_all_drone_info"
                                }",
                    "sender": "communication_handler",
                    "to": "drone_handler",
                    "type": "drone"
                }
        """
        payload = message.payload
        info_command = payload["command"]
        name = info_command["name"]

        if name == "fetch_all_drone_info":
            r_list = []
            for drone in list(self.drones.keys()):
                r_list.append(drone.to_dict())
            result = json.dumps({"drones": r_list})

            new_message = Message("drone_handler", message.sender, "comms", {"type": "reply", "data": result } )

            self.server.message_handler.handle_message(new_message)

    def get_drone_info(self, drone_id, message):
        pass




    def handle_ping(self, message):
        client = self.server.get_client_from_username(message.sender)
        client.update_last_ping()

        ping_payload = {"utility_group": "ping"}
        ping_message = Message("core", message.sender, MessageType.utility, ping_payload)
        self.server.send_message_to_client(ping_message)

    def __str__(self):
        return "DroneHandler Object"

