import time
import RPi.GPIO as g

pins=[5, 6, 12, 13, 16, 19, 20, 26]

g.setmode(g.BCM)

for i in pins:
    g.setup(i,g.OUT)

while True:
    g.output(pins, 1)
    time.sleep(0.4)
    g.output(pins,0)
    time.sleep(0.4)
