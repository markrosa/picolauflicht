import time
from machine import Pin

level_1 = machine.Pin(2, Pin.IN, Pin.PULL_DOWN)
level_2 = machine.Pin(3, Pin.IN, Pin.PULL_DOWN)
level_3 = machine.Pin(4, Pin.IN, Pin.PULL_DOWN)
level_4 = machine.Pin(5, Pin.IN, Pin.PULL_DOWN)


while True:
    level_value = level_1.value()
    print("Levels are : ", level_1.value(), ", ", level_2.value(), ", ", level_3.value(), ", ", level_4.value())
    time.sleep(1)