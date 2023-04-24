import time
from lib.neopixel import Neopixel
# https://github.com/blaz-r/pi_pico_neopixel

# Streifen mit 30 Leds an Pin 28
pixels = Neopixel(num_leds=300, state_machine=0, pin=15, mode="GRB")
 
# einige Farben 
red = (255, 0, 0)
orange = (255, 50, 0)
yellow = (255, 100, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
indigo = (100, 0, 90)
violet = (200, 0, 100)

# Initialisierung
pixels.brightness(20)
pixels.clear()
pixels.show()

# pixels.fill(red)
# pixels.clear()

# pixels[3] = blue
# pixels.set_pixel(14, blue)
# pixels.set_pixel(15, green, 1)
# pixels.set_pixel_line(10, 15, indigo)
# pixels.show()

# pixels.set_pixel_line_gradient(10, 20, blue, red)
# pixels.rotate_right(5)



