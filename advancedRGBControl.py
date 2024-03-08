#Shu Raturi
#Uses a potentiometer, button and a rgb LED.
#The potetiometer increases the brightness of one of the R, G, B colours and the button switches between the three colours so the potentiometer can set the value of each rgb.

from machine import Pin, PWM, ADC
from time import sleep

btn = Pin(15, Pin.IN, Pin.PULL_UP)
red_led = PWM(Pin(11))
green_led = PWM(Pin(12))
blue_led = PWM(Pin(13))

red_led.freq(1000)
green_led.freq(1000)
blue_led.freq(1000)

green_adc = ADC(Pin(27))
toggle = 0

while True:
	if btn.value() == 0:
		toggle += 1
		sleep(0.5)
	elif toggle >= 3:
		toggle = 0

	if toggle == 1:
		red_value = green_adc.read_u16()
		red_led.duty_u16(red_value)
	elif toggle == 2:
		green_value = green_adc.read_u16()
		green_led.duty_u16(green_value)
	else:
		blue_value = green_adc.read_u16()
		blue_led.duty_u16(blue_value)




