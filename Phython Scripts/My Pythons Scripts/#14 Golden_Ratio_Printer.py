"""
nota 1:
    
Il modulo turtle in Python offre un modo semplice e intuitivo per creare grafici e disegni 
attraverso il movimento di una "tartaruga" sullo schermo. 
È ampiamente utilizzato per insegnare concetti di programmazione e grafica in modo visuale e interattivo.
"""

"""
nota 2:
    
Questo programma usa un metodo ricorsivo ovvero la funzione richaima se stessa fino a quando l'if blocca la chiamata ricorsiva
indesiderata e consente al programma di fermarsi anzichè replicarsi in eterno
"""

import turtle  # Importa il modulo turtle
import random  # Importa il modulo random per generare colori casuali

# Funzione per generare un colore casuale
def Rand_Color():
    return random.random(), random.random(), random.random()  # Restituisce un colore casuale come tuple RGB

# Funzione per disegnare una spirale aurea
def Disegna_Spirale_Aurea(lunghezza_arco, angolo):
    turtle.circle(lunghezza_arco, angolo)  # Disegna un arco con la lunghezza e l'angolo specificati
    turtle.color(Rand_Color())  # Imposta il colore della tartaruga in modo casuale
    if lunghezza_arco > 2:  # Continua a disegnare se la lunghezza del ramo è maggiore di 2
        Disegna_Spirale_Aurea(lunghezza_arco // 2, angolo)  # Richiama la funzione con una lunghezza del ramo ridotta della metà

# Impostazioni iniziali
turtle.speed(2)  # Imposta la velocità della tartaruga
turtle.pensize(3)  # Imposta la larghezza del tratto della tartaruga
turtle.left(90)  # Gira la tartaruga di 90 gradi a sinistra
turtle.up()  # Alza la penna per evitare di disegnare mentre si muove
turtle.goto(300, 0)  # Sposta la tartaruga alla posizione iniziale
turtle.down()  # Abbassa la penna per iniziare a disegnare
Disegna_Spirale_Aurea(300, 90)  # Disegna una spirale aurea con raggio 300 e un angolo di 90 gradi

turtle.exitonclick()  # Mantiene la finestra aperta fino a quando l'utente non fa clic sulla finestra
