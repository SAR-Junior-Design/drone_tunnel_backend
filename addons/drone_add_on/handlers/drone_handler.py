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
from addons.drone_add_on.models.DroneMessage import DroneMessageType


class DroneHandler(object):

    def __init__(self, server=None):
        # self.utility_handlers = {}
        self.server = server
        self.drones = {}
        self.logger = None
        self.available_methods = {}

    def register_drone(self, drone):
        self.drones[drone.id] = drone

    def initialize(self, server):
        self.server = server
        if self.server is not None:
            self.logger = self.server.logger
            self.register_methods()
        else:
            print("ERROR! DroneHandler is not initialized properly")
            raise Exception("DroneHandler is not initialized properly!")

    def register_methods(self):
        self.register_method(self.get_all_connected_drones, "get_all_connected_drones")


        self.register_method(self.get_drone_info, "get_drone_info")
        self.register_method(self.get_drone_info_result, "get_drone_info_result")

        self.register_method(self.upload_mission, "upload_mission")
        self.register_method(self.upload_mission_result, "upload_mission_result")

        self.register_method(self.send_rtl_command, "send_rtl_command")
        self.register_method(self.send_rtl_command_result, "send_rtl_command_result")

        self.register_method(self.start_mission, "start_mission")
        self.register_method(self.start_mission_result, "start_mission_result")


    def register_method(self, method, name_of_the_method):
        """
        Registers the methods
        :param method:
        :param name_of_the_method:
        :return:
        """

        if method is None:
            raise Exception("Method cannot be none")
        if name_of_the_method is None:
            raise Exception("name of the method cannot be none")

        self.available_methods[name_of_the_method] = method

    def handle_message(self, message):
        """
               {
                   "payload": "{\"type\": \"login\"}",
                   "sender": "uas-321",
                   "to": "server",
                   "type": "drone"
               }
               """
        if self.server is not None:
            drone_message_payload = message.payload
            payload_type = drone_message_payload["type"]

            self.available_methods[payload_type](message)
        else:
            raise Exception("handler is not initialized, server is none")

    def provide_info(self, message):
        """
        This method is called by the remote user, it sends all the information that it has about the current devices
        connected
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
        """
        Returns full information of the polled drone, this is called by the remote user
        :param drone_id:
        :param message:
        :return:
        """
        print("get drone info called")


    def get_drone_info_result(self, message):
        """
        This will be used by the drone to return the result of the async message get_drone_info
        :param message: the reply message which includes the information about the drone
        :return: does not return most likely writes in the db
        """
        print(message)
        pass

    def upload_mission(self, message):
        """
        This method sends a mission file to the drone, called by remote user
        :return:
        """
        pass

    def upload_mission_result(self, message):
        """

        This method receives the reply of the upload mission command, sent by the drone
        :param message:
        :return:
        """

    def send_rtl_command(self, message):
        """
        This method sends a rtl command to the drone, called by remote user
        :param drone:
        :return:
        """
        pass

    def send_rtl_command_result(self, message):
        """
        This method receives the reply of the rtl request. Sent by the drone
        :param message:
        :return:
        """
        pass

    def get_all_connected_drones(self, message):
        """
        Returns a list of all connected drones, this is called by the remote user
        :return:
        """
        print("get all connected drones called")


    def __str__(self):
        return "DroneHandler Object"

