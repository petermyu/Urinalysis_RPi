from time import sleep
import picamera
import picamera.array
import RPi.GPIO as GPIO
import datetime as dt
import numpy as np

def image_acq():

	led1 = 26
	led2 = 16
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(led1,GPIO.OUT)
	GPIO.setup(led2,GPIO.OUT)
	camera = picamera.PiCamera()
	camera.resolution = (1024, 768)
	GPIO.output(led1, GPIO.HIGH)
	GPIO.output(led2,GPIO.HIGH)
	print("LED on")
	camera.awb_mode = 'shade'
	camera.shutter_speed = camera.exposure_speed
	#camera.exposure_mode = 'off'
	camera.start_preview()
	# Camera warm-up time
	sleep(5)
	print("starting camera.....\n")
	camera.stop_preview()

	date = dt.datetime.now().strftime('%Y_%m_%d_%h_%m_%s')
	image_name = '/home/pi/sd/data/' + date 
	rgb_file = open(image_name+'_rgb.data', 'w+b')
	camera.capture(image_name+ '.png',) 
	print("picture captured as: " + image_name)
	#camera.capture(rgb_file, 'rgb')
	#fwidth = (width + 31) // 32*32
	#fheight = (height)
	#image = np.fromfile(image_name, dtype=np.uint8).\reshape((fheight, fwidth, 3))[:height, :width, :]

	with picamera.array.PiRGBArray(camera) as output:
		camera.capture(output, 'rgb')
		print('captured %d%d image' % (output.array.shape[1], output.array.shape[0]))
		print(output.array)
		rgb_file.write(output.array)
	#print(image))
	sleep(5)
	GPIO.output(led1, GPIO.LOW)
	GPIO.output(led2,GPIO.LOW)
	print("LED off")
