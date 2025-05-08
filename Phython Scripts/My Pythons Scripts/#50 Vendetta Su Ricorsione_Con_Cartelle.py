""" 
11/12/2024 Esercizio Sbagliato Durante un esercitazione e corretto
L'errore stava principalmente in Espl_Cartelle_H1 che non eliminava i tab dal testo
Inoltre il passaggio del dizionario come argomento ricorsivo era confuso
Sono necessari altri test per capire se l'errore era nel passaggio del dizionario
durante la ricorsione o se era un dovuto alla mancanza di eliminazione dei tab
Questo script esplora le cartelle e i file al loro interno in modo ricorsivo 
Verifica che il testo del file inizi e finisca con lo stesso carattere 
Restituisce un dizionario con le cartelle e i file che soddisfano la condizione
"""

import os

# Questa Funzione Verifica che il testo del file inizi e finisca con lo stesso carattere
def Espl_Cartelle_H1(fullpath):
    with open(fullpath,"r", encoding="utf8") as txt:
        content = txt.read()
    content = content.replace("\n", "").replace(" ", "").replace("\t", "")
    if content[0] == content[-1]:
        return True
    else:
        return False
    
    
# Questa Funzione Si occupa di esplorare le cartelle e i file al loro interno
#Utilizza la ricorsione e all'occorenza chiama la funzione Espl_Cartelle_H1 per
#verificare il contenuto dei file
# Per salvare i risultati utilizza un dizionario
# Che viene passato come argomento chiamata dopo chiamata
def Espl_Cartelle_H2(root, Out_Dic):
    for filename in os.listdir(root):
        fullpath = root + "/" + filename
        if fullpath.endswith(".txt"):
            Isvalid = Espl_Cartelle_H1(fullpath)
            if Isvalid == True:
                if root not in Out_Dic:
                    Out_Dic[root] = set()
                Out_Dic[root].add(filename)
    for filename in os.listdir(root):
        fullpath = root + "/" + filename
        if os.path.isdir(fullpath):
            Espl_Cartelle_H2(fullpath,Out_Dic)
    return Out_Dic

# Questa Funzione è la funzione che viene chiamata all'esterno
# Inizializza il dizionario e chiama la funzione ricorsiva
# Restituisce il dizionario con i risultati
def Espl_Cartelle(root):
    Result = Espl_Cartelle_H2(root, {})
    return Result

# Esempio di Utilizzo
print(Espl_Cartelle("C:/Users/david/OneDrive/Documents/Phython Scripts/My Pythons Scripts/Test Material/Os_Recursive"))