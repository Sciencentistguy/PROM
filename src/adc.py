import smbus
import time
I2CADDR = 0x21
CMD_CODE = 0b01000000
bus = smbus.SMBus(1)
bus.write_byte( I2CADDR, CMD_CODE )
tmp = bus.read_word_data( I2CADDR, 0x00 ) 
print(type(tmp))
print(tmp)
stmp="{0:1b}".format(tmp)
number=stmp[12:] + stmp[8:12] + stmp[4:8]+stmp[:4]
number=number[4:]
print(int(number,2))

