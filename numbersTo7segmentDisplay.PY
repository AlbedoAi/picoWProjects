#Shu Raturi
#Uses a 7segment display to show numbers between 1-9 running constantly.

from machine import Pin
import utime
pins = [Pin(12, Pin.OUT), #MIDDLE
        Pin(13, Pin.OUT), #TOP LEFT
        Pin(14, Pin.OUT), #TOP
        Pin(15, Pin.OUT), #TOP RIGHT
        Pin(17, Pin.OUT), #BOTTOM RIGHT
        Pin(18, Pin.OUT), #BOT
        Pin(19, Pin.OUT), #BOT LEFT
        Pin(16, Pin.OUT)] #DOT PIN

numbers = [[0,1, 1, 1, 1, 1, 1, 1], #0 common cathode
           [0,0, 0, 1, 1, 0, 0, 1], #1
           [1,0, 1, 1, 0, 1, 1, 1], #2
           [1,0, 1, 1, 1, 1, 0, 1], #3
           [1,1, 0, 1, 1, 0, 0, 1], #4
           [1,1, 1, 0, 1, 1, 0, 1], #5
           [1,1, 1, 0, 1, 1, 1, 1], #6
           [0,0, 1, 1, 1, 0, 0, 1], #7
           [1,1, 1, 1, 1, 1, 1, 1], #8
           [1,1, 1, 1, 1, 0, 0, 1]] #9
def clear():
    for i in pins:
        i.value(0)
clear()
while True:
    for i in range(len(numbers)):
        for j in range(len(pins)):
            pins[j].value(numbers[i][j])
        utime.sleep(1)

