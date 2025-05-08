# -*- coding: utf-8 -*-
"""
This code is intended to provide all the methods to solve recursive problems that require combination permutation and
combination with repetition


Overview :
    For each character in the input string, the function separates it from the rest of the string.
    It then recursively calls itself with the remaining characters and a reduced length (l-1).
    This recursive call generates all possible anagrams of the remaining characters.
    
note:l is not a very useful var can be sobstituted with a len(str) i only keeped it from the previus examples

-This type of algoritm is hard to understand 100% is better to just apply the method for reaching the desidered result--

"""

#This Funtion is a first code it works but can be improved
def Anagrammatore(string,l):
    if l == 1:  #Base Case stops the recursion when it arrives to the single letter
        return set(string)
    result = set()
    for position in range(len(string)): #  For each position corresponding a character of the string in imput
        char = string[position]
        others_char = string[:position] + string[position+1:] # Others Char = all other char first and later the current char wich is NOT included
        anagrammini = Anagrammatore(others_char,l-1)         #Recursive_Call
        for anagrammino in anagrammini:         #Adding of results
            result.add(char+anagrammino)
    return result
    
#print(Anagrammatore("tren", 4))

"""
Versione Migliorata 2.0

Non capisco appieno come il codice funzioni a fondo ma posso constatare:
    -L Algoritmo è preciso e non fa differenza tra insiemi e liste come container
    -Il codice usa un metodo di Soluzione Down to top risolve i piccoli problemi e poi
    usando lo stesso schema quello grande
    -Il codice somma lettera corrente e anagrammi anche derivati da chiamate precedenti
    -Il codice sembra utilizzare un approccio macroscopicamente randomico ma in fin dei conti logico e funzionale
    -Non ho una ragazza
    -Domani ho un esame
    -lo passo     
    - Non ce l'ho fatta xd 01/12/2024
    
    
    -Approfondimento: Questo Script fa quell'operazione che in combinatoria è chiamata permutazione semplice senza ripetizione
    e il numero di combinazioni è descritto dalla formula combinazioni_n = n! 
    Le permutazioni semplici senza ripetizioni sono i diversi modi di ordinare un insieme di oggetti distinti in cui ogni oggetto compare una sola volta.
    
"""
# 
def Anagrammatore_Upgrade(stringa):
    risultato = [] #A quanto Pare questo tipo di Algoritmo è preciso e funziona sia con lista sia con un insieme
    if len(stringa) == 1: # Caso Base
        return [stringa]  #Questo return di Stringa restituisce il caso base ovvero la lettera singola
    for posizione in range(len(stringa)): #Per Ciascuna posizione occupata da un Carattere
        carattere = stringa[posizione] #Carattere = carattere in quella posizione
        altri_caratteri = stringa[:posizione]+stringa[posizione+1:] #Altri Caratteri crea una stinga formata da i caratteri precedenti e successivi al corrente
        Anagrammi_minori = Anagrammatore_Upgrade(altri_caratteri) # La chiamata Ricorsiva crea combinazioni tra gli altri caratteri, ciascuna chiamata contiene in se i risultati delle chiamate precedenti
        for Anagramma_minore in Anagrammi_minori: #Per ciascuna stringa
            risultato.append(carattere+Anagramma_minore) #Assembliamo e aggiungiamo il risultato al risultato
    return risultato #Restituiamo il risultato

Anagramma = Anagrammatore_Upgrade("abc")
print(Anagramma)
print(len(Anagramma))

"""
Approfondimento : Le combinazioni semplici sono modi di scegliere 𝑘 oggetti da un insieme di 𝑛
    oggetti senza considerare l'ordine.    
    
                            n!
   Formula: c(n,k) =    -----------
                         k!*(n-k)!
                                            
"""

def combinazioni_senza_ripetizione(arr, k):
    if k == 0:  # Base caseit means the current combination is complete. 
        return [[]]
    if len(arr) == 0:
        return []
    
    # Inclusione dell'elemento corrente nelle combinazioni
    result_with_curr = combinazioni_senza_ripetizione(arr[1:], k-1)
    for comb in result_with_curr:
        comb.append(arr[0])
    result_without_curr = combinazioni_senza_ripetizione(arr[1:], k)
    return result_with_curr + result_without_curr

print(combinazioni_senza_ripetizione(["a", "bb", "c"], 2))

"""
Approfondimento : Le combinazioni con ripetizione sono modi di scegliere 𝑘
oggetti da un insieme di 𝑛 oggetti con possibilità di ripetizione. La formula è:
        
                    (n+k-1)!
      C(n,k) =     -----------
                    k!*(n-1)!
                    
        onput ['a', 'b', 'c'],  3
        output ['aaa', 'aab', 'aac', 'aba', 'abb', 'abc', 'aca', 'acb', 'acc', 'baa', 'bab', 'bac', 'bba', 'bbb', 'bbc', 'bca', 'bcb', 'bcc', 'caa', 'cab', 'cac', 'cba', 'cbb', 'cbc', 'cca', 'ccb', 'ccc']
                 
        input ["a","b","c"], 2
        output ['aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc']
                
"""


# This is a recursive helper function that generates all possible 
# combinations of elements from the array arr with repetition allowed.
# Prefix A string that accumulates the current combination of elements.
# k: The number of elements left to add to the current combination.
# arr: The array of elements to choose from.
# combinazioni: A list that stores all the generated combinations.

def combinazioni_helper(prefix, k, arr, combinazioni):
    if k == 0:
        combinazioni.append(prefix)
        return
    for letter in arr:
        combinazioni_helper(prefix + letter, k - 1, arr, combinazioni)


def combinazioni_con_ripetizione(arr, k):
    combinazioni = []
    combinazioni_helper("", k, arr, combinazioni)
    return combinazioni

#Comb_Con_Ripetizione = combinazioni_con_ripetizione(['a', 'bb', 'c'], 2)
#print(Comb_Con_Ripetizione)
#print(len(Comb_Con_Ripetizione))

"""
Combinazioni Con Ripetizione upgrade
"""

# La funzione Combinazioni_Con_Ripetizione_Upgrade genera tutte le possibili combinazioni
# di lunghezza k degli elementi di un insieme (set) con ripetizione permessa.
# Utilizza la ricorsione per costruire le combinazioni aggiungendo elementi uno alla volta.
# Altrimenti, chiama se stessa con k-1 per ottenere le combinazioni di lunghezza k-1,
def Combinazioni_Con_Ripetizione_Upgrade(set1, k):
    if k == 0:
        return {""} # Base case: an empty string is the only combination of length 0.
    Res = set()
    # previous_results stores the result of the recursive call to Combinazioni_Con_Ripetizione_Upgrade with k-1.
    # This means previous_results contains all combinations of length k-1 generated from the elements in set1.
    previous_results = Combinazioni_Con_Ripetizione_Upgrade(set1, k-1)
    
    for stringa in previous_results: # For each string of the previous results
        for s in set1: # For each element in the set
            Res.add(stringa + s) # Add the new combination to the set of results

    return Res # Return the set of all combinations found far and in the end the final result

#Esempio di utilizzo
print(Combinazioni_Con_Ripetizione_Upgrade({"a", "bb", "c"}, 2))