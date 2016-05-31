################################################################################
# Workshop - Lab 3
#
# Created: 2016-05-31 16:27:45.901545
#
################################################################################

import streams
from zerynth_lab.endure import temp_hum_click

# Create a serial console
streams.serial()
sleep(1000)
print("^^^^^^EndurePisa^^^^^^")
 
# Temp and humidity sensor
try:
    temp_hum = temp_hum_click.TempHumClick(I2C1,D38)
except Exception as e:
    print(e)
    
def system_setup():
    pinMode(LED1, OUTPUT)
    pinMode(LED2, OUTPUT)
    pinMode(LED3, OUTPUT)
    pinMode(LED4, OUTPUT)
    pinMode(D24, INPUT)
    pinMode(A1, INPUT)
    onPinFall(A1, btn_press_b)

# LAB 1 - Flashing LEDs
def flash_led(led, delay):
    while True:
        pinToggle(led)
        sleep(delay)

# LAB 2 - Polling and Interrupts
def btn_press_a():
    while True:
        sleep(100)
        if digitalRead(D24) == 1:
            print("Button A Pressed")

def btn_press_b():
    print("Button B Pressed")

# LAB 3 - I2C Sensors
def print_temp_humidity():
    while True:
        tmp, hum = temp_hum.get_temp_humidity()
        print("Temp is:", tmp, "Humidity is:", hum)
        sleep(2000)

# Setup the system
system_setup()

# create the various threads using the same
# function but passing different parameters
thread(flash_led, LED1, 500,  prio=PRIO_LOW)
thread(flash_led, LED2, 1100, prio=PRIO_LOW)
thread(flash_led, LED3, 2000, prio=PRIO_LOW)
thread(flash_led, LED4, 100,  prio=PRIO_LOW)
thread(print_temp_humidity,   prio=PRIO_HIGH)
thread(btn_press_a)
