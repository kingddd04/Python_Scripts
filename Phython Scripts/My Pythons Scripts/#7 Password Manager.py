'''
author: Margherita and Davide
'''
#IN PRIMO LUOGO VIENE CREATA UNA FUNZIONE SETPAS CHE GESTISCE IL COMANDO SETPASSWORD
#VENGONO DICHIARATE LE VARIABILI CORRISPONDENTI ALLE PASSWORD ORA LE VARIABILI SONO VUOTE
def setpas():
    pas = input("\nImposta la tua nuova password ")
    print("\Ottimo password impostata!")
    return pas
pass0='empty'
pass1='empty'
pass2='empty'
pass3="empty"
pass4="empty"
pass5="empty"
pass6="empty"
pass7="empty"
pass8="empty"
pass9="empty"
#VIENE CREATO UN LOOP CHE CONSENTE AL PROGRAMMA DI RESTARE ACCESO, LE VARIABILI SONO FUORI DAL LOOP QUINDI NON SONO VENGONO MODIFICATE
PasswordManager=True
while PasswordManager == True:
    #IL CODICE CREA UN MENU' L'UTENTE TRAMITE I COMANDI POTRA' SCEGLIERE COSA FARE, LE VARIE OPZIONI SONO REOLATE DA IF, E VENGONO SCELTE IN BASE COSA L'UTENTE DIGITA NELL'INPUT, il print Fornisce le informazioni all'utente sull'uso del programma
    textimput= input("\n---PASSWORD MANAGER----\n\nCiao! cosa vuoi fare oggi? Utilizza i comandi supportati.\n\n-Showpasswords, mostra tutte le tue password\n-Setpassword, imposta una password\n-Reset,cancella tutte le tue password\n-Exit, esce dal Password Manager, perderai tutte le tue password\n\n___")
    #"SHOWPASSWORD MOSTRA LE PASS(LE VARIABILI ESTERNE AL LOOP SALVATE E I BLOCCHI DI MEMORIA CHE QUESTE OCCUPANO
    if "showpasswords" in textimput :
        print("Ecco le tue password salvate!")
        print("1- "+pass0)
        print("2- "+pass1)
        print("3- "+pass2)
        print("4- "+pass3)
        print("5- "+pass4)
        print("6- "+pass5)
        print("7- "+pass6)
        print("8- "+pass7)
        print("9- "+pass8)
        print("10- "+pass9)
    #SETPASSWORD CONSENTE ALL'UTENTE DI MODIFICARE UNO SLOT PASSWORD A SCELTA, LA FUNZIONE SETPASS CREA UN IMPUT CHE CONSENTE DI IMPOSTARE UNA PASSWORD
    #SUCCESSIVAMENTE LA PASSWORD VIENE SALVATA NELLE VARIANILI ESTERNE AL LOOP TRAMITE  pass0 = setpas() CHE EGUAGLIA IL VALORE DI SETPASS A QUELLO DI PASS
   #E QUINDI LA SALVA
    elif "setpassword" in textimput:
        setpass= input("\nScegli lo slot password che vuoi sovrascrivere  >> ")
        if "1" in setpass :
            pass0 = setpas()
        elif "2" in setpass :
            pass1 = setpas()
        elif "3" in setpass :
            pass2 = setpas()
        elif "4" in setpass :
            pass3 = setpas()
        elif "5" in setpass :
            pass4 = setpas()
        elif "6" in setpass :
            pass5 = setpas()
        elif "7" in setpass :
            pass6 = setpas()
        elif "8" in setpass :
            pass7 = setpas()
        elif "9" in setpass :
            pass8 = setpas()
        elif "10" in setpass :
            pass9 = setpas()
        else:
            print("\nX- PER FAVORE USA UN COMANDO SUPPORTATO!\n") 
            #RESET CANCELLA TUTTE LE PASSWORD REIMPOSTANDO LE VARIABILI AI VALORI INIZIALI, la CONFERMA DEL RESET E'GESTITA
            #IN MANIERA SIMILE A TUTTE LE ALTRE SELEZIONI DI OPZIONI
    elif "reset" in textimput:
        resetpassword=input("Attenzione tutte le tue password andranno perse(per sempre)! Vuoi continuare(y/n)")
        if "y" in resetpassword :
            print("1- "+pass0)
            print("2- "+pass1)
            print("3- "+pass2)
            print("4- "+pass3)
            print("5- "+pass4)
            print("6- "+pass5)
            print("7- "+pass6)
            print("8- "+pass7)
            print("9- "+pass8)
            print("10- "+pass9)
            print("\nTutte le tue password sono state cancellate")
        if"n" in resetpassword:
            print("\nLe tue password non sono andate perse\n")
        else:
            print("\nX- PER FAVORE USA UN COMANDO SUPPORTATO!\n")
            #EXIT ROMPE IL LOOP DEL PROGRAMMA(MODIFICA LA VARIABILE PASSWORDMANAGER A FALSE ) E IL WHILE NON VIENE
            #ESEGUITO E QUINDI IL CODICE NON VIENE PIU' RIPETUTO SPEGNEDO IL PROGRAMA 
            #LA CONFERMA DELLA CHIUSURA DEL PROGRAMMA E' GESTITA COME LA SELEZIONE DEI PROGRAMMI
    elif "exit" in textimput:
        exitpassman=input("Vuoi uscire dal programma? Perderai tutte le tue password(y/n)")
        if "y" in exitpassman :
            PasswordManager=False
            print("\nSei uscito daL Password Manager\nTutte le tue password sono state cancellate")
        if"n" in exitpassman:
            print("\nOk, stai tornado al menù home\n")
       #VISUALIZZA UN MESSAGGIO DI ERRORE SE SI USA UN COMANDO ERRATO, L'ELSE SI ATTIVA SE NON VIENE USATO NESSUN IF O ELIF  
       #QUINDI SE L'UTENTE FORNISCE COMANDI ERRATI
    else :
        print("\nX- PER FAVORE USA UN COMANDO SUPPORTATO!\n")