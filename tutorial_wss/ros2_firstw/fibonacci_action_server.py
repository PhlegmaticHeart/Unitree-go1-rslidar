import time

import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node

from action_tutorials_interfaces.action import Fibonacci


class FibonacciActionServer(Node):

    def __init__(self):
        super().__init__('fibonacci_action_server')
        self._action_server = ActionServer(
            self,
            Fibonacci,
            'fibonacci',
            self.execute_callback)
    def execute_callback(self, goal_handle):
        self.get_logger().info('Executing goal...')

        if goal_handle.request.order<=46:

            feedback_msg = Fibonacci.Feedback()
            feedback_msg.partial_sequence = [0, 1]
            for i in range(1, goal_handle.request.order):
                feedback_msg.partial_sequence.append(
                    feedback_msg.partial_sequence[i] + feedback_msg.partial_sequence[i-1])
                self.get_logger().info('Feedback: {0}'.format(feedback_msg.partial_sequence))
                goal_handle.publish_feedback(feedback_msg)
                time.sleep(1/3)

            result = Fibonacci.Result()
            result.sequence = feedback_msg.partial_sequence
            result.error_code = 0
            result.error_message = ""

            goal_handle.succeed()

            return result
        else:
            result = Fibonacci.Result()
            result.sequence = []
            result.error_code = 1
            result.error_message="you fool"

            goal_handle.succeed()

            return result
def main(args=None):
    rclpy.init(args=args)

    fibonacci_action_server = FibonacciActionServer()

    rclpy.spin(fibonacci_action_server)


if __name__ == '__main__':
    main()
