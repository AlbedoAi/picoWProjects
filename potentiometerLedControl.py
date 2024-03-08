#Shu Raturi
#Use the potentiometer input to increaser and decrease the brightness of the led.
from machine import Pin, PWM, ADC

led = PWM(Pin(20))
adc = ADC(Pin(28))

led.freq(1000)

while True:
	brightness = adc.read_u16()
	led.duty_u16(brightness)
