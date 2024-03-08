#Shu Raturi
#Simple scanning script to get information on the i2c display
import machine
sda = machine.Pin(0)
scl = machine.Pin(1)
i2c = machine.I2C(0, sda=sda, scl=scl, freq=400000)
print(i2c.scan())
