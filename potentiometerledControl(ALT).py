#Shu Raturi
#Uses three potentiometers inputs to change the values of three different leds
from machine import Pin, PWM, ADC

red_led = PWM(Pin(11))
green_led = PWM(Pin(12))
blue_led = PWM(Pin(13))

red_led.freq(1000)
green_led.freq(1000)
blue_led.freq(1000)

red_adc = ADC(Pin(28))
green_adc = ADC(Pin(27))
blue_adc = ADC(Pin(26))

while True:
	red_value = red_adc.read_u16()
	green_value = green_adc.read_u16()
	blue_value = blue_adc.read_u16()

	red_led.duty_u16(red_value)
	green_led.duty_u16(green_value)
	blue_led.duty_u16(blue_value)
