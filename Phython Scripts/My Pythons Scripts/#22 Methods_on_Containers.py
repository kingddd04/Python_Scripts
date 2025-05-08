List = [1,2,3,"four", 5]
Set = {1,2,3,4,5,6,7,8,9}
Dictionary = {1 : "uno", 2 : "due", 3 : "tre"}
Tuple =("sasso","carta","forbici")


print("""---Containers and their uses lesson n. 4---
      In python we have different ways of organizing datas
      
    - lists = are used to store multiple items in a single variable
              they allow duplicates
              
    - Sets = Are sets of unique items in a sigle place
    
    -Dictionaries = Are Data Structures that archieve keys and values
    
    -Tuples =A tuple is a collection which is ordered and unchangeable, but allow duplicates
                    
    
    --Metodi dei Contenitori Liste--

    • elemento in list
    • List1 + L2 crea una nuova lista concatenazione di List1 e List2
    • List1 * N replicazione di lista 1N volte e concatenazione di esse
    • List.append(elemento) aggiunta di un elemento alla fine
    • List[i] elemento all’indice i (lettura o assegnamento)
    • List.pop() estrazione distruttiva dell’ultimo elemento (ERR se vuota)
    • List.pop(i) estrazione distruttiva dell’elemento all’indice i 
    (ERRore se i non esiste)
    • List.insert(i, elemento) inserisce l’elemento 
    all’indice i (o in cima o in fondo)
    • L.remove(elemento) elimina la prima occorrenza dell’elemento 
    (Restituisce ERRore se non presente)
    • L.index(elemento) trova il primo indice in cui c’è l’elemento
    (ERRore se non è presente)
    • L.count(elemento) conta l’elemento
    • L.reverse() rovesciamento distruttivo della lista
    • L.sort() ordinamento distruttivo della lista
    
    --Metodi dei Contenitori Insieme--
    
    • elemento in S True se elemento è presente in S
    • S1 | S2 oppure S1.union(S2) unione (or)
    • S1 & S2 oppure S1.intersection(S2) intersezione (and, elementi in comune)
    • S1 - S2 oppure S1.difference(S2) insieme degli el. di S1 che non sono in S2
    • S1 ^ S2 oppure S1.symmetric_difference(S2) insieme degli elementi NON in comune (xor)
    • S.pop() estrazione distruttiva di un el. (ERR if empty)
    • S.add(elemento) aggiunta di un elemento
    • S.remove(elemento) rimozione di un el. (ERR if missing)
    • S1.update(S2) come S1 |= S2 (distruttiva)
    
    --Metodi dei Contenitori Insieme--
    
    • key in D True se la chiave è presente
    • D[key] accesso al valore con chiave key (R/W) (ERR se non presente)
    • D.keys() elenco delle chiavi (che sono uniche)
    • D.values() elenco dei valori (con duplicati)
    • D.items() elenco delle coppie (chiave, valore)
    • D.popitem() torna l’ultima coppia (k,v) e la rimuove
    • D1 | D2 nuovo dizionario con tutte le coppie di D1 e di D2 (prese nell’ordine)
    • D1.update(D2) modifica D1 aggiungendo le coppie (K,V) di D2 nell’ordine
    • D.get(key, default) se la chiave è presente ne torna il valore
    , altrimenti torna il valore di default
    • D.setdefault(key, default) se la chiave è presente ne torna il valore
    altrimenti la inserisce col valore di default (e lo torna)
    • D.pop(key, default) se la chiave è presente ne torna il valore e la rimuove,
    altrimenti torna il valore di default (o ERRORE se no default)
    • D.fromkeys(keys, value) costruisce un dizionario con le chiavi fornite,
    tutte associate allo stesso valore indicato
        
      """)

