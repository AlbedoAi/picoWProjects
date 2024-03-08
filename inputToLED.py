#Shu Raturi
#Use button and a switch to get inputs, then uses the input to turn the LED. If the the switch is on it will turn on the blue led,
#and if the button is pressed when the switch is on it will light up the red and green led. If the switch is off the button press will only light up the red led.


import utime
from itsc305gpiozero import *

global toggle_state
toggle_state = False
def main():
    button = Button(14, pull_up=True, bounce_time=50)
    switch = Button(17, pull_up=False, bounce_time=50)
    button.when_pressed = button_pressed
    button.when_released = button_released
    switch.when_pressed = switch_toggle
    while(True):
        pass

def button_pressed():
    red_led = LED(15)
    red_led.value = 1
    print("Button pressed")
    green_led = LED(13)

    global toggle_state
    if toggle_state:
        green_led.value = 1

def button_released():
    red_led = LED(15)
    red_led.value = 0
    print("Button released")
    green_led = LED(13)
    green_led.value = 0

def switch_toggle():
    global toggle_state
    blue_led = LED(12)
    toggle_state = not toggle_state
    print(toggle_state)
    if toggle_state == 0:
        blue_led.value = 0
    else:
        blue_led.value = 1



main()
