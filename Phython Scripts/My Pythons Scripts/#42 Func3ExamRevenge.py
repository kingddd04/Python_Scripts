# Dopo aver Fallito l'esonero per non aver risolto Solo questo esercizio per cattiva comprensione e stanchezza ho deciso di risolverlo
# Non Era così difficile :/
import os

# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 08:31:34 2024

La Func3(revenge) prende in imput:
    
- Una lista di liste di parole
- Una lista di liste di interi 
- una stringa out, che indica a che percorso la funzione 146 deve scrivere un file di testo 

Per ogni lista di parole contenuta in lists il programma scrive una riga del file
in out. L'ordine di scrittura delle parole su ciascuna riga e' pero specificato dalla lista degli interi corrispondenti in listi, 
che vanno considerati come posizioni delle parole da leggere dalle liste per scriverle nel file. 
La funzione ritorna il numero totale di parole scritte nel file out.

Esempio se:

lists = [["monkey", "cat",],
         ["panda", "alligator"],
        [Zoo", 'zuu', 'zotero']]

listi [[1, 0], # prima scrivi la parola 1 e poi τα θ 
       [0, 1],# prima la e e poi la 1
       [2, 1, 0]] # prima la 2 pot la 1 pot la e


valore di ritorno e' 7 e nel file out viene scritto:
    
    
    "
    cat monkey
    panda alligator 
    zotero zuu zoo
    "

"""

def func3_revenge(lists, listint, filepath):
    counter = 0          # Counter Per Contare Le parole 
    stringa = ""         # Stringa Per Archiviare tutto il testo 
    for n_1 in range(len(listint)-1):    # Range per iterare nel primo livello di liste di liste
        row = ""                       # Stringa per contenere il risultato di ogni riga
        for n_2 in range(len(listint[n_1])-1):   #Range per iterare nel secondo livello di liste di liste
            counter += 1                       # incremento del counter delle paroòle
            loc_int = listint[n_1][n_2]        # Ricavo dell'intero presente alle posizioni listainteri[primo livello][secondo livello]
            loc_word = lists[n_1][loc_int]     # Ricavo della stringa presente alle posizioni listastringhe[primo livello][loc_int]
                                               # Loc_int indica quale è la posizione della parola da aggiungere in seguito
                                               #  Il mio errore è stato pensare che l'esercizio volesse una cosa più complessa perchè ero stanco
                                               # Non avevo letto bene il testo e ero stanco
            print("Coordinates_Scanned : "+str(n_1)+ " "+ str(n_2)+ " located_word : " + loc_word)  # Mostra Stato delle variabili
            row += loc_word                    # Aggiungiamo la parola corrente
            row += " "                         # Aggiungiamo uno spazio per la formattazione richiesta
        row.strip(" ")                         # Leviamo lo spazio di troppo a fine riga
        row += "\n"                            # Aggiungiamo a capo
        stringa += row                         # Aggiungiamo la riga al testo completo
                                               # In caso di errore di uguaianza bisognava eventualmente rimuovere lo /n  a fine testo
    with open(filepath, "w", encoding="utf8") as file:  # Apriamo il file
        file.write(stringa)                             # Scriviamo il file 
    print("\nwords counted : " + str(counter))          # Scrivi il numero di lettere contate
    return counter                                      # FINE
            
            
#Print Opzionali
            
path = os.getcwd() 
fullpath = path + "/"+ "FinalmenteHoAvutoLaVendetta.txt"

lists = [["monkey", "cat",],
         ["panda", "alligator"],
        ["Zoo", 'zuu', "zotero"]]
         
listint =  [[1, 0], # prima la parola 1 e poi τα θ 
            [0, 1],# prima la e e poi la 1
            [2, 1, 0]] # prima la 2 pot la 1 pot la e


func3_revenge(lists, listint, fullpath)