from imu import MPU6050
from machine import I2C, Pin
from dht import DHT11
import I2C_LCD_display
import utime as time
import math

#LCD
mylcd = I2C_LCD_display.lcd()

#DHT11 sensor
myPin = Pin(16, Pin.OUT, Pin.PULL_DOWN)
sensor = DHT11(myPin)

#MPU 6050 sensor
i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)
mpu = MPU6050(i2c)

#Rotary variables
DT_Pin = Pin(26, Pin.IN, Pin.PULL_UP)
CLK_Pin = Pin(27, Pin.IN, Pin.PULL_UP)
SW = Pin(22, Pin.IN, Pin.PULL_UP)
value = 0
previousValue = 1
sw_state = 0

#Displays the temperature
def calculate_temperature():
    global sw_state #toggling between f and c
    sensor.measure() #gets the readings
    tempC = sensor.temperature
    hum = sensor.humidity
    strHum = str(hum)
    strTemp = str(tempC)
    tempF = (float(strTemp)*9/5+32)
    strTempF = str(tempF)
    print("\r", 'Temp= ', tempC, chr(176) + 'C ', 'Humidity = ', hum, '%', end='')
    mylcd.lcd_display_string("Humidity: " + strHum + "%" , 1, 0)
    if sw_state == 0:
        mylcd.lcd_display_string("Temp: " + strTemp + "C" , 2, 0)
    else:
        mylcd.lcd_display_string("Temp: " + strTempF + "F" , 2, 0)

#Calculates the tilt of the sensor
def calculate_angle():
    zAccel = mpu.accel.z
    if zAccel > 1:
        zAccel = 1
    theta=math.acos(zAccel)
    thetaDeg = theta/2/math.pi*360
    strThetaDeg = str(thetaDeg)
    print('Tilt Angle: ', thetaDeg, ' Degrees')
    mylcd.lcd_display_string("Tilt Angle: " + strThetaDeg , 1, 0)

#Checks when the rotary is being turned
def rotary_changed():
    global previousValue
    global value
    global sw_state
    if previousValue != CLK_Pin.value():
        if CLK_Pin.value() == 0:
            if DT_Pin.value() == 0:
                value = (value - 1)%2
                print("anti-clockwise", value)
            else:
                value = (value + 1)%2
                print("clockwise", value)
        previousValue = CLK_Pin.value()
    if SW.value() == 0:
        mylcd.lcd_clear()
        sw_state = 1 - sw_state
        time.sleep(.1)
    return value

previous_rotary_value = None
while True:

    #makes it so lcd clear runs once every time rotary value is changed
    current_rotary_value = rotary_changed()
    if current_rotary_value != previous_rotary_value:
        mylcd.lcd_clear()
    if current_rotary_value == 0:
        calculate_angle()
    elif current_rotary_value == 1:
        calculate_temperature()
    previous_rotary_value = current_rotary_value


