#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Operazioni da fare PRIMA DI TUTTO:
 1) Salvare il file come program.py
 2) Assegnare le variabili sottostanti con il tuo
    NOME, COGNOME, NUMERO DI MATRICOLA

Per superare l'esame è necessario:
    - risolvere almeno 3 esercizi di tipo func AND;
    - risolvere almeno 1 esercizio di tipo ex (problema ricorsivo) AND;
    - ottenere un punteggio maggiore o uguale a 18

Il voto finale è la somma dei punteggi dei problemi risolti.

IMPORTANTE: impostare DEBUG = True in `grade.py` per aumentare il livello
di debug e conoscere dove un esercizio genera errore.
Ricordare che per testare e valutare la ricorsione è necessario
impostare DEBUG = False
"""
nome       = "NOME"
cognome    = "COGNOME"
matricola  = "MATRICOLA"

#########################################

# %% ----------------------------------- FUNC1 ------------------------- #
'''func1: 2 punti
Definire la funzione func1(D1, D2), che riceve come argomenti due dizionari
D1 e D2: D1 ha stringhe come chiavi e interi come valori, mentre D2 ha interi
come chiavi e stringhe come valori.
La funzione deve trovare tutti i valori di D1 che sono chiavi di D2 e
restituire un elenco ottenuto concatenando le chiavi corrispondenti di
D1 con il valore corrispondente di D2. L'elenco deve essere ordinato in
ordine decrescente di lunghezza e, in caso di parità, in ordine
alfabetico crescente.

Esempio: se
D1 = {'aa': 1, 'bb': 2, 'cc': 1, 'ddd': 3, 'e':4}
D2 = {4:'bb', 1:'ff', 2:'ggg'}

func1(D1, D2) deve ritornare la lista ['bbggg', 'aaff', 'ccff', 'ebb']
'''
def func1(D1, D2):
    ## Scrivi qui il tuo codice
    pass
## Tests
# D1 = {'aa': 1, 'bb': 2, 'cc': 1, 'ddd': 3, 'e':4}
# D2 = {4:'bb', 1:'ff', 2:'ggg'}
# print(func1(D1, D2))  # ['bbggg', 'aaff', 'ccff', 'ebb']

# %% ----------------------------------- FUNC2 ------------------------- #
''' func2: 2 points
Definire la funzione func2(l) che prende in input una lista di int l e
modifica la lista in modo che l'elemento in posizione i sia la somma di
tutti gli elementi dalla posizione 0 a i. La funzione restituisce il
valore dell'ultimo elemento della lista modificata.

Esempio: se l = [3, -3, 6, -1, 10]
func2(l) deve ritornare il valore 15 e modificare l in [3, 0, 6, 5, 15].
'''
def func2(l):
    ## Scrivi qui il tuo codice
    pass

## Tests
# l = [3, -3, 6, -1, 10]
# print(func2(l) )
# print(l)
# %% ----------------------------------- FUNC3 ------------------------- #
''' func3: 2 points
Definire la funzione func3(words, l) che prenda in input:
    - un set di stringhe words
    - un int l
e restituisce un nuovo insieme con tutte le stringhe di lunghezza almeno l
nell'insieme words che sono una sottostringa di un'altra stringa in words.

Esempio: se words = {'cat', 'bobcat', 'albert', 'syndrome', 'robert', 'be', 'bert'}
func3(words, 3) deve ritornare il set {'cat', 'bert'}
'''

def func3(words, l):
    ## Scrivi qui il tuo codice
    pass

## Tests
# print(func3({'cat', 'bobcat', 'albert', 'syndrome', 'robert', 'be', 'bert'}, 3))

#%% ----------------------------------- FUNC4 ------------------------- #
""" func4: 4 punti
Definire la funzione func4(file_in, file_out, length, chars) che prenda in
input:
    -due stringhe che rappresentano i percorsi di due file di testo
    -un int length,
    -una stringa chars.
La funzione deve restituire l'elenco di tutte le parole trovate nel file
puntato da file_in con una lunghezza almeno pari a length e contenenti almeno 
uno dei caratteri della stringa chars. L'elenco deve essere ordinato per 
lunghezza decrescente e, in caso di parità, in ordine alfabetico.
Inoltre, la funzione deve scrivere le parole dell'elenco in output nel file
indicato da file_out separate da uno spazio bianco.

Esempio: func4('func4/in_01.txt', 'func4/out_01.txt', 5, 'asd')
     deve ritornare la lista['hippopotamus', 'elephant', 'cobra', 'horse', 'panda', 'snake']
     e scrivere la stringa 'hippopotamus elephant cobra horse panda snake' in func4/out_01.txt.
"""

def func4(file_in, file_out, length, chars):
    ## Scrivi qui il tuo codice
    pass
## Tests
# print(func4('func4/in_01.txt', 'func4/out_01.txt', 5, 'asd'))

# %% ----------------------------------- FUNC5 ------------------------- #
""" func5: 8 points
Definire la funzione func5(input_png, output_png, m, M) che prende come input
    - il percorso di un'immagine memorizzata in un file .png denominato input_png,
    - il percorso di un file png di output_png
    - due int m e M.
L'immagine di input contiene diverse linee orizzontali colorate su uno sfondo
nero. 
La funzione deve trovare le linee con una lunghezza compresa nell'intervallo
[m, M] e creare una nuova immagine con solo le linee trovate.

La funzione deve ritornare la differenza tra il numero di linee trovate
nell'immagine di input e quelle nell'immagine di output.
"""
import images

def func5(input_png, output_png, m, M):
    ## Scrivi qui il tuo codice
    pass

## Tests
# print(func5('func5/func5_test1.png', 'func5/func5_out1.png', 1, 20))
# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex1: 6 points
Definire la funzione ex1(chars, l), ricorsiva o che utilizza funzioni o
metodi ricorsivi, che prende in input un insieme di caratteri (ovvero 
stringhe di lunghezza uno) e un int l e restituisce l'insieme di tutte
le possibili stringhe palindrome di lunghezza l composte da caratteri
presi da chars.

Esempio:
    ex1({'a', 'b', 'c'}, 3) deve ritornare il set
    {'aaa', 'bab', 'cac', 'aba', 'bbb', 'cbc', 'aca', 'bcb', 'ccc'}
"""

# SUGGERIMENTO: se si aggiungono sia il primo che l'ultimo carattere (uguali!)
# le stringhe sono SEMPRE palindrome
# Generatore di Stringhe combinatorio alternativo
def genera_stringhe2(caratteri, lunghezza):
    if lunghezza == 0:
        return {''}
    elif lunghezza == 1:
        return caratteri
    else:
        sottostringhe = genera_stringhe(caratteri, lunghezza-2)
        stringhe = set()
        for s in sottostringhe:
            for c in caratteri:
                stringhe.add(c + s + c)
        return stringhe

# Questa funz genera tutte le combinazioni di caratteri possibili
def genera_stringhe(caratteri, lunghezza):
    if lunghezza == 1: # Caso Base
        return caratteri #Terminazione del programma
    else: # Se il caso base non si verifica allora procediamo con la chiamata ricorsiva
        sottostringhe = genera_stringhe(caratteri, lunghezza-1) #Chiamata ricorsiva che prende i la stringa corrente e la lunchezza della stringa meno di 1
        stringhe = set() # Variabile per archiviare tutti i risultati che vengono aggiunti passo passo a ogni chiamata
        for s in sottostringhe: # Sottostringhe contiene tutte le stringhe generate dalle chiamate ricorsive precedenti su più di una lettera
            for c in caratteri:# Per ogni carattere fornito
                stringhe.add(s + c) #ggiungiamo le varie lettere
                return stringhe #Restituiamo tutte le combinazioni

#Questa Funzione è la pricinpale e viene chiamata in primis dall'esercizio
def ex1(chars, l):
    stringhe = genera_stringhe(chars, l) # Invochiamo la funz ricorsiva genera_stringhe per ottenenere tutte le stringhe
    buone = set() # Creiamo un insieme per contenere il risultato 
    for s in stringhe: # Per ciascuna stringa nel risultato 
        if isPalindroma(s): #Se la stringa fornita alla funzione ispalindroma fa restituire true
            buone.add(s) # Aggiungo la stringa verificata all'insieme dei risultati
    return buone # Restituiamo la stringa di risultato

# Questa Funzione consente di verificare se la parola è palindroma come? semplicemente invertendola e verificando che rimanga uguale
# Questa è una funzione alternativa tuttavia non viene usata anche se è più semplice veloce e compatta
# Usiamo l'atra a scopo formativo puramente didattico.
def isPalindroma_Alternative_Method(stringa):
    inverted_str = stringa[::-1] 
    if inverted_str == stringa:
        return True
    else:
        return False

# Questa Funzione consente di verificare se una stringa è palindroma
def isPalindroma(stringa):
    for i in range(len(stringa)//2):# per ciascun numero nella lunghezza della stringa da 0 a lunghezza str diviso 2
        if stringa[i] != stringa[-i-1]: # Se la lettera corrente è diversa dalla lettera opposta nella stringa 
            return False # Restituisci false il test non è superato
    return True # Se non accade False Restituisci true perchè la parola è palindroma

# Test per verificare il corretto funzionamento
print(genera_stringhe2({'a', 'b', 'c'}, 3))
print(genera_stringhe({'a', 'b', 'c'}, 3))
print(ex1({'a', 'b', 'c'}, 3))

# %% ----------------------------------- EX.2 ------------------------- #
"""
Ex2: 6 points
Definire una funzione ex2(root), ricorsiva o che utilizzi funzioni o
metodi ricorsivi, che prende come input root un'istanza di un BinaryTree
(come definito nel modulo tree) che rappresenta la radice di un albero
binario con valori int. La funzione deve restituire una coppia (v, l)
con il valore e il livello del nodo dell'albero con il prodotto massimo v*l.
In caso di più nodi con lo stesso prodotto, la funzione restituisce quello
con il livello minimo.
Si supponga che la radice si trovi al livello 1.

Ad esempio, se l'input è la radice del seguente albero:

               6              livello 1
              / \             
             5   16           livello 2
            /   / \
           4   10  6          livello 3
              /   / \
             7   8  1         livello 4
             
ci sono due nodi con prodotto massimo v*l=32, cioè 8*4 e 16*2, quindi
la funzione dovrebbe restituire la coppia (16, 2).
"""
import tree

# Questa Funzione restituisce un modo per riodirnare la lista di tuple richiesta dall'esercizio
def criterio(coppia):
    v, l = coppia
    return v*l, -l # Il trucco qua è che eliminando l da ogni risultato evitiamo le parità e quindi gli errori

# Funzione che viene chiamata all'inizio e prende in imput la radice di un albero binario 
# La funzione usa scandisci_albero per ottenere tutte una lista di tuple fi tutte le coppie valore livello
# La Funzione restituisce una lista di coppie tuple valore per livello dell'albero

def ex2(root):
    ## Scrivi qui il tuo codice
    coppie = []
    scandisci_albero(root, 1, coppie)#Chiamiamo la funzione ricorsiva fornendo la radice la profondità e un risultato
    print(coppie)
    return max(coppie, key=criterio) # Restituiamo il massimo della lista di tuple ordinata tramite la funzione criterio

# Questa e la funzone ricorsiva che scandisce l'albero funziona chiamandosi ricorsivamente sull'attributo 
# Dell'ogetto che è un riferimento a un altro oggetto il quale potrebbe rappresentare un altro nodo dell'albero
# Se Questo oggetto esiste. Se non esiste non viene eseguito l'if e la funzione si termina.

def scandisci_albero(radice, livello, L):
    if radice is not None: # Se la radice esiste
        L.append((radice.value,livello)) #Estraiamo dall'oggetto l'attributo che contiene il valore e il livello, e mettiamoli in una tupla che appendiamo al risultato
        scandisci_albero(radice.left,  livello+1, L) #Eseguimo la funzione a sin
        scandisci_albero(radice.right, livello+1, L) #Eseguimo la funzione a destra

#Creiamo un albero albero binario di test
T = tree.BinaryTree.fromList([6, [5, [4, None, None], None ], [16, [10, [7, None, None], None],
                                                                [6, [8, None, None], [1, None, None]]]])
print(ex2(T))

# %%#################################################################################
if __name__ == '__main__':
    # Scrivi qui i tuoi test
    print('*'*50)
    print('Devi eseguire il grade.py se vuoi debuggare con il grader incorporato.')
    print('Altrimenit puoi inserire qui del codice per testare le tue funzioni ma devi scriverti i casi che vuoi testare')
    print('*'*50)
