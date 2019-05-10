import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(11, GPIO.IN) # hardware debounced
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # software debounced

while True:
    if (GPIO.input(4) == 0):
        print("software debounce works")
    if (GPIO.input(11) == 1):
        print("hardware debounce works")
    time.sleep(1)
