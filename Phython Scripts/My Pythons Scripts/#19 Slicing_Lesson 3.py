# -*- coding: utf-8 -*-
"""
Bevenuto al ripasso sullo slicing avvia il codice per incominciare

Autore:Davide
"""
print("Ripasso sulla  Stringa, lo slicing e le sue proprietà")
Testo_di_Esempio="Nel mezzo del cammin di nostra vita mi ritrovai per una selva oscura,che la diritta via era smarrita."
Contatore=0
print("\nAnalizziamo un pezzo del primo canto della Divina commedia di Dante e svolgiamoci varie operazioni :\n")
print("Ogni carattere dela stringa ha un numero a partire da 0\n")
for char in Testo_di_Esempio:
    print(str(Contatore)+" " + char)
    Contatore += 1
print("\n-Ok, ora esaminiamo degli esempi di selezionamento con il metodo _variabile[selezione del carattere che vuoi selezionare]_")
print("\n-Ad Esempio Testo_di_Esempio[3] dÃ  in output : "+Testo_di_Esempio[7])
print("\n-Ok, ecco ora facciamo un altra selezione usiamo il metodo _variaile[daquestocarattere:aquestocarattere]_")
print("\n-Ad esempio Testo_di_Esempio[3:9] dÃ  in output- : "+Testo_di_Esempio[3:9])
print("\n-Con len(variabile) misuriamo quanti caratteri ci sono nella stringa Testo_di_Esempio in questo caso : "+str(len(Testo_di_Esempio)))
print("\n-Con questo metodo di slicing [8:] selezioniamo i caratteri di seguno l'ottavo compreso ----"+ Testo_di_Esempio[8:])
print("\n-Con questo altro metodo di slicing var[6:] selezioniamo i caratteri prima dell' sesto compreso -----"+ Testo_di_Esempio[6:])
print("\n-Qui gli indici possono essere negativi il meno inverte la sequenza di lettura con questo metodo selezioniamo il terzultimo carattere var[-3] così--->>" + Testo_di_Esempio[-3])
print("\n-Con questo altro metodo variable[::3] prendiamo un carattere ogni 3(questa cosa si piò fare al contrario aggiungendo un indice negativo) come nell'esempio che segue che prende i numeri in avanti un meno li farebbe prendere all'indietro : "+ Testo_di_Esempio[::3])
print(""" 
      
      Se dobbiamo scrivere testi che contengono 
      accapi ('\\n') possiamo usare il triplo apice ''' 
      oppure il triplo doppio apice \"""
      come osserviamo in questa frase
      
      Possiamo anche costruire facilmente dei testi che contengono valori calcolati (ad es. presi da variabili)
      precedendo la stringa con la lettera f (che sta per 'formatted')
      inserendo i valori da interpolare tra parentesi graffe {var}
      """)
print("Per capire dove un oggetto è in memoria si usa la funzione id ad esempio vediamo dove si trova la nostra variabile Testo_di_Esempio : "+ str(id(Testo_di_Esempio)))
print("\nOk fine lezione!!")