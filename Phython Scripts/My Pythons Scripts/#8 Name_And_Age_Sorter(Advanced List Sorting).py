def ordina_lista_tuple(Tuple_List):
    #Sorted crea una nuova lista, usando key con lambda creiamo una funzione anonima che ordina alfabeticamente per il primo termine
    #E in ordine crescente per il secondo termine numerico, rispettivamente indicati dallo slicing [0][1]
    #con reverse= possiamo invertire entrambi gli ordini e con - possiamo invertire il secondo così abbiamo tutte le combinazioni
    
    New_Tuple_List = sorted(Tuple_List, key=lambda x: (x[0], x[1]))
    return New_Tuple_List

#Lista di Partenza
Complex_Tuple_List = [("Gina", 31),("Teo", 12),("Giuditta",27),("Romolo",44),("Giuseppe", 34),("Gesu", 33),("Noe", 300),("Enea", 25),("Priamo", 50), ("Anchise", 70),("Achille",29),("Andrea", 86),("Giuseppe",87),("Ulisse",75),("Juman",59),("Andrea", 29),("Skipper",30),("Private",27),("Riko",23),("Kolaski",32)]
print("Normal List = "+ str(Complex_Tuple_List)+"\n")

#Creazione Lista Ordinata 
New_Tuple_List = ordina_lista_tuple(Complex_Tuple_List)

print("Sorted List = "+ str(New_Tuple_List))
print("\nNow we  can remove a item from list with pop, pop() allows us to remove a item from a list and if needed we can store it a variable and print it!")
print("We can do the same with .remove but in this case the item gets found and deleted\n")
#eseguiamo delle operazioni di rimozione sulla lista ordinata
#Pop accetta un argomento indice, se non è specificato  rimuove l'ultimo elemento della lista e se richiesto tramite un assegazione di variable
#Lo restituisce, è una rimozione non distruttiva
Popped_Item = New_Tuple_List.pop(7)

print("\n-Removed_Item with pop at index 7 : "+ str(Popped_Item))
print("\n-Now we are gonna remove the tuple (Teo, 12) with list.remove()\n")

#.Remove rimuove un elemento dalla lista e lo cancella del tutto, rimozione distruttiva
New_Tuple_List.remove(("Teo", 12))
print("Resulting List after operations : " , str(Complex_Tuple_List))