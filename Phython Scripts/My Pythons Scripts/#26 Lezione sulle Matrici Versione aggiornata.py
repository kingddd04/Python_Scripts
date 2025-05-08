
print("""
      ---Studi Sulla Matrice---
      
Le matrici sono delle strutture dati che contengono dei valori organizzati in righe e colonne,
come delle tabelle. Le matrici si usano per rappresentare diversi tipi di informazioni,
come le equazioni lineari, le trasformazioni geometriche, le statistiche, le immagini, ecc.
Per creare e manipolare le matrici in Python, si può usare una lista di liste, dove ogni 
lista rappresenta una riga della matrice.
La virgola nelle matrici ha la funzione FONDAMENTALE di separare gli indici che indicano la posizione
degli elementi nella matrice.
      
Prendiamo per esempio la seguente matrice immagine:
    
           0            1            2          3          4           5         6
    0[[(255, 0, 0), (255, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
    1[(255, 0, 0), (255, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
    2[(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
    3[(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
    4[(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
    5[(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 255, 0), (0, 255, 0), (0, 0, 0)],
    6[(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 255, 0), (0, 255, 0)],
    7[(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 255, 0), (0, 255, 0), (0, 0, 0)]]
    
    
    
La virgola separa le varie liste indicando le varie righe di pixels dell immagune
la virgola separa anche le varie tuple che rappresentano i pixels, la virgola 
separa anche i valori di RGB dei vari pixels e indica essi che colori hanno

Ora proviamo a visualizzare l'immagine come matrice come ciò che davvero è
ovvero una lista di liste di tuple:   
      
      """)

Matrix = [[(255, 0, 0), (255, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
         [(255, 0, 0), (225, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
         [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
         [(0, 0, 0), (0, 0, 0), (22, 27, 18), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
         [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
         [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 255, 0), (0, 255, 0)],
         [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 255, 0), (0, 255, 0)],
         [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 255, 0), (0, 255, 0)]]

def trova_pixel_non_neri(Matrix):
    coordinate = []
    # Definisco il colore nero come una tupla di tre zeri
    nero = (0, 0, 0)
    # Ottengo il numero di righe e di colonne della matrice
    num_righe = len(Matrix)
    num_colonne = len(Matrix[0])
    # Per ogni riga della matrice
    for y in range(num_righe):
        # Per ogni elemento della riga
        for x in range(num_colonne):
            # Se l'elemento è diverso dal nero
            if Matrix[y][x] != nero:
                # Aggiungo le coordinate alla lista
                coordinate.append((x, y))
    # Restituisco la lista delle coordinate
    return coordinate

def scan_rectangle(x1,y1, x2,y2):
    pix_numb = 0
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            pix_numb += 1
            print(Matrix[x][y])
    print("\nNumero di pixels scansionati : \n")
    return pix_numb


def stampa_matrice(Matrix):
    # Ottengo il numero di righe e di colonne della matrice
    num_righe = len(Matrix)
    num_colonne = len(Matrix[0])
    print("\t\t ",end="")
    for x in range(num_colonne):
        print("{:15}".format(str(x)), end="")
    print("X")
    # Stampo una linea di separazione
    print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    # Per ogni riga della matrice
    for y in range(num_righe):
        # Stampo la coordinata y in verticale, seguita da una barra
        print("\n" + str(y) + "\t| ", end="")
        # Per ogni elemento della riga
        for x in range(num_colonne):
            # Stampo l'elemento, usando la formattazione con una larghezza di 15 caratteri
            print("{:15}".format(str(Matrix[y][x])), end="")
        # Vado a capo
        print()
    # Stampo una linea di separazione e la coordinata Y
    print("\nY\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    print("""
Otteniamo cosi una matrice di sei colonne e sette righe 
len(Matrix) e Len(matrix[0]) ci contano rispettivamente righe e colonne
(come possiamo osservare dal return della funzione riportato qua sotto)
tuttavia dobbiamo tenere a mente che le cordinate massime della
Matrice sono 6 e 5 in quanto in informatica si conta sempre a partire
da 0.
     """)
    return num_colonne, num_righe


print(stampa_matrice(Matrix))
print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("""
-Possiamo ricercare Qualsiasi elemento della matrice a partire 
dalle sue coordinate ad esempio puoi cercare un pixel usando il metodo
Pixel_Utile = Matrice[coordinata y][coordinata x]

In Python, per accedere agli elementi di una matrice, si usa la notazione matrice[i][j],
 dove i è l’indice della riga e j è l’indice della colonna. Quindi, 
se vuoi cercare un pixel usando il metodo Pixel_Utile = Matrice[coordinata x][coordinata y],
 devi invertire la posizione delle coordinate x e y, perché x corrisponde alla colonna e y corrisponde alla riga.

Prova a cercare i pixel tu stesso inserendo solo i numeri delle coordinate
[x][y] scrivi poi ok per uscire dall'esempio     
      """)
print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

Keep_example_running = True
while Keep_example_running == True:
    y = input("-Inserisci coordinate y > ")
    x = input ("-Inserisci coordinate x > ")
        
    print("\nPixel estratto = "+str(Matrix[int(y)][int(x)]))
    print("")
        
    exit_or_continue = input("Scrivi ok se vuoi proseguire, premi invio per riprovare > ")
        
    if "ok" in exit_or_continue:
        Keep_example_running = False

print("""
          
-Quest' immagine ha quasi tutti pixel neri, il nero è rappresentato dalla tupla (0, 0, 0)
Questo codice consente di trovare i pixel non neri nella matrice e registrarne le coordinate
Tramite appunto le coordinate

          """)
black_pixel = (0, 0, 0)
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

print("Pixels non neri nella matrice/immagine:\n")
Pix_Non_Neri = trova_pixel_non_neri(Matrix)
for pix in Pix_Non_Neri:
    print(pix)
  
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
   
  
print("""
-Iterazione Attraverso matrici

L’iterazione in matrici consiste nel percorrere gli elementi di una matrice,
che è una struttura dati che contiene dei valori organizzati in righe e colonne.
In Python, si possono creare e manipolare le matrici usando diverse tecniche,
come le liste di liste, la libreria NumPy, la libreria scipy.sparse, liste di liste di tuple 
per le immagini Per iterare in una matrice, si possono usare dei cicli for annidati, 
che scorrono le righe e le colonne della matrice e accedono agli elementi con la notazione matrice[i][j],
dove i è l’indice della riga e j è l’indice della colonna.

Per iterare bisongna conoscere il numero di rghe e colonne totali quindi si deve fare uso di range e len
      
QUESTO METODO è ECCELLENTE PER ITERARE E SI BASA SU QUANTO GI DETTO:
    
    n_x = len(Matrix)-1
    n_y = len(Matrix[0])-1

    for y in range(n_x):
        for x in range(n_y):
            print(Matrix[y][x])
            
OSSERVIAMOLO ANALIZZARE TUTTI I PIXELS DELLA MATRICE:
""")

n_x = len(Matrix)-1
n_y = len(Matrix[0])-1

for y in range(n_x):
    for x in range(n_y):
        print(Matrix[y][x])
        
print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

print("""
Ok ora proviamo a fare un esercizio più complesso, analizziamo zone della matrice inserendo
Coordinate di inizio scan e di fine scan pix possiamo usare questo metodo di iterazione
per misurare iquadrati nella matrice.

INSERISCI LE COORDINATE DELLA ZONA CHE VUOI SCANSIONARE:
    
    Primo punto :  primo pixel in alto a sinistra della zona da scansionare
    Secondo punto : ultimo pixel in basso a destra della zona da scansionare
    
Verranno restituiti i pixels scansionati.
    
      """)
        
s_x = input("Inserisci la coordinata x del primo punto :")
s_y = input("Inserisci la coordinata y del primo punto :")
e_x = input("Inserisci la coordinata x del secondo punto :")
e_y = input("Inserisci la coordinata y del secondo punto :")

i_s_x = int(s_x)
i_s_y = int(s_y)
i_e_x = int(e_x)
i_e_y = int(e_y)

print("\nPixels Idntificati :\n")
print(scan_rectangle(i_s_x, i_s_y, i_e_x, i_e_y))





            
