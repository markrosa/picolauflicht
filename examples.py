import time
from lib.neopixel import Neopixel
 
# Streifen mit 30 Leds an Pin 28
pixels = Neopixel(num_leds=300, state_machine=0, pin=15, mode="GRB")
 
# Einige Farben
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

def all_colors(start, stop, colors):
    pixels.clear()
    for i in range(100):
        col_index = i % len(colors)
        for pixel in range(start, stop+1):
            if col_index == 4: # blue
                pixels.set_pixel(pixel, colors[col_index], 150)
            else:
                pixels.set_pixel(pixel, colors[col_index])
            pixels.show()
            time.sleep(0.005)
            col_index += 1
            if col_index == len(colors):
                col_index = 0
   
def rotate_right(start, stop, start_color, stop_color):
    pixels.clear()
    pixels.set_pixel_line_gradient(start, stop, start_color, stop_color)
    for i in range(210):
        pixels.rotate_right(1)
        pixels.show()
        time.sleep(0.05)
    
    pixels.show()
    time.sleep(3)

def move_right_left(start, stop, start_color, stop_color):
    pixels.clear()
    pixels.set_pixel_line_gradient(start, stop, start_color, stop_color)
    first = start
    last = stop
    forward = True
    for i in range(20):
        if forward:
            steps = pixels.num_leds-1 - last
        else:
            steps = first
        for step in range(steps):
            if forward:
                pixels.rotate_right(1)
                last += 1
                first += 1
            else:
                pixels.rotate_left(1)
                last -= 1
                first -=1
            pixels.show()
            time.sleep(0.05)
        forward = not forward
    time.sleep(3)

def one_pixel(start, stop):
    pixels.clear()
    count = 0
    pos = start
    direction = 1
    color_value = 100
    black_color = pixels.colorHSV(0, 0, 0)
    while True:
        color = pixels.colorHSV(color_value, 255, 255) # Farbe, Sättigung, Helligkeit
        pixels.set_pixel(pos, color)
        if pos > 0:
            pixels.set_pixel(pos-direction, black_color)    
        pixels.show()
        time.sleep(0.1) # 0.1 s
        pos += direction
        if pos <= start or pos >= stop:
            direction = -direction
            if color_value >= 65535:
                color_value = 5000
            else:
                color_value += 5000;
        


all_colors(5, 25, (red, orange, yellow, green, blue, indigo, violet))
# rotate_right(10, 20, blue, red)  
# move_right_left(12, 18, blue, red)  
# one_pixel(10, 20)

# HSV - Farbe: 339 Grad, 84% Sättigung, 91% Helligkeit
# color = pixels.colorHSV(int(339/360*65535), int(84/100*255), int(91/100*255)) 
# pixels.set_pixel(20, color)
# pixels.show()

# pixels.clear()
pixels.show()





