#Shu Raturi
#Gets the input from a button and prints to the terminal when the button is pressed and released
import utime
from itsc305gpiozero import Button

def button_pressed():
    global start_time
    start_time = utime.ticks_ms()
    print("Button pressed")


def button_released():
    global start_time
    elapsed_time = utime.ticks_diff(utime.ticks_ms(), start_time) / 1000.0
    print("Button released")
    print(f"Button pressed for {elapsed_time:.2f} seconds")


def main():
    button = Button(15, pull_up=True, bounce_time=50)

    button.when_pressed = button_pressed
    button.when_released = button_released

    while True:
        pass

main()
