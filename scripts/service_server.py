#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from rain_ros2_pkg.srv import OddEvenCheck

class OddEvenCheckServer(Node):
    def __init__(self):
        super().__init__("odd_even_service_server_node")
        self.srv = self.create_service(OddEvenCheck, "odd_even_check", self.determine_odd_even) #2nd param is the topic, 3rd parameter is the call back fxn

    def determine_odd_even(self, request, response):
        print("Request Received")

        if request.number % 2 == 0: #number is request in srv
            response.decision = "Even" #decision is response in srv
        elif request.number % 2 == 1:
            response.decision = "Odd"
        else:
            response.decision = "Error"

        print(request)
        print(response)

        return response

def main(args=None): # this says i want no argument for that function 
    rclpy.init()
    server_node = OddEvenCheckServer() #creates an instance of oddevencheck server thst can be modified anytime. basically a clone
    print("Odd Even Check Service Server Runnning...")

    try:
        rclpy.spin(server_node)
    except KeyboardInterrupt:
        print("Terminating Node...")
        server_node.destroy_node()


if __name__ == "__main__":
    main()