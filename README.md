# Robot-using-ROS-on-Raspberry
Control robot from laptop using 2 nodes and 2 nodes on raspberry

1. A RPI with 2 rosnodes:
      - One can control the robot speed by controlling 2 attached motors speed (differential wheel robot) (the topic name could be "/robot/move_speed"), the motor should be attached to the RPI through some motor shield, the controlling commands are to be sent from another rosnode on the laptop in "2". The node should. The node should publish its status, representing if the command is well executed or not.
    - The other rosnode should read data from an ultrasonic sensor attached to the RPI and publish its data to some topic (e.g. "/robot/ultrasound_sensor") representing the distance between the sensor and the nearest object in front of it in centimetres.
2. A laptop with 2 rosnodes:
    - One listens to the ultrasound data and decides on what speed should the robot move and publishes it.
    - The other rosnode should listens to the robot's moving status and show if the controlling commands done as expected or failed.
