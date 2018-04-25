import RPi.GPIO as GPIO
from time import sleep

def step(w1,w2,w3,w4):
		GPIO.output(Motor1,w1)
		GPIO.output(Motor2,w2)
		GPIO.output(Motor3,w3)
		GPIO.output(Motor4,w4)
		sleep(delay)
		
def run_motor(delay,m1,m2,m3,m4):
	GPIO.cleanup()
	GPIO.setmode(GPIO.BCM) #sets board to GPIO pin mode
	enable = 4 
	Motor4= 27#10 B2
	Motor3= 17 #9 A2
	Motor2= 3# B1
	Motor1 = 2 #A1
	GPIO.setup(enable, GPIO.OUT)
	GPIO.setup(Motor1,GPIO.OUT) #motor 1 direction A
	GPIO.setup(Motor2,GPIO.OUT) #motro 1 direction B
	GPIO.setup(Motor3,GPIO.OUT) #eturns motor on
	GPIO.setup(Motor4,GPIO.OUT) #eturns motor on

	GPIO.output(enable, GPIO.HIGH)
	#pwm=GPIO.PWM(Motor1E,100)
	#pwm.start(0)
	print "Turning motor on" #direction A
	
		
	for x in range (0,100):
		GPIO.output(Motor1,GPIO.HIGH)
		GPIO.output(Motor2,GPIO.HIGH)
		GPIO.output(Motor3,GPIO.LOW)
		GPIO.output(Motor4,GPIO.LOW)
		
		sleep(delay)
		
		GPIO.output(Motor1,GPIO.LOW)
		GPIO.output(Motor2,GPIO.HIGH)
		GPIO.output(Motor3,GPIO.LOW)
		GPIO.output(Motor4,GPIO.LOW)
		sleep(delay)
		GPIO.output(Motor1,GPIO.LOW)
		GPIO.output(Motor2,GPIO.HIGH)
		GPIO.output(Motor3,GPIO.HIGH)
		GPIO.output(Motor4,GPIO.LOW)

		sleep(delay)

		GPIO.output(Motor1,GPIO.LOW)
		GPIO.output(Motor2,GPIO.LOW)
		GPIO.output(Motor3,GPIO.HIGH)
		GPIO.output(Motor4,GPIO.LOW)

		sleep(delay)

		GPIO.output(Motor1,GPIO.LOW)
		GPIO.output(Motor2,GPIO.LOW)
		GPIO.output(Motor3,GPIO.HIGH)
		GPIO.output(Motor4,GPIO.HIGH)
		sleep(delay)
		GPIO.output(Motor1,GPIO.LOW)
		GPIO.output(Motor2,GPIO.LOW)
		GPIO.output(Motor3,GPIO.LOW)
		GPIO.output(Motor4,GPIO.HIGH)
		sleep(delay)
		GPIO.output(Motor1,GPIO.HIGH)
		GPIO.output(Motor2,GPIO.LOW)
		GPIO.output(Motor3,GPIO.HIGH)
		GPIO.output(Motor4,GPIO.HIGH)
		
		sleep(delay)
		
		#step(1,1,0,0)
		#step(0,1,0,0)
		#step(0,1,1,0)
		#step(0,0,1,0)
		#step(0,0,0,1)
		#step(1,0,0,1)
		
	#print "Stopping motor"
	#GPIO.output(Motor1E,GPIO.LOW) 
	 
	GPIO.cleanup()
