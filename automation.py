from time import sleep
import picamera
import picamera.array
import RPi.GPIO as GPIO
import datetime as dt
import numpy as np


from motor_test import run_motor
from camera_test import image_acq
from getting_graphs import image_analysis

print('running motor')
len1 = 10;
len2 = 500;
len3 = 50;
len4 = 100;
fwd = 1;
back = 0;

#run_motor(0.01,2,3,17,27,back,len1) #stepper motor 1

run_motor(0.01,14,15,18,22,back,len2) #stepper motor 2

#run_motor(0.05,23,24,10,9,back,len3) #stepper motor 3
#run_motor(0.05,25,8,7,11,fwd,len4) #stepper motor 4

#image_acq()

#value = image_analysis()
#print('acquired value is ' + value)
