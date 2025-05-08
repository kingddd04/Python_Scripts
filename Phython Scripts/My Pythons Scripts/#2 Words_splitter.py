# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 18:34:49 2024

@author: david
"""
# Printiamo l'interfaccia utente
print("----------------------\n")
print("Words Splitter 12.0\n")
print("----------------------\n")
#Creiamo l'imput dove l'utente inserirà i dati
my_String  = input("Ok,Insert your text here : ")
# Creiamo una lista che contenga ogni parola separata da un altra da uno spazio " " split è eseguito su mystring
words = my_String.split()
#Scrivi il risultato
print("\nParole : \n")
for word in words:
    print(word)



