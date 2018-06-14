import subprocess
import RPi.GPIO as GPIO
import time


Models = ['Matrix1', 'Matrix2', 'Matrix3', 'Matrix4']
arguements = ['/opt/fpp/src/fppmm', '-m', 'a' , '-o', 'on']

fill_trigger = 23
start_trigger = 27
end = 26


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(fill_trigger, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(end, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(start_trigger, GPIO.IN, pull_up_down=GPIO.PUD_UP)
counter = 0

def race_start(channel):
	global counter
	counter = 0
	for i in Models:
		arguements[2] = i
		subprocess.run(arguements)

def fill(channel):
	global counter
	arguements[2] = Models[counter]
	arguements[4] = 'off'
	subprocess.run(arguements)
	counter += 1


GPIO.add_event_detect(start_trigger, GPIO.RISING, callback=race_start, bouncetime=200)
GPIO.add_event_detect(fill_trigger, GPIO.RISING, callback=fill, bouncetime=200)


try:
	GPIO.wait_for_edge(end, GPIO.RISING)
except KeyboardInterrupt:
	GPIO.cleanup()
GPIO.cleanup()
