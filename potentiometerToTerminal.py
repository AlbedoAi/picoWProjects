#Shu Raturi
#Gets input from a potentiometer and displays it to the terminal as to how much it is rotated as a percentage.

import machine
import utime

analog_value = machine.ADC(28)

while True:
    reading = analog_value.read_u16()

    percentage_reading = int(((reading - 224) / (65535 - 224)) * 100)

    print("ADC Rotation: ", percentage_reading, "%")
    utime.sleep(0.2)
