''' 
    Data una sequenza S di  interi definiamo sequenza derivata da S la  sequenza di n interi dove l'i-esimo 
    elemento e' dato dalla somma dei primi i interi di S.
    Ad esempio:
    la sequenza derivata da 
    S= 2, -3, -4,  4, 4, -5, 3, 1,-1  e'
       2, -1, -5, -1, 3, -2, 1, 2, 1.
       ['2', '-1', '-5', '-1', '3', '-2', '1', '2', '1']
    
    Implementate la funzione es41(fname1) che prende in input l'indirizzo fname1 di un file di testo contenente una 
    sequenza S di interi e restituisce il numero che compare con maggior frequenza nella sequenza derivata da S.
    Nel caso in cui i numeri con maggior frequenza siano piu' di uno viene restituito quello di valore massimo.
    Ad esempio se il file fname contiene la sequenza S= 2, -3, -4,  4, 4, -5, 3, 1, -1   la funzione restituisce il valore 2.
    Nel file fname1, ciascun intero della sequenza  e' separato dal successivo da una virgola ed eventuali spazi.
    '''
    # inserisci qui il tuo codice


# Questa funzione Restituisce la lista "strana" richiesta dall'esercizio
def Find_sequence(list1):
    res = []
    temp = [] # temp contiene i numeri via via da sommare
    for n in range(len(list1)):
        temp.append(list1[n]) 
        temp_sum = sum(temp) # Sommiamo i numeri precedenti
        res.append(temp_sum) # Aggiungiamo la somma
    return res



def find_Most_Occurred(second_sequence_str):
    max_n_occ = 0 # NUmero massimo di occorrenze
    max_n = 0     # Numero che ricorre di più
    for i in second_sequence_str:  
        occ_numb = second_sequence_str.count(i) #count non riesce a identificare i - degli interi quindi dobbiamo lavorare con stringhe e convertire all'occorrenza
        if occ_numb >= max_n_occ:    # Ogni numero di frequenza maggiore del precedente lo soppianta
            max_n_occ = occ_numb    
            if int(i) > max_n:        # idem per in numero
                max_n = int(i)    # all occorrenza convertiamo la stringa a int quando c'è da fare comparazione
    return max_n
    
        
#Funzione Centrale dell'esercizio 
def es41(fname1):
    #Lettura della prima riga file di testo 
    with open(fname1, "r",encoding="utf8") as txt:
         row = txt.readline()
    row.strip("\n")     # Pulizia della stringa
    numbers = row.split(",")         #Creazione di una lista di stringhe suddividendo la riga per ciascuna virgola
    int_l = [int(x) for x in numbers]            #Conversione della lista di Stringhe in una lista di interi in grado di processare calcoli
    second_sequence = Find_sequence(int_l)          # Ricavo Della lista di interi richiesta dall'esercizio tramite find_sequence
    second_sequence_str = [str(n) for n in second_sequence]       #Conversione di lista di interi a lista di stringhe per supportare il count di find most occurred
    most_powerful_n = find_Most_Occurred(second_sequence_str)     # Identificazione del numero richiesto dall'esercizio
    return most_powerful_n
    

#print(es41("C:\\Users\\david\\OneDrive\\Documents\\Phython Scripts\\Esercizi Per L'Esame\\Esercizio Pre Esonero 41 (12 11 2024)\\fsequenza1.txt"))


#print(Find_sequence([2, -3, -4,  4, 4, -5, 3, 1,-1]))
#print(find_Most_Occurred(['2', '-1', '-5', '-1', '3', '-2', '1', '2', '1']))

