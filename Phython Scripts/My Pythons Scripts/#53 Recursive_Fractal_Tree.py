import turtle  # Importa il modulo turtle

# Definisce la funzione per disegnare un albero frattale
def DisegnaAlberoFrattale(lunghezza_ramo, t):
    if lunghezza_ramo >= 20:  # Continua a disegnare se la lunghezza del ramo è maggiore di 5
        t.forward(lunghezza_ramo)  # Muove la tartaruga avanti della lunghezza del ramo
        t.right(30)  # Gira la tartaruga a destra di 20 gradi
        DisegnaAlberoFrattale(lunghezza_ramo - 20, t)  # Richiama la funzione con una lunghezza del ramo ridotta di 15
        t.left(60)  # Gira la tartaruga a sinistra di 40 gradi
        DisegnaAlberoFrattale(lunghezza_ramo - 20, t)  # Richiama di nuovo la funzione con una lunghezza del ramo ridotta di 15
        t.right(30)  # Gira la tartaruga a destra di 20 gradi per tornare alla posizione iniziale
        t.backward(lunghezza_ramo)  # Riporta indietro la tartaruga della lunghezza del ramo



"""
Setting globali iniziali della tartaruga (eseguiti una sola voltta)
"""
# Imposta la velocità della tartaruga
turtle.speed(1)

# Posiziona la tartaruga all'inizio
turtle.left(90)  # Gira la tartaruga a sinistra di 90 gradi per puntare verso l'alto
turtle.pensize(3)
turtle.up()  # Alza la penna per evitare di disegnare mentre si muove
turtle.backward(100)  # Sposta la tartaruga indietro di 100 unità
turtle.down()  # Abbassa la penna per iniziare a disegnare
turtle.color("brown")  # Imposta il colore della tartaruga su marrone



"""
 Disegna l'albero frattale
 Nota più l'if in DisegnaAlberoFrattale sarà piccolo rispetto all' argomento iniziale più l'albero sara grande
 Il codice funziona tramite ricorsione e chiamate residue quando viene chiamata una ricorsione quella precedente non sarà terminata
 Ma sarà preservata fino alla fine delle chiamate interne successive ovvero come è visualizzabile tramite il disegno creato dallo script
"""
    
    
DisegnaAlberoFrattale(100, turtle)
turtle.exitonclick()