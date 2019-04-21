import sys
import time
import random
from enum import Enum


def write(s):
    sys.stdout.write(s)
    sys.stdout.flush()


block = "█"
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

up = lambda a: "\u001b[" + str(a) + "A"
down = lambda a: "\u001b[" + str(a) + "B"
right = lambda a: "\u001b[" + str(a) + "C"
left = lambda a: "\u001b[" + str(a) + "D"


class Drawable:
    size = list()
    x = int()
    y = int()
    colour = str()

    def __str__(self):
        return "<Drawable; size: " + str(self.size) + " coords: " + str(self.coords) + ">"

    __repr__ = __str__


#UP_RIGHT = 1
#DOWN_RIGHT = 2
#DOWN_LEFT = 3
#UP_LEFT = 4


class Ball(Drawable):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = [1, 1]
        self.colour = red
        self.velocity = 0
        self.direction = 2

    def flip_vert(self):
        if self.direction == 1:
            self.direction = 2
        elif self.direction == 2:
            self.direction = 1
        elif self.direction == 3:
            self.direction = 4
        elif self.direction == 4:
            self.direction = 3

    def flip_horiz(self):
        if self.direction == 1:
            self.direction = 4
        elif self.direction == 2:
            self.direction = 3
        elif self.direction == 3:
            self.direction = 2
        elif self.direction == 4:
            self.direction = 1

    def tick(self):
        cleanup(self)
        if (self.y >= 24 or self.y <= 1):
            self.flip_vert()
        if (self.x >= 80 or self.x <= 1):
            self.flip_horiz()
        if self.direction == 1:
            self.y -= self.velocity
            self.x += self.velocity
        elif self.direction == 2:
            self.y += self.velocity
            self.x += self.velocity
        elif self.direction == 3:
            self.y += self.velocity
            self.x -= self.velocity
        elif self.direction == 4:
            self.y -= self.velocity
            self.x -= self.velocity
        draw(self)



def goto(x, y):
    write("\u001b[" + str(y) + ";" + str(x) + "H")


def clear_screen():
    write("\033[2J")
    goto(0, 0)


def set_background_colour(colour):
    goto(0, 0)
    for i in range(23):
        write(colour + block * 80)
        goto(0, i)
    goto(0, 0)


def draw(obj):
    if not isinstance(obj, Drawable):
        raise Exception("Tried to draw a non-drawable")

    if obj.size[0] == 1 and obj.size[1] == 1:
        goto(obj.x, obj.y)
        write(obj.colour)
        write(block)
        return
    goto(obj.x, obj.y)
    write(obj.colour)
    for i in range(obj.size[1]):
        write(block * obj.size[0])
        goto(obj.x, obj.y + i)
    return

def cleanup(obj):
    if not isinstance(obj, Drawable):
        raise Exception("Tried to cleanup a non-drawable")

    if obj.size[0] == 1 and obj.size[1] == 1:
        goto(obj.x, obj.y)
        write(obj.colour)
        write(" ")
        return
    goto(obj.x, obj.y)
    write(obj.colour)
    for i in range(obj.size[1]):
        write(" " * obj.size[0])
        goto(obj.x, obj.y + i)
    return


def randcolour():
    return str(random.choice(list(colours.values())))


try:
    write("\u001b[?25l")
    ball = Ball(40, 12)
    clear_screen()
    while True:
        ball.velocity = 1
        ball.tick()
        time.sleep(0.1)
except KeyboardInterrupt as e:
    write("\u001b[?25h")
    raise e
