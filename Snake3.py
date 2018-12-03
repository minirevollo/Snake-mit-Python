### Snake 3 by Mini Revollo 
### Ein Spiel aus dem erfindergarden

from tkinter import *
from time import sleep
from random import randint
from copy import deepcopy

class spielfeld:
    ###Stellt überwiegend das Spielfeld dar.###
        
    # Variablen
    feld = 0        #Frame für das Spiel
    scoreleiste = 0    #Label für die Scoreleiste
    infoleiste = 0     #Label für die Infoleiste
    spielen = 1        #zeigt an ob das Spiel aktiv ist
    raster_x = 12       #Unterteilung des Spielfeldes 
    raster_y = 12       #Unterteilung des Spielfeldes
    breite = raster_x * 50   #Berechnung der Breite des Spielfeldes
    hoehe = raster_y * 40    #Berechnung der Hoehe des Spielfeldes
    groesse = str(breite) + "x" + str(hoehe)   #Groesse des GUI
    score_hoehe = raster_y * 3  #Anzeigenhoehe für den score
    info_hoehe = raster_y * 2   #Anzeigenhoehe für die  info
    info_text = "use the left and the right arrow"  
    fg = "green"  #Schriftfarbe
    bg = "black"   #Hintergrundfarbe
    font = "Consolas"  #Schriftart
    score = 0           #Punkte
    start_speed = 200    #Anfangsgeschwindigkeit in ms zwischen den loops
    speed = start_speed   #Geschwindigkeit wärend des Spiels in ms
    start_richtung = 2    #Richtung bei Spielbeginn
    richtung = start_richtung  #Richtung die wärend des Spiels angepasst wird
    richtung_x = [1, 0, -1, 0]   #Richtungsmultiplikator
    richtung_y = [0, 1, 0, -1]   #Richtungsmultiplikator
    
    # Funktionen
    
    def feld_anzeigen():
        ###Erzeugt das Spielfeld und zeigt es an.###
        
        spielfeld.feld = Frame(root, bg = "black")
        spielfeld.feld.place(x = 0, y = 0, width = spielfeld.breite, height = spielfeld.hoehe)
        
    def scoreleiste_anzeigen():
        ###Erzeugt die scoreleiste und zeigt sie an.###
        
        spielfeld.scoreleiste = Label(spielfeld.feld, 
            text = "by mini revollo                                                            "               
                    + "score: " + str(spielfeld.score) 
                    + "                                            erfindergarden munich"
                    + "\n highscore: " + str(highscore.score[4]),
            bg = "black",
            fg = "green")
        spielfeld.scoreleiste.place(x = 0, y = 0, width = spielfeld.breite, height = spielfeld.score_hoehe)  
        
    def infoleiste_anzeigen():
        ###Erzeugt die infoleiste und zeigt sie an.###
        
        spielfeld.infoleiste = Label(spielfeld.feld,
                text = spielfeld.info_text,
                bg = "black",
                fg = "green")
        spielfeld.infoleiste.place(x = 0, y = spielfeld.hoehe - spielfeld.info_hoehe, width = spielfeld.breite, height = spielfeld.score_hoehe)

    # logo_zeigen
    
    # logo_ausblenden

    def score_erhoehen():
        ###Erhoeht den Spielstand.###
        
        spielfeld.score += 1
        spielfeld.scoreleiste_anzeigen()
        
    def speed_erhoehen():
        ###Erhoeht die Geschwindigkeit.###
        
        a = int(spielfeld.speed * 0.15)
        spielfeld.speed -= a
    
    def game_over():
        ###Aktionen die bei Spielende stattfinden.###
        
        spielfeld.spielen = 0
        spielfeld.info_text = "press - s - for a new game"
        spielfeld.infoleiste_anzeigen()
        highscore.berechnen()
        #highscore.erstellen()
        print("game over")
    
    def game_starten():
        ###Aktionen die bei Neustart ausgefuehrt werden.###
        
        schlange.pos_x = deepcopy(schlange.start_pos_x)
        schlange.pos_y = deepcopy(schlange.start_pos_y)
        schlange.laenge = len(schlange.pos_x)
        spielfeld.spielen = 1
        spielfeld.score = 0
        spielfeld.speed = spielfeld.start_speed
        spielfeld.richtung = spielfeld.start_richtung
        spielfeld.info_text = "use the left and the right arrow"
        spielfeld.infoleiste_anzeigen()
        spielfeld.scoreleiste_anzeigen()
        highscore.ausblenden()
        highscore.pos = 0
        highscore.buchstaben = [65, 65, 65]
        highscore.einreihen = 0
        apfel.positionieren()
        
    
class schlange:
    ###Stellt die Schlange dar.###

    # Variablen
    laenge = 3   #Laenge der Schlange bei Spielgebin
    laenge_max = 40  #Max Anzahl der Schlangenelemente
    elemente = []   #Speichert die Schlangenelemente
    start_pos_x = [spielfeld.raster_x * 10, spielfeld.raster_x * 11, spielfeld.raster_x * 12] #Berechnung der Startposition x
    start_pos_y = [spielfeld.raster_y * 10,spielfeld.raster_y * 10, spielfeld.raster_y * 10] #Berechnung der Startposition y
    pos_x = deepcopy(start_pos_x) #Positionsliste der Elemente die wärend des Spiels angepasst wird
    pos_y = deepcopy(start_pos_y) #Positionsliste der Elemente die wärend des Spiels angepasst wird
    schriftfarbe = "green"
    hintergrund = "black"
    schriftart = "Consolas"
    text_kopf = "O"  #Anzeige für den Kopf der Schlange
    text_koerper = "o" #Anzeige für die Körperelemente der Schlange
    
    # Funktionen
    
    def erstellen():
        ###Erstellt alle Elemente der Schlange ohne diese anzuzeigen.###
        
        for item in range(schlange.laenge_max):      #liste mit den Namen max Anzahl an schlangenteilen 
            schlange.elemente.append("s" + str(item))   #erstellt s0, s1 ...
        for item in range(schlange.laenge_max):    #schlangenkörper objekte erstellen
            schlange.elemente[item] = Label(text = schlange.text_koerper,
                        font = schlange.schriftart,
                        fg = schlange.schriftfarbe, 
                        bg = schlange.hintergrund)
    
    def kopf_berechnen():
        ###Berechnet die neue Position des Schlangenkopfes aus der Richtung.###
        
        x = schlange.pos_x[0] + spielfeld.richtung_x[spielfeld.richtung] * spielfeld.raster_x
        y = schlange.pos_y[0] + spielfeld.richtung_y[spielfeld.richtung] * spielfeld.raster_y
        schlange.pos_x.insert(0, x) #Fügt den Kopf in die Positionsliste der Elemente ein
        schlange.pos_y.insert(0, y) #Fügt den Kopf in die Positionsliste der Elemente ein
       
        
    def kontakt_apfel():
        ###Ueberpruefung auf Kontakt mit dem Apfel.###
        
        if schlange.pos_x[0] == apfel.pos_x and schlange.pos_y[0] == apfel.pos_y:
            apfel.positionieren()
            spielfeld.score_erhoehen()
            spielfeld.speed_erhoehen()
            schlange.laenge_erhoehen()
            print(str(schlange.laenge))
        else:
            schlange.pos_x.pop() #Löscht das letzte Element aus der Positionsliste, da die Schlange nicht wachsen soll
            schlange.pos_y.pop() #Löscht das letzte Element aus der Positionsliste, da die Schlange nicht wachsen soll
            
    def kontakt_rand():
        ###Ueberprueft auf Kontakt mit dem Spielfeldrand.###
        
        if schlange.pos_x[0] < 0 or schlange.pos_x[0] >=spielfeld.breite:
            spielfeld.game_over()
        if schlange.pos_y[0] < spielfeld.score_hoehe or schlange.pos_y[0] > spielfeld.hoehe - spielfeld.info_hoehe:
            spielfeld.game_over()
            
    def kontakt_koerper():
        ###Ueberprueft auf Kontakt mit dem Schlangenkoerper.###
        
        for item in range(1, schlange.laenge):
            if schlange.pos_x[0] == schlange.pos_x[item] and schlange.pos_y[0] == schlange.pos_y[item]:
                spielfeld.game_over()

    def laenge_erhoehen():
        ###Vergroessert die Laenge der Schlange.###
        
        schlange.laenge += 1
        
    def anzeigen():
        ###Zeigt die Schlange auf dem Spielfeld an.###
        
        for item in range(schlange.laenge):
            schlange.elemente[item].place(x = schlange.pos_x[item], y = schlange.pos_y[item],width = spielfeld.raster_x, height = spielfeld.raster_y)

    def ausblenden():
        ###Blendet die Schlange aus.###
       for item in range(schlange.laenge):
            schlange.elemente[item].place_forget()
    
class apfel:
    ###Stellt den Apfel dar.###
    
     # Variablen
     
    a = 0  #Label fuer den Apfel
    pos_x = 0
    pos_y = 0
    font = "Consolas"
    text = "O" #Symbol für den Apfel
    fg = "red"
    bg = "black"
    
    # Funktionen
    
    def erstellen():
        ###Erstellt das Apfellabel.###
        
        apfel.a = Label(text = apfel.text, fg = apfel.fg, bg = apfel.bg)
        
    def positionieren():
        ###Berechnet eine neue Position fuer den Apfel und ueberprueft auf Kontakt mit der Schlange.###
        
        apfel.pos_x = randint(0, spielfeld.breite / spielfeld.raster_x - 1) * spielfeld.raster_x
        apfel.pos_y = randint(spielfeld.score_hoehe / spielfeld.raster_y + 1, (spielfeld.hoehe - spielfeld.info_hoehe) / spielfeld.raster_y - 1) * spielfeld.raster_y
        for item in range(schlange.laenge):
            if schlange.pos_x[item] == apfel.pos_x and schlange.pos_y[item] == apfel.pos_y:
                apfel.positionieren()
        print("apfelposition: " + str(apfel.pos_x) + " : " + str(apfel.pos_y))
        
    def anzeigen():
        ###Zeigt den Apfel im Spielfeld an.###
        
        apfel.a.place(x = apfel.pos_x, y = apfel.pos_y, width = spielfeld.raster_x, height = spielfeld.raster_y)
        
    def ausblenden():
        ###Blendet den Apfel wieder aus.###
        
        apfel.a.place_forget()
  
class highscore:
    
    # variablen
    
    hs = 0 #Label für den highscore
    pos = 0 #Speichert den erreichten Rang
    breite = 200
    hoehe = 200
    score = [0, 0, 0, 0, 0] #Liste der highscore
    buchstaben = [65, 65, 65] #Zeichen die zuerst erscheinen wenn man sich eintragen darf
    buchstaben_pos = 0 #Position des Zeigers fuer den gerade zu verändernden Buchstaben
    name = ["___", "___", "___", "___", "___"] #Namensliste für die highscore
    text = "highscore: " + str(score[0])
    einreihen = 0 #Flag ob ein Eintrag erfolgen soll
    fg = "green"
    bg = "black"
    font = "Consolas"
    
    # funktionen
    
    def berechnen():
        ###Kontrolliert ob ein Eintrag in die Liste erfolgen soll und an welcher Position.###
        
        if spielfeld.score > highscore.score[0]:
            highscore.einreihen = 1
            for item in range(5):
                if spielfeld.score > highscore.score[item]:
                    highscore.pos = item
            highscore.score.insert(highscore.pos + 1, spielfeld.score)
            highscore.score.pop(0)
            highscore.name.insert(highscore.pos + 1, "AAA")
            highscore.name.pop(0)
            print("pos: " + str(highscore.pos))

    def erstellen():
        ###Erstellt den Text für das highscorelabel.###
        
        highscore.text = "highscore: "\
                        + "\n pos 1.     " + highscore.name[4] + "   " + str(highscore.score[4])\
                        + "\n pos 2.     " + highscore.name[3] + "   " + str(highscore.score[3])\
                        + "\n pos 3.     " + highscore.name[2] + "   " + str(highscore.score[2])\
                        + "\n pos 4.     " + highscore.name[1] + "   " + str(highscore.score[1])\
                        + "\n pos 5.     " + highscore.name[0] + "   " + str(highscore.score[0])
        highscore.hs = Label(text = highscore.text, fg = highscore.fg, bg = highscore.bg)
        
    def text_anpassen():
        ###Passt den Text für das highscorelabel mit der Namenseingabe an.###
        
        if highscore.einreihen == 1:
            highscore.name[highscore.pos] = chr(highscore.buchstaben[0]) + chr(highscore.buchstaben[1]) + chr(highscore.buchstaben[2])
            highscore.hs.config(text = "highscore: "\
                            + "\n pos 1.     " + highscore.name[4] + "   " + str(highscore.score[4])\
                            + "\n pos 2.     " + highscore.name[3] + "   " + str(highscore.score[3])\
                            + "\n pos 3.     " + highscore.name[2] + "   " + str(highscore.score[2])\
                            + "\n pos 4.     " + highscore.name[1] + "   " + str(highscore.score[1])\
                            + "\n pos 5.     " + highscore.name[0] + "   " + str(highscore.score[0]))

    def anzeigen():
        ###Zeigt den highscore an.###
        
        highscore.hs.place(x = (spielfeld.breite - highscore.breite) / 2, y = spielfeld.hoehe / 3, width = highscore.breite, height = 200)
        
    def ausblenden():
        ###Blendet das highscore label aus.###
        
        highscore.hs.place_forget()

def tasten_auswertung(key):
    ###Wertet die Tasteneingabe je nach Spielmodus aus.###
    
    if spielfeld.spielen == 1:
        if  key.keysym == "Right":           
            spielfeld.richtung += 1
            if spielfeld.richtung > 3:
               spielfeld.richtung = 0
        if key.keysym == "Left":
            spielfeld.richtung -= 1
            if spielfeld.richtung < 0:
                spielfeld.richtung = 3
    else:
        if key.char == "s":
            spielfeld.game_starten()
        if key.keysym == "Right":
            highscore.buchstaben_pos += 1
            if highscore.buchstaben_pos > 2:
                highscore.buchstaben_pos = 0
            print(str(highscore.buchstaben_pos))
        if key.keysym == "Left":
            highscore.buchstaben_pos -= 1
            if highscore.buchstaben_pos < 0:
                highscore.buchstaben_pos = 2
            print(str(highscore.buchstaben_pos))
        if key.keysym == "Up":
            highscore.buchstaben[highscore.buchstaben_pos] += 1
            if highscore.buchstaben[highscore.buchstaben_pos] > 120:
                highscore.buchstaben[highscore.buchstaben_pos] = 65
            print(str(highscore.buchstaben[highscore.buchstaben_pos]))
        if key.keysym == "Down":
            highscore.buchstaben[highscore.buchstaben_pos] -= 1
            if highscore.buchstaben[highscore.buchstaben_pos] < 65:
                highscore.buchstaben[highscore.buchstaben_pos] = 120
            print(str(highscore.buchstaben[highscore.buchstaben_pos]))
            
### Setup ###

root = Tk()                              #ein Fenster erstellen
root.geometry(spielfeld.groesse)          #Größe zuordnen
root.title("Snake 3 - by mini revollo")   #Fenster mit einem Titel versehen 
root.bind_all("<KeyPress>", tasten_auswertung)     #Tastendruck abfangen 
spielfeld.feld_anzeigen()
spielfeld.scoreleiste_anzeigen()
spielfeld.infoleiste_anzeigen()
highscore.erstellen()
schlange.erstellen()
apfel.positionieren()
apfel.erstellen()

#spielfeld.logo_zeigen()

### Loop ###

def spiel():
    if spielfeld.spielen == 1:
        apfel.anzeigen()
        schlange.kopf_berechnen()
        schlange.anzeigen()
        schlange.kontakt_apfel()
        schlange.kontakt_rand()
        schlange.kontakt_koerper()
    else:
        schlange.ausblenden()
        apfel.ausblenden()
        highscore.text_anpassen()
        highscore.anzeigen()
    root.after(spielfeld.speed, spiel)
    

root.after(0, spiel)
root.mainloop()