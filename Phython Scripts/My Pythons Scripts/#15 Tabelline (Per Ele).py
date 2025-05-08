# L'esercizio richiede di creare una funzione esercizio che accetta una var(variabile) numero
# Per chiamare una funzione usiamo il comando def e la var (num) dichiarata insieme alla funzione
# Le righe che iniziano per "#" non vengono contante come codice e si chiamano commenti servono a descrivere 
# Ciò che fà il codice
def esercizio(num):
    #definiamo una var counter servirà a inicare al programma il numero con il quale dovrà moltiplicare
    #la var (num) la variabile è impostata a 1 siccome l'esercizio richiede che num sia moltiplicato da 1 a 10 compresi
    counter=1
    #Questo print scrive la riga di testo richiesta dall'output
    print("Tabellina del 7 :")
    # Questo if e quello successivo verificano se num è = a 0 o no se è uguale a 0 srive "fine"
    # se è !=(diverso) da 0 svolge l'esercizio
    if num == 0:
        print("Fine")
    if num != 0:
        #Finchè counter è minore o = a 10 il while eseguira il codic al suo interno in loop
        while counter <= 10:
            #Creiamo una var di risultato che si aggiorna a ogni ciclo ed è ottenuta da num moltiplicato per counter
            Current_Result = num*counter
            #Questa riga scrive l' output dell' esercizio scrivendo le varie varibili num, counter e result
            #sotto formto di stringa di testo str() perchè scrivendole sotto formato di interi int() dava un errore 
            #in quanto non puoi concatenare stringhe e interi
            print(str(num)+ " x " + str(counter) + " = " + str(Current_Result))
            #Dopo aver scritto la riga di output aumentiamo counter di 1  per aumentare far sì che al ciclo successivo
            #Num sia moltiplicato per il numero successivo della tabellina sempre indicato da counter
            counter += 1

#Definiamo la var num e chiamiamo la funzione se noi non chiamiamo la funzione non sarà svolto il codice al suo interno
#Num verrà fornita alla funzione come argomento se esercizio non la riceve dà errore
num = 9
esercizio(num)
"""
                                                         =)
"""