from time import sleep
import picamera
import picamera.array
import RPi.GPIO as GPIO
import datetime as dt
import numpy as np


from motor_test import run_motor
from camera_test import image_acq
from Getting Graphs import image_analysis

print('running motor')
run_motor(0.05,2,3,17,27) #stepper motor 1

run_motor(0.05,14,15,18,22) #stepper motor 2

run_motor(0.05,23,24,10,9) #stepper motor 3
image_acq()


value = image_analysis()

