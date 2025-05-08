# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 09:17:22 2024

@author: david
"""


class Nodo_Bimario:

    def __init__(self, valore, sinistra, destra): # Costr
        self.valore = valore
        self.sinistra = sinistra
        self.destra = destra
        return

    def __repr__(self):
        return f'Nodo_Binario({self.valore})'


"""
Creazione di un oggetto Nodo_Binario e rappresentazione tramite metodo __repr__
"""
#nodo = Nodo_Bimario(10,None,None)
# print(nodo.__repr__())

"""
Creiamo un albero binario Chiamando la classe Nodo_Binario per creare ogni nodo dell'albero binario
-
                           6              livello 1
                          / \             
                         5   16           livello 2
                        /   / \
                       4   10  6          livello 3
                          /   / \
                         7   8  1         livello 4
"""

n1 = Nodo_Bimario(1, None, None)
n8 = Nodo_Bimario(8, None, None)
n7 = Nodo_Bimario(7, None, None)
n4 = Nodo_Bimario(4, None, None)
n6 = Nodo_Bimario(6, n8, n1)
n10 = Nodo_Bimario(10, n7, None)
n16 = Nodo_Bimario(16, n10, n6)
n5 = Nodo_Bimario(5, n4, None)
Nodo_Radice = Nodo_Bimario(6, n5, n16)


def stampa_Albero(root, livello=0):
    if root:  # Se radice esiste
        stampa_Albero(root.sinistra, livello+1)  # stampo il sottoalbero SX
    if root:
        print('|--'*livello, root)  # stampo nodo corrente
    if root:
        stampa_Albero(root.destra, livello+1)  # poi il sottoalbero DX
    return


"""
In questo semplice esercizio Scandiremo l'albero e troveremo il numero di numeri pari e dispari

nota: alla fine il risultato res è restituito dal return della prima chiamata ricorsiva siccome tutte le chiamate precedenti aggiornano res che è passato come riferimento alla
funzione di volta in volta finche alla fine non è restituita tramite il return finale
"""


def Conta_Pari_Dispari(root, res):
    if root:
        if root.valore % 2 == 0:
            res[0] += 1
        else:
            res[1] += 1
        Conta_Pari_Dispari(root.sinistra, res)
        Conta_Pari_Dispari(root.destra, res)
    return res


#res = Conta_Pari_Dispari(Nodo_Radice, [0, 0])
#print("Numeri Pari trovati = " + str(res[0]) + " Numeri Dispari trovati= " + str(res[1]))

"""
In questo Esercio Per ogni nodo dell'albero Sostituiamo il suo attributo valore con la somma dei suoi valori più il suo valore corrente
                           6              livello 1       63
                          / \                           /  \
                         5   16           livello 2    9   48
                        /   /  \                      /  /  \
                       4   10  6          livello 3  4  17 15
                          /   / \                       /  / \
                         7   8  1         livello 4    7  8  1
                         
                         |--|-- Nodo_Binario(4)
                         |-- Nodo_Binario(9)
                          Nodo_Binario(63)
                         |--|--|-- Nodo_Binario(7)
                         |--|-- Nodo_Binario(17)
                         |-- Nodo_Binario(48)
                         |--|--|-- Nodo_Binario(8)
                         |--|-- Nodo_Binario(15)
                         |--|--|-- Nodo_Binario(1)
"""


def Somma_Figli(root):
    if root is None:
        return 0
    return root.valore + Somma_Figli(root.sinistra) + Somma_Figli(root.destra)

#print(Somma_Figli(Nodo_Radice))

def Scandisci_E_Modifica_Albero(root):
    if root:
        root.valore = Somma_Figli(root)
        Scandisci_E_Modifica_Albero(root.sinistra)
        Scandisci_E_Modifica_Albero(root.destra)
    return

#Scandisci_E_Modifica_Albero(Nodo_Radice)
#stampa_Albero(Nodo_Radice)


"""
In quessto esercizio Cerchiamo la tupla che rappresenta il rapporto maggiore tra valore del nodo e la sua profondità
Otteniamo ciò scannerizzando l'albero binario alla ricerca di tutti valori e poi  li ordiniamo tramite 
.sort e la funzione Ordina_lista_Tuple
"""

def Scandisci_albero(root, depht_level, raw_res):
    if root:
        loc_tuple = (root.valore, depht_level)
        raw_res.append(loc_tuple)
        Scandisci_albero(root.sinistra, depht_level+1, raw_res)
        Scandisci_albero(root.destra, depht_level+1, raw_res)
        return raw_res




def Ordina_lista_Tuple(x):
    return x[0]*x[1], -x[1]

def Operazioni_Esercizio(root):
    lista_Tuple = Scandisci_albero(root, 1, [])
    lista_Tuple.sort(key=Ordina_lista_Tuple)
    Primo_Elemento = lista_Tuple[-1]
    return Primo_Elemento


#print("\nRapporto Più Elevato : "+str(Operazioni_Esercizio(Nodo_Radice))+"\n")



"""
In questo esercizio sommiamo tutti i nodi di una medesima profondità 
il codice funziona grazie al passagggio dei risultati negli argomenti e grazie al blocco della ricorsione
sui nodi none La lista è costruita ricorsivamente 

Schema delle chiamate:
    
[6]  esecuz su nodo rad
[6, 5]  esec su nodo 5
[6, 5, 4]  esec su nodo 4
[6, 5, 4]  esecuzione su nodo none bloccata          6              livello 1
[6, 5, 4]  esecuzione su nodo none bloccata         / \             
[6, 5, 4] esecuzione su nodo none bloccata         5   16           livello 2
[6, 21, 4]  esecuzione su nodo 16                 /   / \
[6, 21, 14] esecuz su nodo 10                    4   10  6          livello 3
[6, 21, 14, 7] es su nodo 7                         /   / \
[6, 21, 14, 7] esecuzione su nodo none bloccata    7   8  1         livello 4
[6, 21, 14, 7]  esecuzione su nodo none bloccata  
[6, 21, 14, 7]  esecuzione su nodo none bloccata  
[6, 21, 20, 15]  esec su nodo 8
[6, 21, 20, 15]   esecuzione su nodo none bloccata  
[6, 21, 20, 15]    esecuzione su nodo none bloccata  
[6, 21, 20, 16]    es su nodo 1
[6, 21, 20, 16]      esecuzione su nodo none bloccata  
[6, 21, 20, 16]  esecuzione su nodo none bloccata  
"""


def ex1_H(root, depht, out_res):
    
    if root is None:   #Questa Riga è il nostro salvavita che blocca le esecuzione sui nodi inesistenti None
        return 
    
    if depht >= len(out_res): # Se la profondita è maggiore alla lunghezza del risultato allunghiamo la lista
        out_res.append(0)     # Affinche possa contenere il risultato che sta per essere generato
        
    loc_V = root.valore      # Estraiamo il valore
    out_res[depht] += loc_V   # Incrementiamo la posizione della lista corrispondente alla profondita con il val corrente 
    ex1_H(root.sinistra, depht+1, out_res) # Chiamiamo la ricorsione su nodo sin
    ex1_H(root.destra, depht+1, out_res)   # idem per il destro
    return out_res    # Non sono generati errori perchè le ricorsioni possono lavorare anche non in parallelo
                      # Perchè ogni chiamata ricorsiva ha la sua profondità al quale viene adattata la l dei risultati
                      # che avanza insieme alle chiamate e non per forza e quindi se la lista è sufficientemente grande 
                      #  non sara allungata

def ex1(root, out_res):
    result = ex1_H(root, 0 , out_res)
    return result
    
#print(ex1(Nodo_Radice, []))


"""
Questo Esercizio è simile al precedente con la sola differenza che il risultato vuole una lista di set anziche una lista semplice
"""

def ex11_H(root, lista, profondità):
    if root is None:
        return
    if len(lista) <= profondità:
        lista.append(set())
    loc_Val = root.valore
    lista[profondità].add(loc_Val)
    ex11_H(root.destra, lista, profondità+1)
    ex11_H(root.sinistra, lista, profondità+1)
    return lista
    

def ex11(root):
    res = ex11_H(root, [], 0)
    return res
    
print(ex11(Nodo_Radice))

"""
Può non essere scontato ma effettivamente Si possono sommare un valore  di un nodo radice con il valore dei nodi figli
e si può accedere al valore del nodo figlio destro e sinistro a partire da quello radice
"""
def Somma_Solo_Nodo_E_Figli(root):
    return root.valore + root.sinistra.valore + root.destra.valore

#print(Somma_Solo_Nodo_E_Figli(Nodo_Radice))

 

"""
In questo esercizio sommiamo ogni nodo con il valore dei suoi due figli a partire dal basso
"""   


def Somma_FIgli_Dal_Basso(root):
    if root is None:
        return 0

    left_sum = Somma_FIgli_Dal_Basso(root.sinistra)
    right_sum = Somma_FIgli_Dal_Basso(root.destra)

    root.valore += left_sum + right_sum
    return root.valore

#print(Somma_FIgli_Dal_Basso(Nodo_Radice))
#stampa_Albero(Nodo_Radice)

"""
Questo esercizio trova il numero di Nodi e quali sono a una determinata profondita
"""

def Conta_Nodi_1(root):
    res = [0]
    Conta_Nodi_2(root, res)
    return res[0]

def Conta_Nodi_2(root, n_nodi):
    if root:
        n_nodi[0] += 1
        Conta_Nodi_2(root.destra, n_nodi)
        Conta_Nodi_2(root.sinistra, n_nodi)
    return n_nodi 


#print(Conta_Nodi_1(Nodo_Radice))

"""
Questo esercizio trova il valore di tutti i nodi  e li mette in una stringa
il risultato si può archiviare per riferimento o tremite il return
"""

def Trova_Nodi(root):
    res = Trova_nodi_2(root, [])
    return res
        

def Trova_nodi_2(root,res):
    if root:
        res.append(root.valore)
        Trova_nodi_2(root.destra, res)
        Trova_nodi_2(root.sinistra, res)
        return res

#print(Trova_Nodi(Nodo_Radice))


"""
Questo esercizio torna i nodi a una determinata prondita
Conta i Nodi a profondità "profondita_ric" archivando il risultato in una variabile passata per riferimento
"""

def Conta_a_profondità(radice, profondita_ric ):
    num_di_elementi = [0]
    Conta_a_profondità_Helper(radice, profondita_ric, num_di_elementi,  0)
    return num_di_elementi
    

def Conta_a_profondità_Helper(radice, profondita_ric, num_di_elementi, profondità):
    if radice:
        if profondità == profondita_ric:
            num_di_elementi[0] += 1
        Conta_a_profondità_Helper(radice.destra, profondita_ric, num_di_elementi, profondità+1)
        Conta_a_profondità_Helper(radice.sinistra, profondita_ric, num_di_elementi, profondità+1)
    
    
print(Conta_a_profondità(Nodo_Radice, 1))
    