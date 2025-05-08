# -*- coding: utf-8 -*-
"""
Ricorsione Lineare: Una funzione che richiama se stessa una sola volta in ogni invocazione. 
in questo caso il funzionain maniera lineare ovvero :  Recursive_Countdown(3):  Recursive_Countdown(2): Recursive_Countdown(1):
Recursive_Countdown(0): E qui si ferma
"""

def Recursive_Countdown(countdown_int):
    if countdown_int == 0:
        return " Buon Anno !"
    else:
        Recursive_Countdown(countdown_int-1)
        
#Recursive_Countdown(13)

# La sequenza di Fibonacci è una serie di numeri in cui ciascun numero è la somma dei due precedenti. 
# La sequenza inizia generalmente con 0 e 1. I primi numeri della sequenza sono 0, 1, 1, 2, 3, 5, 8, 13, ... 
# Questo codice calcola il numero di Fibonacci n-esimo usando la ricorsione La sequenza e data dal ciclo

"""
Ricorsione Annidata: Una funzione che richiama se stessa più volte. e una volta che ha raggiunto il caso base iniziera a calcolarsi i risultati 
delle vARIE chiamate annidate l'una nell'altra partendo dall'ultima e arrivando alla prima ovvero,  partendo da  1 e 0 e arrivando  a n a n-1
"""
def fibonacci(n): 
    if n <= 1:   #Caso Base
        return n # Stop alle chiamate ricorsive
    else:
        return fibonacci(n-1) + fibonacci(n-2) #chiamate ricorsive


#print([fibonacci(n) for n in range(1, 11)])

"""
Ricorsione a Coda accomulativa(Tail Recursion): Una forma di ricorsione dove la chiamata ricorsiva è l'ultima operazione della funzione. 
Il termine "ricorsione a coda" deriva dal fatto che la chiamata ricorsiva è "alla coda" o alla fine della funzione.
l'ultimo atto della funzione è chiamare se stessa, con nessun altro lavoro da fare dopo la chiamata ricorsiva. 
Questo significa che la funzione può terminare immediatamente dopo la chiamata ricorsiva, senza dover eseguire ulteriori operazioni.
Il risultato è Memorizzato nelle variabili passate di volta in volta alla funzione e quando alla fine il caso base è raggiunto 
viene restituito correttamente
"""

def creatore_Interi_Naturali_N(intero, risultato):
    if intero == 0:  # Caso Base
        risultato.append(0)
        return risultato  # Restituzione Del Risultato
    else:         
        risultato.append(intero)
        return creatore_Interi_Naturali_N(intero-1, risultato)
        

#print(creatore_Interi_Naturali_N(7, []))



def combinazioni_senza_ripetizione(arr, k):
    if k == 0:
        return [[]]
    if len(arr) == 0:
        return []
    
    # Inclusione dell'elemento corrente nelle combinazioni
    result_with_curr = combinazioni_senza_ripetizione(arr[1:], k-1)
    for comb in result_with_curr:
        comb.append(arr[0])
    
    # Esclusione dell'elemento corrente nelle combinazioni
    result_without_curr = combinazioni_senza_ripetizione(arr[1:], k)
    
    return result_with_curr + result_without_curr

# Esempio d'uso
#print(combinazioni(['A', 'B', 'C' , "D", "E"], 2))

"""
Questa funzione recursive_Least_Common_Divisor ricorsiva trova il minimo comune divisore di una lista di numeri interi.
Tramite un helper, Restituisce il minimo comune divisore di una lista di numeri interi se esiste, 
altrimenti restituisce False.
"""
def recursive_Least_Common_Divisor_Helper(list1,intero):
    if intero < max(list1):
        return False
    Result = True
    for i in list1:
        if i % intero != 0:
            Result =  False
            return recursive_Least_Common_Divisor_Helper(list1, intero+1)
    return intero

def recursive_Least_Common_Divisor(list1):
    Res = recursive_Least_Common_Divisor_Helper(list1, 2)
    return Res
    
        
        
#print(recursive_Least_Common_Divisor([3,7]))

"""
Questa Funzione Recursive_Occurences_Couter Conta le occorrenze di un elemento in una lista Usando la Ricorsione
Prende in input una lista e restituisce un dizionario con le occorrenze di ciascun elemento.
Usa una funzione helper per modificare un dizionario che memorizza le occorrenze di ciascun elemento.
"""
def Recursive_Occurences_Couter_Helper(Dizionario, lista):
    if len(lista) == 0:
        return Dizionario
    else:
        if lista[0] in Dizionario:
            Dizionario[lista[0]] += 1
        else:
            Dizionario[lista[0]] = 1
        return Recursive_Occurences_Couter_Helper(Dizionario, lista[1:])

    
def Recursive_Occurences_Couter(list1):
    return Recursive_Occurences_Couter_Helper({}, list1)

#print(Recursive_Occurences_Couter(["Nigger", "Yolo","Nigger","Nigger","Nigger","Yolo","Duce","Duce","Ses","Youmath"]))

