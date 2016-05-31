################################################################################
# Workshop - Lab 2
#
# Created: 2016-05-31 16:27:45.901545
#
################################################################################

import streams
 
# Create a serial console
streams.serial()
sleep(1000)
print("^^^^^^EndurePisa^^^^^^")
 
def system_setup():
    global display
    pinMode(LED1, OUTPUT)
    pinMode(LED2, OUTPUT)
    pinMode(LED3, OUTPUT)
    pinMode(LED4, OUTPUT)
    pinMode(D24, INPUT_PULLDOWN)
    pinMode(A1, INPUT)
    onPinFall(A1, btn_press_b,debounce=100)

def flash_led(led, delay):
    while True:
        pinToggle(led)
        sleep(delay)

def btn_press_a():
    while True:
        sleep(100)
        if digitalRead(D24) == 1:
            print("Button A Pressed")

def btn_press_b():
    print("Button B Pressed")

# Setup the system
system_setup()

# create the various threads using the same
# function but passing different parameters
thread(flash_led, LED1, 500,  prio=PRIO_LOW)
thread(flash_led, LED2, 1100, prio=PRIO_LOW)
thread(flash_led, LED3, 2000, prio=PRIO_LOW)
thread(flash_led, LED4, 100,  prio=PRIO_LOW)
thread(btn_press_a)

