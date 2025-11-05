import rclpy
from rclpy.node import Node
import time

class PickAndPlace(Node):
    def __init__(self):
        super().__init__('pick_and_place')
        self.objects = ['circle', 'square', 'triangle']
        self.current = 0
        self.get_logger().info('Pick-and-place simulation started!')
        self.timer = self.create_timer(5.0, self.pick_next)

    def pick_next(self):
        shape = self.objects[self.current]
        self.get_logger().info(f'Picking {shape} ...')
        time.sleep(1)
        self.get_logger().info(f'Placing {shape} into bin_{shape} ...')
        time.sleep(1)
        self.get_logger().info(f'{shape} placed successfully!')
        self.current = (self.current + 1) % len(self.objects)

def main(args=None):
    rclpy.init(args=args)
    node = PickAndPlace()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
