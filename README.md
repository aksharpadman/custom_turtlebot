## Custom turtlebot 

### Prerequisites
1. Gazebo classic
2. ROS 1

### Setup 

Clone the repo into your ros workspace 

```sh
    cd <catkin_ws>/src
     git clone https://github.com/aksharpadman/custom_turtlebot.git 
```
Build the repo

```sh
    #From the root of ros workspace run
    catkin_make
```
Source the environment
```sh
    echo "source <catkin_ws>/devel/setup.bash" >> ~/.bashrc 
```

### Launch simulation

Open a new terminal and launch gazebo simulation
```sh
    roslaunch custom_turtlebot turtle.launch
```
Open another terminal and run
```
    rosrun custom_turtlebot move_around.py
```

### Usage
Keyboard commands are used to control the motion of the vehicle. Use the following keyboardbinding to move the vehicle.
```
Moving around:
   u(turn  left)                i(forward)          o(turn right)
   j (rotate left)              k (No binding)      l(rotate right)
   m (turn left in reverse)     ,(backward)         .(turn right in reverse)
   ```