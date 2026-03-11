#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

import math

WHEEL_RADIUS = 0.35  # Radius of the wheel in meters (adjust to match your wheel)

class RPMSubscriber(Node):
    def __init__(self):
        super().__init__("rpm_subscriber_node")

        # Subscribe to the same topic "wheel_rpm" the publisher is sending to
        self.sub = self.create_subscription(Float64, "wheel_rpm", self.rpm_callback, 10)

    def rpm_callback(self, msg):
        rpm = msg.data

        # Formula: Speed (m/s) = (RPM × 2π × radius) / 60
        speed_ms  = (rpm * 2 * math.pi * WHEEL_RADIUS) / 60

        # Convert to km/h for easier understanding
        speed_kmh = speed_ms * 3.6

        self.get_logger().info(
            f"RPM: {rpm:.2f} | Speed: {speed_ms:.3f} m/s | {speed_kmh:.3f} km/h"
        )


def main(args=None):
    rclpy.init()
    rpm_sub = RPMSubscriber()
    print("RPM Subscriber Node Running... Waiting for RPM data.")

    try:
        rclpy.spin(rpm_sub)
    except KeyboardInterrupt:
        print("Terminating Subscriber...")
        rpm_sub.destroy_node()


if __name__ == "__main__":
    main()