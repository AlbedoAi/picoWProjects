#Shu Raturi
#Activates the onboard led on the pico w and makes it blink
from itsc305gpiozero import *
from time import *

led_on_Board = LED("LED")

while(True):
    led_on_Board.value = 1
    sleep(1)
    led_on_Board.value = 0
    sleep(1)
