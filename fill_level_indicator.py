import time
from lib.neopixel import Neopixel
 
# Streifen mit 30 Leds an Pin 28
pixels = Neopixel(num_leds=30, state_machine=0, pin=15, mode="GRB")
 
# Einige Farben
red = (255, 0, 0)
orange = (150, 30, 0)
yellow = (255, 100, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
indigo = (100, 0, 90)
violet = (200, 0, 100)
black = (0, 0, 0) # entspricht dem Wert "Aus"

# Farbverlauf Anzeige, definiert in einer Liste für Level 0 bis 9, entspricht 1 bis 10)
level_colors = (red, orange, orange, yellow, yellow, yellow, yellow, green, green, green)
# Definition der Anzeigenbereiche für den Level-Indikator und die restlichen Funktionen
# die Zählung beginnt bei 0, da das erste LED die "Adresse" 0 hat
level_indicator_start_pixel = 0
level_indicator_end_pixel = 9
warning_indicator_start_pixel = 12
warning_indicator_end_pixel = 19

# Initialisierung
pixels.brightness(20)
pixels.clear()
pixels.show()

# Funktion, welche die ersten 10 LEDs auf die korrekten Farbwerte setzt
def show_level(level):
    # für alle anzuzeigenden Level-LEDs (bei Level 5 wären das die LEDs an der Position 0, 1, 2, 3 und 4)
    # führe die nachfolgenden eingerückten Zeilen aus; dabei ist in der Variablen curr_level
    # der aktuelle Wert - also die LED Position für den jeweiligen Level - gespeichert
    for curr_level in range(level_indicator_start_pixel, level_indicator_start_pixel+level):
        # setze die LED an der Position curr_level auf den dazu passenden Farbwert,
        # der in der Listenvariable level_colors an diesem Listenindex steht
        # (Der Listenindex beginnt ebenfalls mit dem Wert 0, passt also!)
        pixels.set_pixel(curr_level, level_colors[curr_level])
    # für alle restlichen LEDs in dem Bereich für die Levelanzeige wird der Farbwert black gesetzt,
    # um sie auszuschalten
    for curr_dark in range (level, level_indicator_end_pixel+1):
        # setze die LED an der Position curr_dark auf den Farbwert black
        pixels.set_pixel(curr_dark, black)
        
    # aktiviere alle Veränderungen an den LED-Einstellungen
    pixels.show()
    
    if level == 1:
        low_level_notification()
        
    if level == 10:
        top_up_notification()
    
def low_level_notification():
    for i in range(0,10):
        pixels.set_pixel_line(warning_indicator_start_pixel, warning_indicator_end_pixel, red)
        pixels.show()
        time.sleep(0.3)
        pixels.set_pixel_line(warning_indicator_start_pixel, warning_indicator_end_pixel, black)
        pixels.show()
        time.sleep(0.7)

def top_up_notification():
    for i in range(0,5):
        pixels.set_pixel_line(warning_indicator_start_pixel, warning_indicator_end_pixel, green)
        pixels.show()
        time.sleep(0.2)
        pixels.set_pixel_line(warning_indicator_start_pixel, warning_indicator_end_pixel, black)
        pixels.show()
        time.sleep(0.3)

def run_tests():
    # zeige aufsteigend alle level an (1 bis 10)
#     for i in range(1,11):
#         print("test level: ", i)
#         show_level(i)  
#         time.sleep(0.5)
    # zeige absteigend alle level an (10 bis 1)
    for i in range(10,0,-1):
        print("test level: ", i)
        show_level(i)  
        time.sleep(0.5)

pixels.set_pixel_line(level_indicator_end_pixel+1, warning_indicator_start_pixel-1, violet)
pixels.show()

run_tests()

time.sleep(1)

pixels.clear()
pixels.show()