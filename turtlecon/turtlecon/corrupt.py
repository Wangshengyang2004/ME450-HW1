"""Subscribes to a topic called pure_cmd_vel of type geometry_msgs/msg/Twist
For every pure_cmd_vel message receives publishes a corrupted version:
Gaussian Noise is added independently to the linear and rotational velocities
The noise is zero mean, with standard deviation proportional to noise_coefficient * |velocity|
The noise_coefficient is a parameter that defaults to 0.05"""