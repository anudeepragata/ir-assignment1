from functions import *
from controller import Robot, Motor, GPS
from math import *

TIME_STEP = 64

MAX_SPEED = 6.28

TARGET = point(0.75, 0)


# create the Robot instance.
robot = Robot()
gps = robot.getDevice('gps')
gps.enable(True)
compass = robot.getDevice('compass')
compass.enable(True)

# get a handler to the motors and set target position to infinity (speed control)
leftMotor = robot.getDevice('left wheel motor')
rightMotor = robot.getDevice('right wheel motor')
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))

# set up the motor speeds at 10% of the MAX_SPEED.
leftMotor.setVelocity(MAX_SPEED)
rightMotor.setVelocity(MAX_SPEED)

def get_bearing_in_degrees():
  north = compass.getValues()
  rad = atan2(north[1], north[0])
  bearing = (rad - 1.5708) / 180.0
  if (bearing < 0.0):
    bearing = bearing + 360.0
  return bearing

while robot.step(TIME_STEP) != -1:
   loc = point(gps.getValues()[0], gps.getValues()[1])
   line = line_2_points(loc, TARGET)
   bearing = get_bearing_in_degrees()
   print(bearing)
   
