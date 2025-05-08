

import albero

'''
    Es 12: 3 punti
    Un albero si dice binario completo se tutti i suoi nodi interni hanno esattamente 2 
    figli e tutte le foglie si trovano allo stesso livello.
    Si definisca la funzione es12(k ) ricorsiva (o che fa uso di funzioni o 
    metodi ricorsive/i) che:
    - riceve come argomenti  un intero k 
    - costruisce un albero binario completo di altezza k composta da nodi del tipo  
      Nodo definito nella libreria albero.py allegata. Gli identificatore delle foglie, 
      letti da sinistra a destra sono i 2^k-interi che vanno da 1 a 2^k (nota che 
      un albero binario completo di altezza k ha sempre 2^k foglie). Gli identificatori 
      dei nodi interni sono dati dalla somma degli identificatori dei due loro figli. 
    - torna come risultato la radice dell'albero costruito. 
    Esempio: 
    - es12(2)  crea e restituisce l'albero a sinistra 
    - es12(3) crea e restituisce l'albero a destra

        

                    10           2                       36         3      
             _______|______                      _______|______         
            |              |                    |              |        
            3              7     1              10             26      2  
         ___|___        ___|__               ___|___        ___|__      
        |       |      |      |             |       |      |      |                         136                        diff     nodi  prof
        1       2      3      4    0         3       7     11     15    1             36                 100            64       2     3 
                                           _|_     _|_    _|_    _|_            10      26        42          58        16       4      2  
                                          |   |   |   |  |   |  |   |          3   7  11  15   19    23    27    31     2        8      1
                                          1   2   3   4  5   6  7   8    0    1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16    1        16     0
                            
                                          

                                 
                                            
    '''
def get_root_int(k):
    res = 0
    n_int = 1
    max_n_nodes = 2**k
    for n in range(max_n_nodes):
        res += n_int
        n_int+=1
    return res
    
def Find_differenciator(root_int, depht):
    if depht == 1:
        return 2
    elif depht == 0:
        return 1
    else:
        res = 2
        for n in range(depht-2):
            res = res*2
            res = res*2
        return res
            
        
        
def Crea_albero(root,depht):
    if depht != 0:
        diff = Find_differenciator(root, depht)
        new_node = albero.Nodo(root,[Crea_albero(None])
        return new_node
    else:
        return None
    return None
        
        
        
        
        
        

def es1(k):
    root_int = get_root_int(k)
    Crea_albero(root, depht)
    return root_int

print(es1(4))
    
    
    
    
    
