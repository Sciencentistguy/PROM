import smbus
import time
I2C_ADDR = 0x38
LED_ON = 0x00
LED_OFF = 0xFF
led_codes = [x for x in range(0xFF)]
bus = smbus.SMBus(1)

def activate_led(number):
    i=1#led decode code
    bus.write_byte(I2C_ADDR, i)

def reset_leds():
    bus.write_byte(I2C_ADDR, LED_OFF)

for i in led_codes:
    bus.write_byte(I2C_ADDR, i)
    print(i)
    time.sleep(1)
    bus.write_byte(I2C_ADDR, LED_OFF)

#while True:
#    bus.write_byte(I2C_ADDR, LED_ON)
#    time.sleep(1)
#    bus.write_byte(I2C_ADDR, LED_OFF)
#    time.sleep(1)
