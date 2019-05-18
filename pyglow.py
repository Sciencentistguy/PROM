#####
#
# PyGlow
#
#####
#
# Python module to control Pimoronis PiGlow
# [http://shop.pimoroni.com/products/piglow]
#
# * test.py - set brightness for each color individually
#
#####


import time
from PyGlow import PyGlow

def pyglw():
    pyglow = PyGlow()
    pyglow.color("white", 236)
    time.sleep(0.5)
    pyglow.color("blue", 129)
    time.sleep(0.5)
    pyglow.color("green", 52)
    time.sleep(0.5)
    pyglow.color("yellow", 106)
    time.sleep(0.5)
    pyglow.color("orange", 23)
    time.sleep(0.5)
    pyglow.color("red", 98)
    time.sleep(0.5)
    pyglow.all(200)
    time.sleep(1)
    pyglow.color("white", 0)
    pyglow.color("blue", 0)
    pyglow.color("green", 0)
    pyglow.color("yellow", 0)
    pyglow.color("orange", 0)
    pyglow.color("red", 0)
    pyglow.all(0)
