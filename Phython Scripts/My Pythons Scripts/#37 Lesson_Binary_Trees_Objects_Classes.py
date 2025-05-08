# let's declre a class
class Nodo_Binario:
    # This Function is a builder per oggetti costruiti tramite la classe nodo binario
    # Questo Costruttore appartiene alla classe Nodo Binario Crea oggetti con Attributi:
    # - Quindi ogni nodo dichiarato avrà dei valori se saranno aggiunti alla dichiarazione dell'oggetto
    # - Valore --- int                              - Questo è il valore di tipo int assgnato che il nodo conterrà
    # - Sinistra --- "Nodo_Binario"                 - Questo argomento dovrebbe essere di classe nodo  binario e se non viene fornito niente sarà impostato a none questa var è un riferimento al nodo figlio di sinistra di classe appunto nodoBinario
    # - Destra --- "Nodo_Binario"                   - Questo argomento dovrebbe essere di classe nodo binario e se non viene fornito starà di deafult a none questa variabile è un riferimento al al nodo figlio di destra nodoBinario
    # -
    # -
    # -
    # -
    def __init__(self,V : int | str, left : 'Nodo_Binario' = None, right :'Nodo_Binario' = None):
        self._value = V #.self è una keyword che rappresenta l’istanza corrente della classe, permettendo di accedere agli attributi e ai metodi dell’oggetto all’interno della classe stessa.
        self._sx = left
        self._dx = right
        return
    
    #Questa funzione è un metodo di classe, vale a dire che va eseguito su degli oggetti e ha accesso alle var primitive
    # __repr__ restituisce una rappresentazione di un oggetto equivalente più o meno a un print restituisce una stringa ufficiale e non ambigua dell'oggetto, utile per il debugging.
    def __repr__(self):
        return f'Nodo_Binario({self._value})'
    
# Questo metodo si esegue su degli oggetti  e serve a stampare un albero binario in maniera visualmente comprensibile
def stampa_IN(radice, livello=0):
    if radice: # Se radice esiste
        stampa_IN(radice._sx, livello+1) # stampo il sottoalbero SX
    if radice:
        print('|--'*livello, radice)  # stampo nodo corrente
    if radice:
        stampa_IN(radice._dx, livello+1) # poi il sottoalbero DX
        
        
# Creiamo alcuni oggetti che rappresentano i nodi di un albero binario
# i nodi hanno un valore V che rappresenta il loro numero
# Eventualmente negli argomenti left e right se il nodo ha nodi figli troviamo riferimenti agli oggetti che sono
#nodi figli
"""
  Creiamo l'albero binario usando la classe Nodo_Binario
"""
#Questo nodo è il nodo radice se lo forniamo a stampa albero ricorsivamente verrà stampato tutto l'albero ricorsivamente
n3 = Nodo_Binario(3)
n4 = Nodo_Binario(4)
n5 = Nodo_Binario(5)
n6 = Nodo_Binario(6)
n1 = Nodo_Binario(1,left=n3,right=n4)
n2 = Nodo_Binario(2, left= n5, right=n6)
r = Nodo_Binario('radice', n1, n2)

#eseguiamo Stampa albero
stampa_IN(r)