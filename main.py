import time
from lib.neopixel import Neopixel
from machine import Pin

DEBUG = True

# wir haben 4 pins belegt (GP2 bis GP5), die jeweils einen bestimmten Füllstand anzeigen
# wir gehen davon aus, dass der niedrigste Füllstand über den niedrigsten pin angezeigt wird
# und der höchste Füllstand über den höchsten pin
level_1 = machine.Pin(2, Pin.IN, Pin.PULL_DOWN)
level_2 = machine.Pin(3, Pin.IN, Pin.PULL_DOWN)
level_3 = machine.Pin(4, Pin.IN, Pin.PULL_DOWN)
level_4 = machine.Pin(5, Pin.IN, Pin.PULL_DOWN)

# wir definieren eine Statusvariable, damit wir uns den letzten/aktuellen Level merken können
# so müssen wir nicht jedesmal wieder die Anzeige aktualisieren, wenn sich gar nichts geändert hat
# seit der letzten Messung
# dies sorgt dann auch dafür, dass wir bei Niedrigstand oder Höchststand nicht unendlich die
# Notifikation wiederholen :-)
last_level = 0 # 0 ist eigentlich kein gültiger Wert (Level geht von 1 bis 10), aber zum initialsieren ist das ok
new_level = 0

# Definition einiger Farben (diese Werte sind konstant und werden nicht geändert im Programmverlauf)
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
notification_start_pixel = 12
notification_end_pixel = 19

# Initialisierung der Lichterkette als Streifen mit 30 Leds an Pin 15
pixels = Neopixel(num_leds=30, state_machine=0, pin=15, mode="GRB")
# wir stellen die Helligkeit auf einen relativ niedrigen Wert, dies reduziert den Stromverbrauch für
# den Raspberry Pi Pico :-)
pixels.brightness(20)
# sicherstellen, dass die Lichterkette komplett aus ist, d.h. alle LEDs dunkel/schwarz
pixels.clear()
# aktiviere diese Initialeinstellungen der LEDs auf der Lichterkette
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
    
    # wenn wir Level 1 anzeigen (= niedrigster Stand), dann bitte die Funktion low_level_notification ausführen
    if level == 1:
        low_level_notification()
        
    # wenn wir Level 10 anzeigen (= höchster Stand), dann bitte die Funktion top_up_notification ausführen
    if level == 10:
        top_up_notification()

# diese Funktion wird alle LEDs im Notifikationsbereich 10x rot (langsam) blinken lassen
def low_level_notification():
    if DEBUG: print("   Zeige 'low level notification'.") # DEBUG
    for i in range(0,10):
        pixels.set_pixel_line(notification_start_pixel, notification_end_pixel, red)
        pixels.show()
        time.sleep(0.3)
        pixels.set_pixel_line(notification_start_pixel, notification_end_pixel, black)
        pixels.show()
        time.sleep(0.7)

# diese Funktion wird alle LEDs im Notifikationsbereich 5x grün (schnell) blinken lassen
def top_up_notification():
    if DEBUG: print("   Zeige 'top up notification'.") # DEBUG
    for i in range(0,5):
        pixels.set_pixel_line(notification_start_pixel, notification_end_pixel, green)
        pixels.show()
        time.sleep(0.2)
        pixels.set_pixel_line(notification_start_pixel, notification_end_pixel, black)
        pixels.show()
        time.sleep(0.3)
        
# wir füllen den die LEDs zwischen der Füllstandsanzeige und dem Notifikationsbereich mit violetten LEDs
pixels.set_pixel_line(level_indicator_end_pixel+1, notification_start_pixel-1, violet)
pixels.show()

# dies ist der Hauptteil des Programms, der alle 1 sec den aktuellen Füllstand überprüft und
# die Anzeige entsprechend umstellt, wenn nötig
while True:
    # wenn der pin für den Level 4 (voll) aktiv ist, dann ...
    if level_4.value() == 1:
        # ... stelle die Anzeige auf Level 10
        new_level = 10
    # wenn das if-Statement oberhalb nicht zutrifft,
    # und gleichzeitig der pin für den Level 3 aktiv ist, dann ...
    elif level_3.value() == 1:
        # ... stelle die Anzeige auf Level 8
        new_level = 8
    # wenn das if-Statement oberhalb nicht zutrifft,
    # und gleichzeitig der pin für den Level 2 aktiv ist, dann ...
    elif level_2.value() == 1:
        # ... stelle die Anzeige auf Level 5
        new_level = 5
    # wenn das if-Statement oberhalb nicht zutrifft,
    # und gleichzeitig der pin für den Level 1 aktiv ist, dann ...
    elif level_1.value() == 1:
        # ... stelle die Anzeige auf Level 5
        new_level = 3
    # wenn das if-Statement oberhalb nicht zutrifft,
    # dann ...
    else:
        # ... stelle die Anzeige auf Level 5
        new_level = 1

    # Hat sich der Füllstand gerade geändert (verglichen mit dem Wert, den wir uns bei der
    # letzten Runde gemerkt haben)?
    if last_level != new_level:
        if DEBUG: print("ändere Level von ", last_level, " auf ", new_level) # DEBUG
        # ja, wir haben einen neuen Wert, also stellen wir die Anzeige auf den neuen Level
        show_level(new_level)
        # und setzen den last_level auf den aktuellen Stand für die nächste Runde
        last_level = new_level

time.sleep(1)
