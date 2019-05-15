import sys
import time
import random
from enum import Enum
import led
import adc
import buzzer
import constants

PI = True

if PI:
    from serial import Serial
    import smbus
    import RPi.GPIO as GPIO
    serialPort = Serial("/dev/ttyAMA0", 57600)
    if not serialPort.isOpen():
        serialPort.open()
    GPIO.setmode(GPIO.BCM)
    [GPIO.setup(x, GPIO.OUT) for x in [5, 6, 12, 13, 16, 19, 20, 26]]


def write(s, ser=True):
    global PI
    global serialPort
    if PI and ser:
        serialPort.write(bytes(s, "UTF-8"))
    else:
        sys.stdout.write(s)
        sys.stdout.flush()


modified = [[True for j in range(25)] for i in range(81)]

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
        return "<Drawable; size: " + str(self.size) + " x: " + str(self.x) + " y:" + str(self.y) + ">"

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
        self.velocity = 1
        self.direction = 2 if x < 40 else 3

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

    def collision_check(self, paddle):
        if self.y in range(paddle.y, paddle.y + paddle.size[1]):
            return True
        return False

    def __str__(self):
        return "<Ball; size: " + str(self.size) + " x: " + str(self.x) + " y:" + str(self.y) + ">"


class Paddle(Drawable):
    def __init__(self, x, y, length):
        self.x = x
        self.y = y
        self.size = [1, length]
        self.colour = yellow

    def __str__(self):
        return "<Paddle; size: " + str(self.size) + " x: " + str(self.x) + " y:" + str(self.y) + ">"


def goto(x, y, ser=True):
    write("\u001b[" + str(y) + ";" + str(x) + "H", ser)


def reset_led():
    led.clear_led()
    pins = [5, 6, 12, 13, 16, 19, 20, 26]
    GPIO.output(pins, False)


def set_led(led_n, state):
    pins = [5, 6, 12, 13, 16, 19, 20, 26]
    GPIO.output(pins[led_n], state)
    led.activate_led(led_n)


def clear_screen(ser=True):
    write("\u001b[2J", ser=ser)
    goto(0, 0, ser=ser)


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
        set_modified(obj.x, obj.y)
        return
    goto(obj.x, obj.y)
    write(obj.colour)
    for i in range(obj.size[1]):
        write(" " * obj.size[0])
        goto(obj.x, obj.y + i)
    return


def randcolour():
    return str(random.choice(list(colours.values())))


def draw_background():
    if True in modified[40]:
        write(white)
        for i in range(12):
            if i % 2 == 0:
                continue
            goto(40, i * 2)
            write(block)
            goto(40, (i * 2) + 1)
            write(block)
        modified[40] = [False for i in range(25)]


def draw_number(left, n, X=0):
    x = 30 if left else 48
    if not X == 0:
        x = X
    goto(x, 4)
    write(white)
    ls = open("ascii_numbers/" + str(n), "r").readlines()
    for c, i in enumerate(ls):
        write(i)
        goto(x, 2 + c)


def win(player):
    clear_screen()
    goto(12, 20)
    write(white)
    if player == 0:
        write("Congratulations, left has won!")
        return
    if player == 1:
        write("Congratulations, right has won!")


def get_controller_l_input():
    I2CADDR = 0x21
    CMD_CODE = 0b01000000
    bus = smbus.SMBus(1)
    bus.write_byte(I2CADDR, CMD_CODE)
    tmp = bus.read_word_data(I2CADDR, 0x00)
    top8 = tmp >> 8
    bottom8 = tmp & 0b11111111
    tmp2 = (bottom8 << 8) + top8
    tmp3 = tmp2 & 0b111111111111
    return tmp3


def set_modified(x, y):
    global modified
    modified[x][y] = True


def clear_modified():
    global modified
    modified = [[False for i in range(25)] for j in range(81)]


def start_game(ball, padl, padr):
    draw(ball)
    draw(padl)
    draw(padr)
    buzzer.dududududododoooooodododod()
    countdown()


def countdown():
    draw_number(True, 3, 39)
    time.sleep(0.8)
    draw_number(True, 2, 39)
    time.sleep(0.8)
    draw_number(True, 1, 39)
    time.sleep(0.8)


reset = False
last_win_left = False


def write_score(score):
    if score[0] > 9:
        win(0)
        time.sleep(10)
        exit()
    if score[1] > 9:
        win(1)
        time.sleep(10)
        exit(1)
    draw_number(True, score[0])
    draw_number(False, score[1])


def tick(ball, padl, padr):
    global reset
    global score
    global last_win_left
    global rand_speed
    draw_background()
    write_score(score)

    cleanup(ball)
    if (ball.y >= 24 or ball.y <= 1):
        ball.flip_vert()

    if ball.direction == 1:
        ball.y -= ball.velocity
        ball.x += ball.velocity
    elif ball.direction == 2:
        ball.y += ball.velocity
        ball.x += ball.velocity
    elif ball.direction == 3:
        ball.y += ball.velocity
        ball.x -= ball.velocity
    elif ball.direction == 4:
        ball.y -= ball.velocity
        ball.x -= ball.velocity


    if ball.x == 2 or ball.x == 78:
        if ball.collision_check(padl):
            ball.flip_horiz()
            rand_speed = random.choice([0.05, 0.04, 0.02, 0.06, 0.07, 0.1])
        if ball.collision_check(padr):
            ball.flip_horiz()
            rand_speed = random.choice([0.05, 0.04, 0.02, 0.06, 0.07, 0.1])
    if (ball.x >= 80):
        ball.flip_horiz()
        score[0] += 1
    if ball.x <= 1:
        ball.flip_horiz()
        score[1] += 1

    draw(ball)
    clear_screen(False)
    print(ball)
    print(padl)
    print(padr)
    print("<rand_speed; " + str(rand_speed) + ">")
    print("<scores; left: " + str(score[0]) + " right: " + str(score[1]) + ">")

    reset_led()
    if ball.x < 10:
        set_led(0, True)
    elif ball.x >= 80:
        set_led(7, True)
    else:
        set_led(int(str(ball.x)[0]), True)

    cleanup(padl)
    if PI:
        varistor_input = get_controller_l_input()
        print("<ADC 1; value: " + str(varistor_input) + ">")
        varistor_input *= (21 / 4096)
        padl.y = int(varistor_input) + 1
    draw(padl)

    cleanup(padr)
    varistor_input = adc.adc_run()
    print("<ADC 1; value: " + str(varistor_input) + ">")
    padr.y = int(varistor_input)
    draw(padr)

    if constants.random_speed:
        time.sleep(rand_speed)
    else:
        time.sleep(0.05)


try:
    padl = Paddle(3, 10, 4)
    padr = Paddle(78, 10, 4)
    write("\u001b[?25l")
    ball = Ball(40, 12)
    clear_screen()
    ball.velocity = 1
    score = [0, 0]
    start_game(ball, padl, padr)
    rand_speed = 0.05
    clear_screen()
    while True:
        tick(ball, padl, padr)
except KeyboardInterrupt as e:
    write("\u001b[?25h")
    raise e
