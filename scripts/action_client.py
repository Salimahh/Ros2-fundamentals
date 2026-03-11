#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from rclpy.action import ActionClient
from geometry_msgs.msg import Point
from rain_ros2_pkg.action import Navigate

DISTANCE_THRESHOLD = 0.125

class NavigateActionClient(Node):
    def __init__(self):
        super().__init__("action_client_node")
        self._action_client = ActionClient(self, Navigate, "navigate")

    def send_goal(self, x, y, z):
        goal_msg = Navigate.Goal()
        goal_msg.goal_point.x = float(x)
        goal_msg.goal_point.y = float(y)
        goal_msg.goal_point.z = float(z)

        self._action_client.wait_for_server()
        self._send_goal_future = self._action_client.send_goal_async(goal_msg, self.feedback_callback)
        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def feedback_callback(self, feedback_msg):
            feedback = feedback_msg.feedback
            print("Received feedback: " + str(feedback.distance_to_point))
    
    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            print("Goal Rejected")
            return None

        print("Goal Accepted")
        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        result = future.result().result
        print("Result: " + str(result.elasped_time) + " seconds")
        rclpy.shutdown()


def main(args=None):
    rclpy.init()
    action_client_node = NavigateActionClient()
    print("Action CLient Runnning...")

    try:
        x = input("Enter a X coordinate: ")
        y = input("Enter a Y coordinate: ")
        z = input("Enter a Z coordinate: ")

        action_client_node.send_goal(x,y,z)
        rclpy.spin(action_client_node)

    except KeyboardInterrupt:
        print("Terminating Node...")
        action_client_node.destroy_node()


if __name__ == "__main__":
    main()