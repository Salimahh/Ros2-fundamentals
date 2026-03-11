#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64   # Float64 because RPM is a decimal number

import math
import random  # To simulate changing RPM values

class RPMPublisher(Node):
    def __init__(self):
        super().__init__("rpm_publisher_node")

        # Create a publisher on topic "wheel_rpm", with queue size 10
        self.pub = self.create_publisher(Float64, "wheel_rpm", 10)

        # Call publish_rpm every 0.5 seconds
        self.timer = self.create_timer(0.5, self.publish_rpm)

    def publish_rpm(self):
        msg = Float64()

        # Simulate RPM between 0 and 300 (replace with real sensor data later)
        msg.data = round(random.uniform(0.0, 300.0), 2)

        self.pub.publish(msg)

        # Log what was published so you can see it in the terminal
        self.get_logger().info(f"Published RPM: {msg.data}")


def main(args=None):
    rclpy.init()
    rpm_pub = RPMPublisher()
    print("RPM Publisher Node Running...")

    try:
        rclpy.spin(rpm_pub)
    except KeyboardInterrupt:
        print("Terminating Publisher...")
        rpm_pub.destroy_node()


if __name__ == "__main__":
    main()