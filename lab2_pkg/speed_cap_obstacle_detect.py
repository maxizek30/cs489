import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist  # Use the correct message type (Twist)
from std_msgs.msg import Header  # For using headers in the lights message

# Assuming LightringLeds is a valid class from your codebase or custom message
# from your_custom_msgs.msg import LightringLeds  # Uncomment and use if it's a custom message

class SpeedCapObstacleDetect(Node):
    def __init__(self):
        # Initialize the node with the name 'speed_cap'
        super().__init__('speed_cap')

        # Create a subscription to 'cmd_vel_unfiltered' topic with Twist message type
        self.speed_cap_subscriber = self.create_subscription(Twist, '/robot1/cmd_vel_unfiltered', self.speed_cap_callback,  10)
        self.speed_cap_subscriber
        
    def speed_cap_callback(self, msg):
        # Assuming LightringLeds is a custom message type and initialized properly
        lights = LightringLeds()  # Replace with actual message
        lights.header.stamp = self.get_clock().now().to_msg()
        lights.override_system = True

        # Get the linear velocity from the Twist message (only considering x direction)
        speedometer = msg.linear.x
        self.get_logger().info(f"Received speed: {speedometer}")

        # Cap speed at 0.4 and adjust the lights accordingly
        if speedometer > 0.4:
            speedometer = 0.4
            for i in range(6):  # Assuming we have 6 LEDs to control
                lights.leds[i].red = 255
                lights.leds[i].green = 0
                lights.leds[i].blue = 0

        # Log the speed
        self.get_logger().info(f"Speed after cap: {speedometer}")

def main(args=None):
    rclpy.init(args=args)

    # Create an instance of the node
    node = SpeedCapObstacleDetect()

    # Keep the node spinning to process callbacks
    rclpy.spin(node)

    # Clean up and shut down when done
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()


