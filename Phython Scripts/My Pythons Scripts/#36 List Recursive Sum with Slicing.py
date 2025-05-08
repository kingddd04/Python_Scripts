def Somma_Ricorsiva(lista):
    if lista:
        primo, *resto_della_lista = lista
        res = primo+Somma_Ricorsiva(resto_della_lista)
        print(primo, resto_della_lista,res)
        return res
    else:
        return 0
    
    
    
print(Somma_Ricorsiva([10,10,10,10,10,23,21,19]))

