import RPi.GPIO as GPIO
from race import Game

animations = ['animation_one', 'animation_two', 'animation_three', 'animation_four']

g = Game()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(g.get_switches(), GPIO_IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(g.target, GPIO.RISING, callback=g.fill(), bouncetime=200)
GPIO.add_event_detect(g.winner, GPIO.RISING, callback=g.play_winner(), bouncetime=200)
GPIO.add_event_detect(g.not_winner, GPIO.RISING, callback=g.play_not_winner(), bouncetime=200)
GPIO.add_event_detect(g.prepare, GPIO.RISING, callback=g.prepare(), bouncetime=200)

print(g.get_switches())