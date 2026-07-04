import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/jesus-rivera/ros2_jazzy/turtlesim_ws/src/install/my_turtle_controller'
