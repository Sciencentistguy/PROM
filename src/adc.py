import smbus
import time
I2CADDR = 0x21
CMD_CODE = 0b01000000
bus = smbus.SMBus(1)
bus.write_byte(I2CADDR, CMD_CODE)
tmp = bus.read_word_data(I2CADDR, 0x00)
print(type(tmp))
print(tmp)
top8 = tmp >> 8
print(top8)
bottom8 = tmp & 0b11111111
print(bottom8)
tmp2 = (bottom8 << 8) + top8
print(tmp2)
tmp3 = tmp2 & 0b111111111111
print(tmp3)
