#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Operazioni da svolgere PRIMA DI TUTTO:
 1) Salvare il file come program.py
 2) Assegnare le variabili sottostanti con il proprio
    NOME, COGNOME, NUMERO DI MATRICOLA
 3) Rinominare la directory examPY inserendo il proprio numero di matricola

Per superare l'esame e' necessario soddisfare tutti i seguenti vincoli:
    - risolvere almeno 3 esercizi di tipo func; AND
    - risolvere almeno 1 esercizio di tipo ex; AND
    - ottenere un punteggio maggiore o uguale a 18

Il voto finale e' la somma dei punteggi dei problemi risolti.
Attenzione! DEBUG=True nel grade.py per migliorare il debugging.
Per testare correttamente la ricorsione è, però, necessario DEBUG=False.

"""
nome       = "Davide"
cognome    = "Di Stefano"
matricola  = "00121"


#########################################

################################################################################
# ---------------------------- SUGGERIMENTI PER IL DEBUG --------------------- #
# Per eseguire solo alcuni dei test, si possono commentare le voci
# corrispondenti ai test che non si vogliono eseguire all'interno della lista
# `test` alla FINE di `grade.py`.
#
# Per eseguire il debug di funzioni ricorsive potete disattivare il test di
# ricorsione, assegnando `DEBUG=True` all'interno file `grade.py`.
#
# L'impostazione DEBUG=True attiva anche lo la stampa a terminale dello STACK
# TRACE degli errori, che permette di conoscere il numero della linea di
# program.py che ha generato un errore.
################################################################################


# %% -------------------------------- FUNC.1 -------------------------------- #
''' func1: 2 punti
Si definisca la funzione func1(string_list1, string_list2) che riceve in
ingresso due liste di stringhe e restituisce una nuova lista di stringhe
contenente le stringhe presenti soltanto in una delle due liste in ingresso
(ossia, che non compaiono in entrambe le liste). La lista in output
dev'essere ordinata in ordine lessicografico inverso.
'''
def func1(string_list1, string_list2):
    New_List = []
    for item in string_list1:
        if item in string_list2:
            continue
        else:
            New_List.append(item)
            
    for string_obj in string_list2:
        if string_obj in string_list1:
            continue
        else:
            New_List.append(string_obj)
            
    New_List.sort(reverse=True)
    return New_List

# %% -------------------------------- FUNC.2 -------------------------------- #
''' func2: 2 punti
Si definisca una funzione funct2(path_to_file) che riceve in ingresso
una stringa che rappresenta il percorso ad un file testuale. La funzione
deve restituire il dizionario che associ ad ogni carattere nel testo il
conteggio delle sue occorrenze.

Esempio:
  Il contenuto di func2_test_1.txt è:
    cat rat fat
    art
  L'output atteso dall'invocazione di func2('func2/func2_test_1.txt') è:
  {'c':1, 'a':4, 't':4, 'r':2, 'f':1, ' ':2, '\n':1}

Nota:
  Aprire il file con encoding 'utf-8'.
'''
def func2(path_to_file):
    occurrences_dictionary = {}
    with open(path_to_file, "r", encoding="utf-8") as txt:
        text_datas = txt.read()
    for letter in text_datas:
        if letter in occurrences_dictionary:
            occurrences_dictionary[letter] += 1
        else:
            occurrences_dictionary[letter] = 1
    return occurrences_dictionary
    
            
# %% -------------------------------- FUNC.3 -------------------------------- #
'''  func3: 2 punti
Si definisca una funzione func3(a_list) che riceve in ingresso una lista
di numeri ed opera su di essa (ossia, provocando side-effect) rimuovendo tutti
gli elementi uguali al massimo e al minimo.
La funzione deve restituisce la differenza fra la lunghezza iniziale e la
lunghezza finale della lista.

Esempio:
    se a_list = [3, 12, -3, 4, 6, 12]
    dopo la chiamata a func3(a_list) si ha che
    a_list = [3, 4, 6]
    e la funzione restituisce 3.

IMPORTANTE: la lista `a_list` deve risultare cambiata alla fine
dell'esecuzione della funzione.
''' 

def func3(a_list):
    to_rem = []
    Raw_List_Len = len(a_list)
    Max_n = max(a_list)
    Min_n = min(a_list)
    for n in a_list:
        if n == Max_n:
            to_rem.append(n)
        if n == Min_n:
            to_rem.append(n)
    for x in to_rem:
        if x in a_list:
            a_list.remove(x)
    Elaborated_List_Len = len(a_list)
    return Raw_List_Len-Elaborated_List_Len
        
        
# %% -------------------------------- FUNC.4 -------------------------------- #
""" func4: 6 punti
Si definisca una funzione func4(input_filepath, output_filename) che
riceve in ingresso due percorsi a file:
  - Il file `input_filepath` contiene una sequenza di parole, ossia stringhe
    separate da spazi, tabulazioni o invii a capo.
  - Il file `output_filename` indica dove salvare un nuovo file di testo,
    i cui contenuti sono specificati di seguito.
Il file in output deve contenere tutte le parole presenti in
`input_filename`, ripetute una sola volta e organizzate in righe nel modo
seguente.

Le righe nel file di output sono in ordine alfabetico.
All'interno di ogni riga, le parole
  - hanno la stessa lettera iniziale, senza distinzione fra maiuscole e
    minuscole;
  - sono separate da uno spazio;
  - sono ordinate in base alla loro lunghezza e, in caso di pari
    lunghezza, in base all'ordine alfabetico, senza distinzione fra
    maiuscole e minuscole. Nel caso in cui nessuno dei criteri sin qui
    forniti distingua le parole, quelle coincidenti devono essere
    disposte secondo ordinamento lessicografico (ovverosia, si tiene conto
    della differenza tra lettere maiuscole e minuscole solo in ultima
    istanza).

La funzione deve restituire il numero di righe scritte nel file
`output_filename`.

Esempio:
  Nel file 'func4/func4_test1.txt' sono presenti le seguenti due righe:
cat bat    rat
Condor baT
  L'invocazione di func4('func4/func4_test1.txt', 'func4/func4_out1.txt')
  dovrà scrivere nel file 'func4/func4_out1.txt' le seguenti tre righe
  restituendo il valore 3:
baT bat
cat Condor
rat
"""

def func4(input_filename, output_filename):
    # Inserire qui il proprio codice
    pass

# %% -------------------------------- FUNC.5 -------------------------------- #
""" func5: 8 punti
Si definisca una funzione func5(imagefile, output_imagefile, color) che riceve
in ingresso due stringhe che rappresentano due percorsi a file di immagini PNG e
un colore fornito come una tupla RGB.
L'immagine nel file `imagefile` contiene esclusivamente segmenti orizzontali
bianchi su uno sfondo nero. Ogni riga ha al più un segmento bianco.
La funzione deve creare una nuova immagine in cui sono presenti gli stessi
segmenti dell'immagine in ingresso e modificare il colore dei segmenti con
lunghezza massima utilizzando il colore `color` in ingresso.

L'immagine così ottuenuta deve essere salvata in formato PNG nel file con
percorso `output_imagefile`.

La funzione restituisce il numero di segmenti colorati nell'immagine
in output.
"""
import images
def chec_line(Matrix,y):
    lenght_line = 0
    for x in Matrix[y]:
        if x != (0,0,0):
            lenght_line +=1
    return lenght_line

def func5(imagefile, output_imagefile, color):
    line_list = []
    black = (0,0,0)
    Matrix = images.load(imagefile)
    n_lines = 0
    N_Y = len(Matrix)
    N_X = len(Matrix[0])
    for y in range(0,N_Y):
        line_l = chec_line(Matrix,y)

        if line_l != 0:
            line_list.append(line_l)
    max_l = max(line_list)
    for y in range(0,N_Y):
        loc_len = chec_line(Matrix,y)
        if loc_len == max_l:
            n_lines += 1
            for x in range(0,N_X):
                if Matrix[y][x] != black:
                    Matrix[y][x] = color
    images.save(Matrix, output_imagefile)
    return n_lines
            
    
#print(func5("func5/image01.png", "func5/expectedigga01.png",(0,0,0)))

# %% --------------------------------- EX.1 --------------------------------- #
"""
Ex1: 6 punti

Implementare la funzione ex1 (in modo ricorsivo o utilizzando funzioni
ricorsive) come segue. La funzione ex1 riceve in ingresso i seguenti
argomenti:
  - `directory`, una stringa che rappresenta il percorso di una directory
  - `ext`, una stringa che rappresenta un'estensione di file.
La funzione deve cercare in modo ricorsivo all'interno della `directory`
e in tutte le sue sottodirectory i file che abbiano `ext` come estensione.
Questi file devono essere interpretati come file di testo. La funzione
ex1 deve calcolare la somma delle dimensioni di tutti i file trovati
nelle sottodirectory e restituire un dizionario strutturato come
come segue:
  - le chiavi sono tutte le sottodirectory in cui è presente almeno
    un file con estensione `ext`
  - i valori sono la somma delle dimensioni di tali file contenuti in quella
  sottodirectory.
Le sottodirectory devono essere riportate con il percorso relativo alla
directory corrente. Per esempio, data la struttura di directory:
A/
  B/
    file1.png    #4 byte
  file2.txt      #8 byte

L'invocazione `ex1("A", ".png")` deve restituire `{"A/B":4}`

La dimensione di un file può essere calcolata contando il numero di caratteri
letti dal file.

Si consiglia di utilizzare le funzioni os.listdir, os.path.isfile e
os.path.isdir e NON la funzione os.join in Windows. Utilizzare
la concatenazione tra stringhe con il carattere '/'.
"""

import os


def ex1(directory, ext):
    size = 0
    dictionary = {}
    for path in os.listdir(directory):
        fullpath = directory +"/" + path
        if fullpath.endswith(ext):
            L_size = os.path.getsize(fullpath)
            size += L_size
    for path0 in os.listdir(directory):
        fullpath = directory +"/" + path0
        if os.path.isdir(fullpath):
            Loc_dict = ex1(fullpath, ext)
            dictionary.update(Loc_dict)
    if size != 0:
        dictionary[directory] = size
    return dictionary
            
        
        
            
    
            
        



# %% --------------------------------- EX.2 --------------------------------- #
"""
Ex2: 6 punti

Si definisca la funzione ex2(root) che riceve in ingresso la radice di un
albero binario, come definito nella classe `BinaryTree` del modulo tree.py.
La funzione deve restituire la somma di tutti i valori associati ai nodi che
sono ad un livello pari nell'albero con radice `root`, e sottraendo tutti i
valori associati ai nodi ad un livello dispari. La radice si assume a livello 0.

Esempio:

        ______5______                        ______2______
       |             |                      |             |
       8__        ___2___                __ 7__        ___5___
          |      |       |              |      |      |       |
          3      9       1             _4_     3_    _0_     _5_
                                      |   |      |  |   |   |   |
                                      2   -1     1  8   3   2   9

  Se l'albero è quello di sinistra, la funzione deve restituire il valore 8.
  Se l'albero è quello di destra, la funzione deve restituire il valore -22.
"""


def ex2(root):
    # Inserire qui il proprio codice
    list1 = Trova_Pari_Disp(root, 0, [0,0])
    res = list1[0]-list1[1]
    return res


def Trova_Pari_Disp(root,profondita, ris_lista):
    if root:
        if profondita % 2 == 0 or profondita == 0:
            ris_lista[0]+= root.value
        if profondita % 2 != 0 :
            ris_lista[1] += root.value
        Trova_Pari_Disp(root.right, profondita +1, ris_lista)
        Trova_Pari_Disp(root.left, profondita +1, ris_lista)
        
        return ris_lista
    

###################################################################################
if __name__ == '__main__':
    # Place your tests here
    print('*' * 50)
    print('ITA\nEseguire grade.py per effettuare il debug con grader incorporato.')
    print('Altrimenti, inserire codice qui per verificare le funzioni con test propri')
    print('*' * 50)
    print('ENG\nRun grade.py to debug the code with the automatic grader.')
    print('Alternatively, insert here the code to check the functions with custom test inputs')
    print('*' * 50)
