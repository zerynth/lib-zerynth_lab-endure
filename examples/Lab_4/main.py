################################################################################
# Workshop - Lab 4
#
# Created: 2016-05-31 17:51:15.706452
#
################################################################################

import streams
from zerynth_lab.endure.temp_hum_click import temp_hum_click
from zerynth_lab.endure.eight_click import eight_click
 
# Create a serial console
streams.serial()
sleep(1000)
print("^^^^^^EndurePisa^^^^^^")
 
# Temp and humidity sensor
temp_hum = temp_hum_click.TempHumClick(I2C1, D38)
display = eight_click.LedDisplay(D17)
display_speed = 100
 
 
def system_setup():
    pinMode(LED1, OUTPUT)
    pinMode(LED2, OUTPUT)
    pinMode(LED3, OUTPUT)
    pinMode(LED4, OUTPUT)
    pinMode(D24, INPUT)
    pinMode(A1, INPUT)
    onPinFall(A1, btn_press_b)
    display.shutdown(0,False)
 
# LAB 1 - Flashing LEDs
def flash_led(led, delay):
    while True:
        pinToggle(led)
        sleep(delay)
 
# LAB 2 - Polling and Interrupts
def btn_press_a():
    global display_speed
 
    while True:
        sleep(100)
        if digitalRead(D24) == 1:
            print("Button A Pressed")
            display_speed -= 100
            if display_speed < 100:
                display_speed = 10
 
def btn_press_b():
    global display_speed
    print("Button B Pressed")
    display_speed += 100
 
 
# LAB 3 - I2C Sensors
def print_temp_humidity():
 
    while True:
        tmp, hum = temp_hum.get_temp_humidity()
        print("Temp is:", tmp, "Humidity is:", hum)
        sleep(2000)
 
# LAB 4 - Adding SPI Display
def led_display():
    intensity = 10
 
    while True:
        for row in range(8):
            for col in range(8):
                display.set_led( 0, col, row, 1 )
                sleep(display_speed)
                display.clear_display(0)
 
        display.set_intensity( 0, intensity )
        intensity += 1
 
        if intensity > 16:
            intensity = 0
 
 
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
thread(led_display)
