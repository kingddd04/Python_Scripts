

import immagini

'''    
                for y in range(Number_of_Rows):
                    for x in range(Number_of_Columns):
                        pixel = Matrix[y][x]
                        if pixel not in Unique_Color_Tuple_L:
                            Unique_Color_Tuple_L.append(pixel)
    Es 12: 4 punti
    Progettare la  funzione es13(fimm,fimm1) che, 
    - riceve gli  indirizzi fimm e  fimm1 di due file .PNG. 
    - legge l'immagine da fimm ne modifica i colori dei pixel e  la salva poi 
      all'indirizzo fimm1.
    - restituisce infine il numero di colori DIFFERENTI presenti nell'immagine modificata.
    
    
      I colori dei pixel dalla nuova immagine si ottengono a partire da quelli 
      dell'immagine originaria con la seguente  procedura:.
      
      le tuple dei DIFFERENTI colori presenti nella prima immagine vengono ordinate in 
      ordine crescente.
      
      La sequenza ordinata di tuple  che si ottiene viene suddivisa a gruppi di 50 (se il 
      numero totale di tuple non e' un multiplo di 50 allora l'ultimo gruppo avra' 
      meno di 50 elementi). 
      
      I colori corrispondenti alle tuple che compaiono come  primo elemento di 
      ciascun gruppo saranno i colori assegnati ai pixel dell'immagine.
      
      tutti i pixel che avevano colori corrispondenti a tuple finite in uno stesso 
      gruppo avranno come colore quello corrispondente alla prima tupla del gruppo.
      
      Ad esempio i pixel che avevano colori corrispondenti alle tuple finite nelle prime 50 posizioni 
      della sequenza ordinata  avranno ora tutti lo stesso colore (dato dal colore corrispondente 
      alla tupla che occupa la prima posizione  della sequenza), i pixel 
      che avevano colori le cui tuple  nella sequenza occupano le posizioni 
      da 50 a 99 avranno tutti lo stesso  colore (corrispondente alla tupla in posizione  
      50) ecc. ecc. 
      Sull'immagine Fig1.png la funzione deve produrre il file RisFig1.png e restituire il numero ?
    Per caricare e salvare i file PNG si possono usare load e save della libreria immagini.
    '''
def find_colors(Matrice):
    insieme = set()
    for row in Matrice:
        for pix in row:
            insieme.add(pix)
    insieme_lista = list(insieme)
    return insieme_lista

def divide_into_sublists(tuple_list): 
    sublists = [] 
    for i in range(0, len(tuple_list), 50): 
        chunk = tuple_list[i:i + 50] 
        sublists.append(chunk) 
        return sublists
    
def es13(fimm,fimm1):
    Matrice = immagini.load(fimm)
    Lista_Tuple_Singole = find_colors(Matrice)
    Lista_Tuple_Singole.sort()
    sublists = divide_into_sublists(Lista_Tuple_Singole)
    for y in range(len(Matrice)):
        for x in range(len(Matrice[0])):
            pix = Matrice[y][x]
            for sottolista in sublists:
                if pix in sottolista:
                    Matrice[y][x] = sottolista[0]
    new_list = find_colors(Matrice)
    lenght_new_list = len(new_list)
    immagini.save(Matrice, fimm1)
    return lenght_new_list
                    
            
    
    
    
    
    


es13("C:\\Users\\david\\OneDrive\\Documents\\Phython Scripts\\Esercizi Per L'Esame\\Esercizio sulle Matrici 16 11 2024\\Foto2.png", "C:\\Users\\david\\OneDrive\\Documents\\Phython Scripts\\Esercizi Per L'Esame\\Esercizio sulle Matrici 16 11 2024\\Duce.png")
                    
    
    
            
        
        
    
            
            