source /opt/ros/humble/setup.sh
export RMW_IMPLEMENTATION=rmw_fastrtps_cpp
[ -t 0 ] && export ROS_SUPER_CLIENT=True || export ROS_SUPER_CLIENT=False
export ROS_DOMAIN_ID=1
export ROS_DISCOVERY_SERVER=10.5.112.149:11811
source ~/turtlebot4_ws/install/setup.sh