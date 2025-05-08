

'''
    Definite la funzione es63(fileParole,fileTerne) che prende in input:
    - il path FileParole ad un file di testo contenente parole, una parola per ogni riga,
    - il path fileTerne di un file di testo da creare.
    La funzione legge le parole presenti nel file di FileParole e crea
    un nuovo file di testo che salva all'indirizzo fileTerne e restituisce infine il
    numero totale di caratteri presenti nelle parole del file FileParole (ignorando spazi e accapi).
    Il file creato ha lo stesso numero di righe del file letto (una per ogni parola)
    ma le parole in ciascuna riga sono sostituite da terne di interi. Piu' precisamente in
    corrispondenza della generica parola s viene prodotta la stringa con la tupla
    (a,b,c) seguita da accapo,
    dove a e' la lunghezza della parola s, b e' il numero di vocali presenti nella
    parola s e c e' il numero di lettere maiuscole presenti nella parola s.

    Ad esempio se il file delle parole contiene le due parole 'PytHon' e 'fonDAMenti'
    la funzione deve creare e salvare in fileTerne un  file di due righe con le due
    terne (6,1,2) e (10,4,3) e restituire poi l'intero 16.
    '''
    # inserite qui il vostro codice
    
# Funzione che conta le vocali
def FindWowels(string):
    count_vocali = 0
    vocali = {'a', 'e', 'i', 'o', 'u'}
    for i in range(len(string)): # loop per iterare nella stringa
        if string[i].lower() in vocali:
            count_vocali += 1
    return count_vocali

#funzione che conta i caratteri maiuscoli
def Howmany_upper(string):
    count_upp = 0 #counter 
    for i in range(len(string)): # loop per iterare nella stringa
        if string[i].isupper():
            count_upp += 1
    return count_upp
    
#Funzione principale 
def es63(fileParole, fileTerne):
    out_lines = []
    n_char = 0
    
    #lettura file
    with open(fileParole, "r", encoding="utf8") as file:
        lines = file.readlines()# archiviazione dati file in una lista
    
    #elaborazione dati
    for line in lines: # Loop per elaborare ciascuna riga
        line = line.strip("\n").strip(" ") #puliamo la riga
        lenght, vow_n, upper_n = len(line), FindWowels(line), Howmany_upper(line)# otteniamo dati dalle funz. 
        new_tuple = (lenght, vow_n, upper_n)#archiviamo in tupla
        new_str = str(new_tuple)+"\n" #convertiamo in stringa e aggiungiamo il newline
        out_lines.append(new_str)
        n_char += lenght # contiamo le lettere e aggiungiamole al risultato globale
    
    #scrittura file
    with open(fileTerne, "w", encoding="utf8") as file1:
        file1.writelines(out_lines) # writelines é l'opposto di readlines scrive una lista di stringhe ma non mette il newline che va aggiunto a parte
    
    return n_char


