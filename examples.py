import time
from lib.neopixel import Neopixel
 
# Streifen mit 30 Leds an Pin 28
pixels = Neopixel(num_leds=30, state_machine=0, pin=15, mode="GRB")
 
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

# Lauflicht in dem alle LEDs zwischen start und stop aktiv sind
# aber die Farbe nacheinander die Liste der unter dem Parameter colors
# übergebenen Farben anzeigt
def all_colors(start, stop, colors):
    # mache alle LEDs dunkel
    pixels.clear()
    # setze i auf 0; i wird unser Durchlaufzähler
    ####i = 0
    # führe den Farbwechsel genau 100 Mal durch
    for i in range(100):
    # Beginn der unendlichen Schleife
    ####while True:
        # Berechnung des Farbindex (= Position in der übergebenen Farbliste)
        # mit Hilfe einer Modulo-Rechnung:
        # nimm i und Teile es (ganzzahlig) durch die Länger der Liste colors (in unserem Fall 7)
        # und nehme den Rest, der verbleibt
        col_index = i % len(colors)
        # führe die folgende Berechnung für alle LEDs durch, die in unserem Anzeigeraum liegen
        for pixel in range(start, stop+1):
            ##if col_index == 4: # blue
            ##    pixels.set_pixel(pixel, colors[col_index], 150)
            ##else:
            # setze die LED an der aktuellen Stelle (definiert durch den Wert in pixel) auf den
            # Farbwert, der in der Farbliste colors an der Stelle col_index steht
            pixels.set_pixel(pixel, colors[col_index])
            # jetzt werden die Veränderungen an den LEDs durchgeführt
            pixels.show()
            # warte für ein 5-tausendstel einer Sekunde
            time.sleep(0.005)
            # erhöhe den Farbindex um 1, so dass die nächste Farbe gesetzt wird
            col_index += 1
            # wenn der Farbindex auf der höchsten möglichen Zahl angekommen ist, dann
            # setze ihn wieder auf 0
            if col_index == len(colors):
                col_index = 0

#
def rotate_right(start, stop, start_color, stop_color):
    # mache alle LEDs dunkel
    pixels.clear()
    
    pixels.set_pixel_line_gradient(start, stop, start_color, stop_color)
    for i in range(210):
        pixels.rotate_right(1)
        pixels.show()
        time.sleep(0.05)
    
    pixels.show()
    time.sleep(3)

# Lauflicht, bei dem eine Reihe von aktiven LEDs, die einen Farbverlauf anzeigen
# erst immer weiter in Richtung Ende der LED-Kette verschoben werden, und wenn sie
# das Ende der LED-Kette erreicht haben wieder zurück in Richtung des Anfangs der
# LED-Kette verschoben werden.
def move_right_left(start, stop, start_color, stop_color):
    # mache alle LEDs dunkel
    pixels.clear()
    # erstelle einen LED-Farbverlauf zwischen der LED an der Position start
    # und der LED an der Position end mit den Farbverlaufanfangswert start_color und
    # dem Endwert für den Farbverlaug stop_color
    pixels.set_pixel_line_gradient(start, stop, start_color, stop_color)
    # setze die Werte first gleich start und last gleich stop
    first = start
    last = stop
    # wir definieren, dass zu Beginn die LEDs vorwärts gewechselt werden im Lauflicht
    forward = True
    # führe die folgende Schleife aus,
    # solange der Wert für i zwischen 0 und kleiner als 20 ist
    # i wird dabei automatisch am Ende von jedem Durchlauf um 1 erhöht
    for i in range(0, 20):
        # wenn forward == True, wir also in einem Vorwärtslauf sind ...
        if forward:
            # wir berechnen, wieviele Lauflichtschritte vom letzten aktiven LED
            # bis zum Ende der LED-Kette vorhanden sind
            # HINWEIS: Die Bibliothek neopixel liefert uns mit pixels.num_leds
            # die Anzahl der LEDs in unserem LED-Streifen zurück.
            steps = pixels.num_leds-1 - last
        # ... andernfalls sind wir im Rückwärtslauf
        else:
            # die Anzahl Laufrichtschritte vom ersten aktiven LED bis zum Anfang
            # der LED-Kette entspricht der Position des ersten LED
            # HINWEIS: Die LEDs der Lichterkette (also die Positionen) werden vom
            # Wert 0 aufwärts gezählt. Die erste LED hat also die Position 0!
            steps = first
        # führe die folgende Schleife so oft aus, wie Schritte im Wert steps stehen
        # step wird dabei automatisch am Ende von jedem Durchlauf um 1 erhöht
        for step in range(0, steps):
            # wenn forward == True, wir also in einem Vorwärtslauf sind ...
            if forward:
                # schiebe alle LEDs um einen Schritt weiter nach rechts
                pixels.rotate_right(1)
                # setze die gemerkte Position der letzten aktiven LED um eins höher
                last += 1
                # setze die gemerkte Position der ersten aktiven LED um eins niedriger
                first += 1
            # ... andernfalls sind wir im Rückwärtslauf
            else:
                # schiebe alle LEDs um einen Schritt weiter nach links
                pixels.rotate_left(1)
                # setze die gemerkte Position der letzten aktiven LED um eins niedriger
                last -= 1
                # setze die gemerkte Position der ersten aktiven LED um eins höher
                first -=1
            # jetzt werden die Veränderungen an den LEDs durchgeführt
            pixels.show()
            # wir warten 5 100-tel Sekunden
            time.sleep(0.05)
        # kehre den Wert von forward um;
        # d.h. wenn er auf True stand ist er jetzt False
        # wenn er auf False stand ist er jetzt True
        forward = not forward
    # wir warten 3 Sekunden; TODO: warum???
    time.sleep(3)
    
# Lauflicht, bei dem eine Reihe von aktiven LEDs, die einen Farbverlauf anzeigen
# erst immer weiter in Richtung Ende der LED-Kette verschoben werden, und wenn sie
# das Ende der LED-Kette erreicht haben wieder zurück in Richtung des Anfangs der
# LED-Kette verschoben werden.
def gradient_bounce(length_chain, length_gradient, start_color, stop_color):
    # mache alle LEDs dunkel
    pixels.clear()
    # setze/berechne erste und letzte Position des Gradienten zum Start des Programms
    first = 0
    last = length_gradient

    print('length: ', pixels.num_leds)

    # prüfe, ob length_chain kleiner ist als length_gradient und setze den Wert
    # in diesem Fall auf length_gradient x 2
    if length_chain <= length_gradient:
        length_chain = 2 * length_gradient
    # prüfe, ob length_chain grösser der Gesamtlänge der LED-Kette ist
    # und setze den Wert in diesem Fall gleich der Gesamtlänge der LED-Kette
    if length_chain > pixels.num_leds:
        length_chain = pixels.num_leds
    # erstelle einen LED-Farbverlauf zwischen der LED an der Position start
    # und der LED an der Position end mit den Farbverlaufanfangswert start_color und
    # dem Endwert für den Farbverlaug stop_color
    pixels.set_pixel_line_gradient(first, last, start_color, stop_color)
    # wir definieren, dass zu Beginn die LEDs vorwärts gewechselt werden im Lauflicht
    forward = True
    # führe die folgende Schleife aus,
    # solange der Wert für i zwischen 0 und kleiner als 20 ist
    # i wird dabei automatisch am Ende von jedem Durchlauf um 1 erhöht
    for i in range(0, 20):
        # wenn forward == True, wir also in einem Vorwärtslauf sind ...
        if forward:
            # wir berechnen, wieviele Lauflichtschritte vom letzten aktiven LED
            # bis zum Ende der LED-Kette vorhanden sind
            # HINWEIS: Die Bibliothek neopixel liefert uns mit pixels.num_leds
            # die Anzahl der LEDs in unserem LED-Streifen zurück.
            steps = length_chain-1 - last
        # ... andernfalls sind wir im Rückwärtslauf
        else:
            # die Anzahl Laufrichtschritte vom ersten aktiven LED bis zum Anfang
            # der LED-Kette entspricht der Position des ersten LED
            # HINWEIS: Die LEDs der Lichterkette (also die Positionen) werden vom
            # Wert 0 aufwärts gezählt. Die erste LED hat also die Position 0!
            steps = first
        # führe die folgende Schleife so oft aus, wie Schritte im Wert steps stehen
        # step wird dabei automatisch am Ende von jedem Durchlauf um 1 erhöht
        for step in range(0, steps):
            # wenn forward == True, wir also in einem Vorwärtslauf sind ...
            if forward:
                # schiebe alle LEDs um einen Schritt weiter nach rechts
                pixels.rotate_right(1)
                # setze die gemerkte Position der letzten aktiven LED um eins höher
                last += 1
                # setze die gemerkte Position der ersten aktiven LED um eins niedriger
                first += 1
            # ... andernfalls sind wir im Rückwärtslauf
            else:
                # schiebe alle LEDs um einen Schritt weiter nach links
                pixels.rotate_left(1)
                # setze die gemerkte Position der letzten aktiven LED um eins niedriger
                last -= 1
                # setze die gemerkte Position der ersten aktiven LED um eins höher
                first -=1
            # jetzt werden die Veränderungen an den LEDs durchgeführt
            pixels.show()
            # wir warten 5 100-tel Sekunden
            time.sleep(0.05)
        # kehre den Wert von forward um;
        # d.h. wenn er auf True stand ist er jetzt False
        # wenn er auf False stand ist er jetzt True
        forward = not forward
    # wir warten 3 Sekunden; TODO: warum???
    ##time.sleep(3)


# Lauflicht mit einzelnem Pixel und Farbänderung durch den gesamten Farbraum
# als Parameter werden die erste und die letzte LED-Position übergeben zwischen
# denen das Lauflicht laufen soll
def one_pixel(start, stop):
    # mache alle LEDs dunkel
    pixels.clear()
    # Zähler wird auf 0 gesetzt (initialisieren)
    count = 0
    # aktuelle Positions wird auf den Wert start gesetzt (wurde als Parameter übergeben)
    pos = start
    # Laufrichtung wird gesetzt; 1 ist vorwärts, -1 ist rückwärts
    direction = 1
    # ein Anfangswert für die Farbe wird gesetzt;
    # wir arbeiten mit HSV-Werten, also Farbwert, Sättigung, Helligkeit
    # die möglichen Farbwerte gehen bis 65535, dem maximum darstellbaren Wert
    color_value = 5000
    # der "Farbwert" für eine dunkle/schwarze LED wird definiert
    black_color = pixels.colorHSV(0, 0, 0)
    # Beginn der unendlichen Schleife
    while True:
        # aktueller Farbwert wird definiert (mit dem aktuellen "color_value",
        # welcher beim ersten Durchlauf auf 100 steht (siehe oben)
        color = pixels.colorHSV(color_value, 255, 255) # Farbe, Sättigung, Helligkeit
        # die LED an der Stelle pos wird auf den gerade definierten Farbwert gesetzt
        pixels.set_pixel(pos, color)
        # solange wir nicht an der Stelle 0 sind, also ab dem zweiten Durchlauf...
        if pos > 0:
            # die LED, die als vorherige aktiviert worden ist, wird auf dunkel gesetzt
            pixels.set_pixel(pos-direction, black_color)
        # jetzt werden die Veränderungen an den LEDs durchgeführt
        pixels.show()
        # wir warten eine 10-tel Sekunde
        time.sleep(0.1) # 0.1 s
        # die Position pos wird um den Wert von direction erhöht
        # dieser ist entweder +1 (bei Vorwärtslauf) oder -1 (bei Rückwärtslauf)
        pos += direction
        # wenn wir bei oder unter der Startposition angekommen sind,
        # oder wenn wir über oder bei der Endposition angekommen sind...
        if pos <= start or pos >= stop:
            # ändere die Richtung von +1 auf -1 bzw. von -1 auf +1
            direction = -direction
            # wenn der Farbwert über dem höchsten möglichen Wert 65535 liegt ...
            if color_value >= 65535:
                # setze den Farbwert auf 5000 zurück
                color_value = 5000
            # ansonsten ...
            else:
                # erhöhe den Farbwert um 5000
                color_value += 5000;
        
def audi_blinker():
    pixels.clear()
    for pos in range(0,15,1):
        pixels.set_pixel(pos, yellow)
        pixels.set_pixel(29-pos, yellow)
        pixels.show()
        time.sleep(1)

       
        

# all_colors(5, 25, (red, orange, yellow, green, blue, indigo, violet))
# rotate_right(10, 20, blue, red)  
# move_right_left(12, 18, blue, red)
# gradient_bounce(30, 7, red, blue)
# one_pixel(10, 20)
while True:
    audi_blinker()
    pixels.clear()
    pixels.show()

# HSV - Farbe: 339 Grad, 84% Sättigung, 91% Helligkeit
# color = pixels.colorHSV(int(339/360*65535), int(84/100*255), int(91/100*255)) 
# pixels.set_pixel(20, color)
# pixels.show()

# pixels.clear()
pixels.show()





