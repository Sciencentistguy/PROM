import smbus
import time
I2C_ADDR = 0x38
LED_OFF = 0xFF
led_codes = [0xfe, 0xfb, 0xf7, 0xef, 0xdf, 0xbf, 0x7f]
bus = smbus.SMBus(1)


def activate_led(number):
    global I2C_ADDR, led_codes
    bus.write_byte(I2C_ADDR, led_codes[number])


def clear_led():
    global LED_OFF, I2C_ADDR
    bus.write_byte(I2C_ADDR, LED_OFF)
