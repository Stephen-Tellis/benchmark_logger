#!/usr/bin/env python3

# Local classes libs
from benchmark_logger.monitor import Monitor

# Python libs
from datetime import datetime

# ROS client libs
import rclpy
from rclpy.node import Node

# Import ros msgs
from std_msgs.msg import Empty


class Subscriber(Node):
    def __init__(self):
        super().__init__("log_now")
        self.log_datasubscription = self.create_subscription(
            Empty, "benchmark_logger", self._listener_callback, 1
        )
        curDT = datetime.now()
        self.systemstats = Monitor(fname=curDT.strftime("%m-%d-%Y-%H-%M-%S"))

    def _listener_callback(self, msg):
        self.systemstats.log_all_stats()


def ros_main(args=None):
    rclpy.init(args=args)

    subscriber = Subscriber()

    rclpy.spin(subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    subscriber.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    ros_main()
