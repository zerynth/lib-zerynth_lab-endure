################################################################################
# Workshop - Lab 1
#
# Created: 2016-05-31 19:07:32.793231
#
################################################################################

import streams
 
# Create a serial console
streams.serial()
sleep(1000)
print("^^^^^^EndurePisa^^^^^^")
 
def system_setup():
    pinMode(LED1, OUTPUT)
    pinMode(LED2, OUTPUT)
    pinMode(LED3, OUTPUT)
    pinMode(LED4, OUTPUT)
 
# LAB 1 - Flashing LEDs
def flash_led(led, delay):
    while True:
        pinToggle(led)
        sleep(delay)
 
# Setup the system
system_setup()
 
# create the various threads using the same
# function but passing different parameters
thread(flash_led, LED1, 500)
thread(flash_led, LED2, 1100)
thread(flash_led, LED3, 2000)
thread(flash_led, LED4, 100)
