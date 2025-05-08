"""
Lezione Generica e pratica Sulle Classi in python
"""

#Creiamo Una Classe Questa Classe Che 
class Automobile :
    # Creiamo un construttore con __init__, tramite lui assegneremo degli attributi ai nostri oggetti di classe Automobile
    def __init__(self, Marca, Modello, Anno_Di_Produzione, Grado_Usura, Chilometraggio):
        #sélf si riferisce all'istanza della classe e viene utilizzato per accedere ai suoi attributi e metodi. 
        self.Marca = Marca
        self.Modello = Modello
        self.Anno_Di_Produzione = Anno_Di_Produzione
        self.Grado_Usura = Grado_Usura
        self.Chilometraggio = Chilometraggio
        
    # Questo è un metodo che funziona con variabili di istanza non locali. Quelli primitivi
    def Mostra_Informazioni(self):
        print(f"Macchina : {self.Marca} {self.Modello} {self.Anno_Di_Produzione} {self.Grado_Usura} {self.Chilometraggio}")

Lista_Automobili =  []
#Questi sono gli oggetti creati fornendo valori che verrano assegnati all'oggetto dal costruttore
Auto_1 =  Automobile("Citroen","C_5","2001","Usata","200.000") 
Auto_2 = Automobile("Fiat", "500", "1970", "Usata", "400.000")
Auto_3 = Automobile("Peugeot", "308", "2007", "Nuova", "0")
     
#Gli oggetti si possono archiviare in containers
Lista_Automobili.append(Auto_1)
Lista_Automobili.append(Auto_2)

#Invochiamo il metodo sull'oggetto
Auto_1.Mostra_Informazioni()

#Possiamo modificare gli attributi di oggetti e archiviarli in variabili
Auto_3.Marca = "Mercedes"
Marca = Auto_1.Marca
print(Marca)


