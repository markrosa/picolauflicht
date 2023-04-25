import time
from machine import Pin

level_1 = machine.Pin(2, Pin.IN, Pin.PULL_UP)
level_2 = machine.Pin(3, Pin.IN, Pin.PULL_UP)
level_3 = machine.Pin(4, Pin.IN, Pin.PULL_UP)


while True:
    level_value = level_1.value()
    print("Levels are : ", level_1.value(), ", ", level_2.value(), ", ", level_3.value())
    time.sleep(1)