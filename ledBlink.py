#Shu Raturi
#Makes an LED blink forever by decreasing and increasing its brightness on the breadboard.
from machine import Pin, PWM
from time import sleep, time

led = PWM(Pin(20))
led.freq(1000)

while True:
    # Increasing brightness
    for brightness in range(0, 65536, 200):
        led.duty_u16(brightness)
        sleep(2 / (65536 / 200))

    # Decreasing brightness
    for brightness in range(65536, 0, -200):
        led.duty_u16(brightness)
        sleep(2 / (65536 / 200))
