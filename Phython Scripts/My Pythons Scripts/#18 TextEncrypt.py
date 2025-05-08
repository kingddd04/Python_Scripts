"""
Note errori, 
-Quando incontri un key error "(fra virgolette appare la nostra chiave cercata nel dizionario tramite il metodo dizionario[chiave] " 
significa che la chiave che hai ricercato nel dizionario non esiste e  quindi il codice non può proseguire
-La stringa di testo che viene fornita dall'utente copiando il percorso tramite l'apposito comando windows
ha gli "\" nel percorso che vengono interpretati come caratteri di escape e quindi il percorso file(o la stringa in questione) si modifica e non sarà 
più valido per il nostro scopo di indicazione percorso file, ciò puo essere evitato in due modi o aggiungendo un altro "\" per ogni "\" in maniera che 
#Ogni "\" interpreti il successivo come termine letterale valido per il percorso oppure
#possiamo convertire la stringa a stringa cruda (raw) che è come io ho fatto

"""


import os

is_running = True

while is_running == True:
    
    #Definiamo il nostro dizionario di traduzione carattere----->>stringa di lettere
    #Dizionario= chiave : valore
    
    Text_Encryption_Dict= {
        'A': 'Ao', 'B': 'gu3', 'C': 'aoP', 'D': 'i0a', 'E': 'WEoh',
        'F': 'vgv', 'G': 'Tot', 'H': 'on', 'I': 'h b', 'J': 'Sush',
        'K': 'Pos', 'L': 'wk', 'M': 'YB', 'N': 'Mà', 'O': '8hn',
        'P': 'UBs', 'Q': 'sx', 'R': 'NaN', 'S': 'io9', 'T': 'gvvn',
        'U': 'usj', 'V': 'uhnj', 'W': 'hnd', 'X': 'frn', 'Y': 'aq', 'Z': 'yunPO',
        'a': 'yuj', 'b': 'dx', 'c': 'wtrh', 'd': '3qwes', 'e': 'tc',
        'f': 'dfn', 'g': 'b j', 'h': '3hj', 'i': '3ub5', 'j': '3tgv6',
        'k': '3hjb7', 'l': '3adz8', 'm': '3gc9', 'n': '4gv0', 'o': '4uv1',
        'p': '4aar2', 'q': '4i3', 'r': '4yhwje', 's': 'tgu5', 't': '4jiug6',
        'u': 'o01', 'v': 'hu8', 'w': '4QX', 'x': '5R', 'y': '5gkj', 'z': '5bmj',
        '0': 'ghv2', '1': 'n2t4', '2': 'gwi5', '3': 'kjw6', '4': '57',
        '5': 'vgt', '6': 'fctr', '7': 'tfy6', '8': 'Edv0', '9': 'ghgw2',
        '-': 'gtug', '=': '6wf0', '_': 'wu15', '[': 'OI6', ']': 'GUol',
        '{': 'FK', '}': 'gvqe', "'": 'sn l', '?': '34fb', '<': 'QEF8h',
        '>': 'QTEg', ',': 'Q£j', '.': 'tttE', ':': 'uIOR', ';': 'FHJv',
        '!': 'Rfs', '@': 'Qefd', '*': '8hi9', '(': 'WCb1', ')': 'UHKs',
        " ": "Ah 7" 
    }
    
    #Creiamo un Dizionario che inverte chiavi e valori cosicche in seguito possa implementare una decifratura in seguito
    
    Text_Decryption_Dict= dict(zip(Text_Encryption_Dict.values(), Text_Encryption_Dict.keys()))
    
    #Creiamo similmente un secondo dizionario di cifratura per cifrare i caratteri già cifrati sta volta con i numeri
    
    Number_Encryption_Dict = {
        ' ': '72', 'A': '71', 'B': '70', 'C': '69', 'D': '68', 'E': '67',
        'F': '66', 'G': '65', 'H': '64', 'I': '63', 'J': '62',
        'K': '10', 'L': '11', 'M': '12', 'N': '13', 'O': '14',
        'P': '15', 'Q': '16', 'R': '17', 'S': '18', 'T': '19',
        'U': '20', 'V': '21', 'W': '22', 'X': '23', 'Y': '24', 'Z': '25',
        'a': '26', 'b': '27', 'c': '28', 'd': '29', 'e': '30',
        'f': '31', 'g': '32', 'h': '33', 'i': '34', 'j': '35',
        'k': '36', 'l': '37', 'm': '38', 'n': '39', 'o': '40',
        'p': '41', 'q': '42', 'r': '43', 's': '44', 't': '45',
        'u': '46', 'v': '47', 'w': '48', 'x': '49', 'y': '50', 'z': '51',
        '0': '52', '1': '53', '2': '54', '3': '55', '4': '56',
        '5': '57', '6': '58', '7': '59', '8': '60', '9': '61',
    }
    
    #Creiamo un dizionario che inverte chiavi e valori, sarà utile per decifrare i numeri criptati
    
    Number_Decryption_Dict= dict(zip(Number_Encryption_Dict.values(), Number_Encryption_Dict.keys()))
    
    
    #Definiamo una serie di variabili fuori dal programma vero e proprio per comodità
    
    encrypted_password_level1=""
    decrypted_password_level1=""
    encrypted_password_level2=""
    decrypted_password_level2=""
    encrypted_password_level3=""
    decrypted_password_level3=""
    letters=""
    text=""
    folderpath=""
    user_password=""
    numbers=""
    numb=""
    
    #Creiamo la nostra  interfaccia utente con i print e gli imput
    
    print("---Text Encripter---by King ddd\n")
    print("-Encrypt and decrypt your .txt files, use the following commands:")
    print("-------------------------")
    print("-Encrypt, Encrypt an existing .txt file")
    print("-Decrypt, Decrypt an existing .txt file")
    print("-Secondaryencryption, encript a second time an already encripted file with a custom password")
    print("-Secondarydecryption, decrypt an encrypted file using your password numerica")
    print("-------------------------")
    print("-Exit:- Exit from Text Encripter")
    
    #Creiamo un Selettore di comandi, ci consentirà di selezionare delle azioni che vogliamo eseguire
    
    Command_Selector = input("\nOk, what operation do you want to perform?   ")
    
    #Questo if gestisce il comando Encrypt digitato dall'utente
    
    if "Encrypt" in Command_Selector:
        PathSelector = input("\nOk insert the path of the file you want to encrypt---  ")
        if "\"" in PathSelector:
            PathSelector=PathSelector[1:-1]
            filenameselect = PathSelector.split("\\")
            filename = filenameselect[-1]
            print("\nOk "+ PathSelector + " Selected\n")
            print("Ok,"+ filename + " will be encrypted")
            with open(PathSelector, 'r' ) as file:
                readlines = file.readlines()
                for line in readlines:
                    for char in line:
                        if char in Text_Encryption_Dict:
                            encrypted_password_level1= encrypted_password_level1 + Text_Encryption_Dict[char]
                            
    #Trasformiamo la stringa fornita dall'utente in una stringa raw
    
            PathSelector_raw= r"{}".format(PathSelector)
            folderpath=os.path.dirname(PathSelector_raw)
            filenameselect = PathSelector.split("\\")
            filename = filenameselect[-1]
            EncryptedFilePath= folderpath+"\\"+filename[:-4]+".encrypted"+".txt"
            with open( EncryptedFilePath, "w") as file:
                file.write(encrypted_password_level1)
            print("\nOk, your encrypted file was created\n")
            print("")
            
    #Questo if gestisce il comando Decrypt digitato dall'utente
    
    if "Decrypt" in Command_Selector:
        PathSelector = input("\nOk insert the path of the file you want to decrypt--- ") 
        if "\"" in PathSelector:
            PathSelector=PathSelector[1:-1]
            
    #Con la seguente riga convertiamo la seguente stringa a raw, questo significa che i caratteri speciali del percorso
    #Fornito dall'utente nel nostro caso "\" non verrano interpretati in maniera diversa da ciò che in realtà sono
    #Ovvero parte di un percorso file
    
            PathSelector_raw= r"{}".format(PathSelector)
            folderpath=os.path.dirname(PathSelector_raw)
            filenameselect = PathSelector.split("\\")
            filename = filenameselect[-1]
            print("\nOk "+ PathSelector + " Selected\n")
            
            with open(PathSelector, 'r' ) as file :
                readline= file.readlines()
                for char in readline:
                    text = text+char
                for letter in text:
                    if letters in Text_Decryption_Dict.keys():
                        decrypted_password_level1= decrypted_password_level1+ Text_Decryption_Dict[letters]
                        letters=""
                        letters=letters+letter
                    else:
                        letters=letters+letter
            decrypted_password_level1= decrypted_password_level1 + Text_Decryption_Dict[letters]
            DecryptedFilePath= folderpath+"\\"+filename[:-4]+".decrypted"+".txt"
            print("Ok, your decrypted file ("+ DecryptedFilePath+")was created\n")
            with open(DecryptedFilePath, "w") as file:
                file.write(decrypted_password_level1)
            print("")
                
    #Questo if gestisce la cifratura numerica con aggiunta di password
    #Utilizza il dizionario numerico e il suo dizionario autocreato di cifratura
    #Cripta il codice in numeri poi chiede all'utente di creare una password numerica
    #Questa password verrà moltiplicata per la password vera e propria cosicchè
    #Questa sia più nascosta
             
    if "Secondaryencryption" in Command_Selector:
        PathSelector = input("\nOk insert the path of the file you want to encrypt a second time with a custom password---  ")
        PathSelector=PathSelector[1:-1]
        filenameselect = PathSelector.split("\\")
        filename = filenameselect[-1]
        PathSelector_raw= r"{}".format(PathSelector)
        folderpath=os.path.dirname(PathSelector_raw)
        print("\nOk "+ PathSelector + " Selected\n")
        print("Ok,"+ filename + " will be encrypted")
        with open(PathSelector, 'r' ) as file:
            readlines = file.readlines()
            for line in readlines:
                for char in line:
                    encrypted_password_level2 = encrypted_password_level2 + Number_Encryption_Dict[char]
        user_password= input("Create a numerical password (do not lose it because there is no data recovery option)\n---->")
        encrypted_password_level3= int(encrypted_password_level2) * int(user_password)
        print("Your password has been encrypted a secon time for extra security; when you want to decrypt it use (Secondaryencryption)")
        PathSelector_raw= r"{}".format(PathSelector)
        EncryptedFilePath= folderpath+"\\"+filename[:-4]+".encrypted"+".txt"
        with open( EncryptedFilePath, "w") as file:
            file.write(str(encrypted_password_level3))
        print("\nOk, your super-safe encrypted file was created\n")
        print("")
        
        #Questo if gestisce la decifratura numerica con aggiunta di password
        #Utilizza il dizionario numerico e il suo dizionario autocreato di cifratura
        #Cripta il codice in numeri poi chiede all'utente digitale la password numerica
        #Creata in precedenza
        
    if "Secondarydecryption" in Command_Selector:
        PathSelector = input("\nOk insert the path of the file you want to decrypt---  ")
        PathSelector=PathSelector[1:-1]
        PathSelector_raw= r"{}".format(PathSelector)
        folderpath=os.path.dirname(PathSelector_raw)
        filenameselect = PathSelector.split("\\")
        filename = filenameselect[-1]
        with open(PathSelector, 'r' ) as file :
            file_numbers = file.read()
        print("\nOk "+ PathSelector + " Selected\n")
        user_password= input("Insert The Password you created before, if you will enter a wrong one the datas will be not decrypted correctly--->")
        decrypted_password_level3 = int(file_numbers) // int(user_password)
        str_decrypted_password_level3 = str(decrypted_password_level3)
        for numb in str_decrypted_password_level3:
            if numbers in Number_Decryption_Dict.keys():
                decrypted_password_level2= decrypted_password_level2+ Number_Decryption_Dict[numbers]
                numbers=""
                numbers = numbers + numb
            else:
                numbers = numbers + numb
        decrypted_password_level2 =  decrypted_password_level2 + Number_Decryption_Dict[numbers]
        DecryptedFilePath= folderpath+"\\"+filename[:-4]+".decrypted"+".txt"
        print("Ok, your decrypted file ("+ DecryptedFilePath +")was succesfully created")
        print("However you may need to decrypt it again to access to the text\n")
        print("")
              
        with open(DecryptedFilePath, "w") as file:
            file.write(decrypted_password_level2)
        
    if "exit" in Command_Selector:
        Are_you_sure= input("\nDo you really want to exit from the program(y/n)?")
        if "y" in Are_you_sure:
            is_running = False
            print("\nOk, you are exiting from Text Encrypt have a nice day")
        if "n" in Are_you_sure:
            "Ok, you will be redirected to the boot menù"
        print("")
            
