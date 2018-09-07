import subprocess
import RPi.GPIO as GPIO
import time
import os

Models = 'Matrix'
arguements = ['/opt/fpp/src/fppmm', '-m', 'a' , '-o', 'on']

my_env = {**os.environ, 'PATH': '/usr/sbin:/sbin:' + os.environ['PATH']}
fill_trigger = 12
start_trigger = 20
end = 16
not_winner = 17
counter = 1

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(fill_trigger, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(end, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(start_trigger, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def bash_command(cmd):
	subprocess.Popen(cmd, shell=True, executable = "/bin/bash")


def race_start(channel):
	for i in range(1, 16):
		arguements[2] = Models + str(i)
		subprocess.run(arguements)
	#subprocess.run(["/opt/fpp/bin.pi/fpp", "-d"])
	#time.sleep(5)
	bash_command("/opt/fpp/src//fpp -p spiral")
	#time.sleep(.5)
	#subprocess.run(["/opt/fpp/bin.pi/fpp", "-p", "SpiralPattern"])

def fill(channel):
	global counter
	print(counter)
	if counter < 16:
		arguements[2] = Models + str(counter)
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
