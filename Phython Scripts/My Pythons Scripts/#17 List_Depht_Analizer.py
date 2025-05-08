def find_list_depht(deep_list):
    res = []
    # Per ogni elemento di un eventuale lista di liste        
    for current_list in deep_list:
        counter = 0
        list_str = str(current_list)
        for char in list_str:
            if char == "[":
                counter += 1
        # Per rendere lo script funzionale anche sulle liste singole basta contare una parentesi in piu
        if len(deep_list) == 1:
            counter += 1
        res.append(counter)
    return res

print("""
      ---List Depht Analizer---
      
This tool Can misure how much your list is deep! 
      
      """)

res = find_list_depht([[[]]])
print("\nProfondità delle lista o delle liste : ", end= "")
for i in res :
    print(str(i)+ " ", end="")
# max trova il numero piu grande in una lista e min fa l'opposto
print("\nProfondità massima = "+ str(max(res)))
print("Profondità minima = "+ str(min(res)))
    