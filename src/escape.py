import sys
import time
import random

black = "\u001b[30;1m"
red = "\u001b[31;1m"
green = "\u001b[32;1m"
yellow = "\u001b[33;1m"
blue = "\u001b[34;1m"
magenta = "\u001b[35;1m"
cyan = "\u001b[36;1m"
white = "\u001b[37;1m"
reset = "\u001b[0m"
colours = {"black": black, "red": red, "green": green, "yellow": yellow, "blue": blue, "magenta": magenta, "cyan": cyan, "white": white}


def randcolour():
    return str(random.choice(list(colours.values())))


bblack = "\u001b[30"
bred = "\u001b[31"
bgreen = "\u001b[32"
byellow = "\u001b[33"
bblue = "\u001b[34"
bmagenta = "\u001b[35"
bcyan = "\u001b[36"
bwhite = "\u001b[37"

backgroundred = "\u001b[41m"
write = sys.stdout.write

block = "█"

up = "\u001b[{1}A"
down = "\u001b[{1}B"
right = "\u001b[{1}C"
left = "\u001b[{5}H"
while True:
    write(randcolour())
    write(block * 5)
    write(left)
    write(reset)
