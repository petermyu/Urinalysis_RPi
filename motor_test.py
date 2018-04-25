import RPi.GPIO as GPIO
from time import sleep

global delay
def step(m1,m2,m3,m4,w1,w2,w3,w4):
		GPIO.output(m1,w1)
		GPIO.output(m2,w2)
		GPIO.output(m3,w3)
		GPIO.output(m4,w4)
		sleep(delay)
		
def run_motor(delay1,m1,m2,m3,m4):
	GPIO.cleanup()
	GPIO.setmode(GPIO.BCM) #sets board to GPIO pin mode
	Motor4 = m4 #10 B2
	Motor3 = m3 #9 A2
	Motor2 = m2 #B1
	Motor1 = m1 #A1
	global delay
	delay = delay1
	GPIO.setup(m1,GPIO.OUT) #motor 1 direction A
	GPIO.setup(m2,GPIO.OUT) #motro 1 direction B
	GPIO.setup(m3,GPIO.OUT) #eturns motor on
	GPIO.setup(m4,GPIO.OUT) #eturns motor on

	#pwm=GPIO.PWM(Motor1E,100)
	#pwm.start(0)
	print "Turning motor on" #direction A
	
		
	for x in range (0,100):	
		step(m1,m2,m3,m4,1,1,0,0)
		step(m1,m2,m3,m4,0,1,0,0)
		step(m1,m2,m3,m4,0,1,1,0)
		step(m1,m2,m3,m4,0,0,1,0)
		step(m1,m2,m3,m4,0,0,0,1)
		step(m1,m2,m3,m4,1,0,0,1)
		
	#print "Stopping motor"
	#GPIO.output(Motor1E,GPIO.LOW) 
	 
	GPIO.cleanup()
