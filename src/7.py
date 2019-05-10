import smbus
import time

I2CADDR = 0x38

bus = smbus.SMBus(1)
digits = [0,1,2,3]

def displaydig(num):
    bus.write_byte(I2CADDR, num)

displaydig(3)
time.sleep(1)
displaydig(2)
time.sleep(1)
displaydig(1)
time.sleep(1)
displaydig(0)







