import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(10, GPIO.IN)
GPIO.setup(9, GPIO.IN)
GPIO.setup(11, GPIO.IN) 

def my_callback(channel):
 print('Callback one')

GPIO.add_event_callback(10, my_callback, bouncetime=200)

def my_callback_two(channel):
    print('Callback two')

GPIO.add_event_callback(9, my_callback, bouncetime=200)

def my_callback_two(channel):
    print('Callback three')

GPIO.add_event_callback(11, my_callback, bouncetime=200)
