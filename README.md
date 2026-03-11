# ROS2 Basic Nodes

This repository contains my foundational ROS2 Python scripts. I am using these to understand core communication protocols while running ROS2 on WSL.

## Contents
* **Topics:** `rpm_pub.py`, `publish.py`, and `publisher.py` simulate publishing sensor data (like wheel RPM) and basic string messages.
* **Services:** `service_client.py` handles synchronous request/response logic for evaluating numbers. `picture_server.py` and `picture_client.py` are the structural setup for a request/response system.
* **Actions:** `action_server.py` and `action_client.py` implement a custom `Maps` action. The client sends XYZ coordinates, and the server calculates the distance, providing continuous feedback until the goal is reached.
