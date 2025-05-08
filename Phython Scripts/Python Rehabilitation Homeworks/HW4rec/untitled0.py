lista = [("Chimica Generale Ed Inorganica", "2017/04/25", 31),
         ("Elettrotecnica", "2018/04/27", 31),
         ("Strategic Intelligence And Political Decision Making", "2020/09/14", 26),
         ("Seminario Multidisciplinare Per Approfondimenti Specifici", "2021/12/13", 24),
         ("Analisi Matematica", "2020/09/14", 28),
         ("Fisica Sperimentale", "2018/04/27", 30)]

# Ordina la lista in base alla data in ordine crescente
# In caso di parità, ordina in base al nome del corso in ordine alfabetico inverso
# Imposta reverse a True per ottenere questo risultato
lista_ordinata = sorted(lista, key=lambda t: (t[1], t[0]))

# Stampa la lista ordinata
for tupla in lista_ordinata:
    print(tupla)
    
    
    """
    new_list = []
    new_list1 =[]
    
    for tupl in exams_datas_tuple_list:
        name, date, voto = tupl
        date =  date.replace("/","")
        new_tupl = (name, date, voto)
        new_list.append(new_tupl)
        
    new_list_sorted = sorted(new_list, key=lambda t: (t[1], t[0]))
    for tupla in new_list_sorted:
        name, date, number = tupla
        date1 = "/".join([date[:4], date[4:6], date[6:]])
        new_tupl = (name, date1, number)
        new_list1.append(new_tupl)
    print(new_list1)

    """