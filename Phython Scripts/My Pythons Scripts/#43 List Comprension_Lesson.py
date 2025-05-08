# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 11:22:22 2024

@author: david
"""

print("""
      List Comprension
 La list comprehension in Python è una tecnica efficente e concisa per creare liste applicando un'operazion
 e o un filtro a ogni elemento di un'altra lista (o altro iterabile). 
      
- - - - - - - - -SINTASSI GENERALE: - - - - - - - - - - 
   [espressione for elemento in iterabile if condizione]
   
   Esempi:
. . . . . . . Convertire una lista di stringhe a lista di interi:
                lista_interi = [int(x) for x in lista_stringhe if x.isdigit()]
        
        
. . . . . .Creare una lista di numeri quadrati:       
            quadrati = [x**2 for x in numeri]
            
. . . . . .Filtrare elementi con una condizione
            numeri_pari = [x for x in numeri if x % 2 == 0]

. . . . .Trovare la lunghezza minima degli elementi della lista 
            lunghezza_minima = min([len(elemento) for elemento in lista_stringhe])
            
        
- - - - - -Le list comprension si possono usare su qualsiasi iterabile come tuple insiemi- - - - - - -

insieme........insieme = {x**2 for x in lista} # Questo codice crea una lista nel quale ogni numero e la potenza di due del numero
 
stringa........result = [char.upper() for char in stringa] # Questo codice crea una lista di caratteri maiuscoli in una stringa

tupla........result = [x * 2 for x in tupla] # Questo codice crea una lista con ogni x nella tupla per 2
       
- - - - - - -Ovviamente l'output non deve essere per forza archiviato in una stringa- - - - - - - 
        # Stringa di esempio

. . . . . . .nuova_stringa = ''.join([char.upper() for char in stringa])


            In generale la sist comprension ha due vantaggi principali:
                - La brevitas, ovvero la sintesi di riassumere almeno 4 righe in una 
                    e impedisce l'accomularsi di righe per operazioni semplici
                - La Semplicità di lettura che riduce la possibilità di errori accidentali
                - l'efficienza del codice 
                - Velocità di scrittura
                
                Ecco un pò di esempi sul quale giocare : 
      """)
      
Lista_Str = ["Gatto", "CANE", "CAvALLO", "DEmagogia", "Suino", "Casa", "Albergo", "Centravanti", "tre"]
lunghezza_minima_parola = min([len(x) for x in Lista_Str])
lunghezza_max_parola = max([len(x) for x in Lista_Str])
print("lunghezza_Minima_Parola : " + str(lunghezza_minima_parola))
print("lunghezza_Massima_Parola : " + str(lunghezza_max_parola))

print("""
      In questo caso la list comprension ci ha risparmiato:
          lista_lunghezza = []
          for parola i  Lista_Str 
              lunghezza = len(parola)
              lista_lunghezza.append(lunghezza)
        lunghezza minima = min(lista_lunghezza)
        
        5 Rige di codice: lo stesso per la lunghezza massima 10 in totale
      """)
