"""
recap :
sorted(): Ritorna una nuova lista ordinata e non modifica l'iterabile originale.
sort(): Modifica la lista originale e non ritorna nulla (ritorna None),  non ti passi in 
mente di assegnarla a una nuova variabile
"""
def criterio(Lista):
    return (len(Lista), Lista )

# Variabili di Test

Example_List_Ez = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Example_List =  ["Endgame","You","Sad","Moon","hope","Overdrive","Ion Pulse", "Overlord", "Pulsar", "Blaster", "Ion Cannon", "Earth Splitter","Strange Days", "Sun Burst", "Nova","Quasar","Alien","Atlas","Overload"]

Example_List_Of_Tuples = [(10,20,30), (40,50,60), (70,80,90), (100,110,120)]

Example_List_Complex =[('Marco', 22), ('Anna', 25), ('Elena', 25), ('Elena', 28), ('Luca', 30)]

# Sorting
Sorted_Example_List = sorted(Example_List, key=criterio)

Example_List.sort(key=lambda x: (-len(x), x),reverse=False)

Example_List_Of_Tuples.sort(key=lambda x: (x[1], x[2]),reverse=False)

persone_ordinate = sorted(Example_List_Complex, key=lambda x: (x[1], x[0]))


# Output
#print(Sorted_Example_List)
#print(Example_List)
#print(Example_List_Of_Tuples)
#print(Example_List_Ez[:1])
print(persone_ordinate)
"""
METODO 1 Spiegazione:
    
Definizione di criterio: La funzione criterio restituisce una tupla contenente 
la lunghezza della stringa e la stringa stessa.
Utilizzo di criterio in sorted(): Sorted_Example_List = sorted(Example_List, key=criterio) 
utilizza criterio per generare le chiavi di ordinamento per ogni elemento della lista.
key=criterio: La funzione criterio viene chiamata su ogni elemento della lista per generare le chiavi di ordinamento.
Tupla (len(Lista), Lista): Le tuple risultanti vengono utilizzate per ordinare la lista principalmente per lunghezza e,
in caso di parità, alfabeticamente.

METODO 2
key=: Questo parametro accetta una funzione che viene chiamata su ogni elemento 
della lista prima che l'elemento venga confrontato durante l'ordinamento.

lambda x: (len(x), x): Questa è una funzione anonima (lambda) che:
x: Rappresenta ogni elemento della lista.
len(x): Calcola la lunghezza della stringa x.
x: La stringa stessa.
La funzione lambda restituisce una tupla (len(x), x) che viene utilizzata per l'ordinamento. 
La lista viene ordinata principalmente per la lunghezza delle stringhe (len(x)), e in caso di stringhe di uguale lunghezza,
 viene ordinata alfabeticamente (x).
 
Quando utilizziamo una funzione chiave, come nel caso della funzione criterio o della lambda function, 
la funzione di ordinamento la applica a ciascun elemento per ottenere una chiave di ordinamento.
In questo caso, criterio viene chiamata su ogni elemento di Example_List. 
La tupla risultante (len(Lista), Lista) viene utilizzata per determinare l'ordine.
"""