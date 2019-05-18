import smbus
import time

I2CADDR = 0x24

bus = smbus.SMBus(1)

bus.write_byte_data(I2CADDR,0x03,0x00)
bus.write_byte_data(I2CADDR,0x01,0x03)
time.sleep(1)
bus.write_byte_data(I2CADDR,0x03,0x00)
bus.write_byte_data(I2CADDR,0x01,0x02)
time.sleep(1)
bus.write_byte_data(I2CADDR,0x03,0x00)
bus.write_byte_data(I2CADDR,0x01,0x01)
time.sleep(1)
bus.write_byte_data(I2CADDR,0x03,0x00)
bus.write_byte_data(I2CADDR,0x01,0x00)








