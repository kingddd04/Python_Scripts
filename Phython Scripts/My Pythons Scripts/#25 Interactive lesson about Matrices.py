print("""
      ---Studi Sulla Matrice---
      
      Le Matrici contengono dati sotto forma di una 
      Lista di liste di tuple si usano per rappresentare anche le 
      immagini.
      
      -LA matrice  è come una tabella in 2d il print non ce ne rende
      l'idea bene usiamo un ciclo che le rappresenti in colonna
      
      -Svolgiamo alcuni esercizi per comprendere meglio il loro funzionamento.
      
      """)

Matrix = [
    [(1, 1, 1), (0, 0, 0), (0, 40, 0), (0, 0, 0)],
    [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
    [(22, 22, 22), (255, 0, 0), (255, 0, 0), (0, 0, 0)],
    [(0, 0, 0), (0, 255, 0), (0, 255, 0), (0, 0, 0)],
    [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
    [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 255)],
]

Matrix = [[(255, 0, 0), (255, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
               [(255, 0, 0), (255, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
               [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
               [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
               [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 255, 0), (0, 255, 0)],
               [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 255, 0), (0, 255, 0)]]

Keep_example_running = True
while Keep_example_running == True:
    x_count = 0
    y_count =0
    Create_first_row_numb = True

    for row in Matrix:
        if Create_first_row_numb == True:
            for item in row:
                print("\t\t"+str(x_count)+"\t",end="")
                x_count +=1
            print("    Y")
            Create_first_row_numb = False
            print("\n______________________________________________________")
        print("\n"+str(y_count)+"\t| "+str(row))
        y_count +=1
    print("\nX\n ________________________________________________________")
    print(len(Matrix))
    print(len(Matrix[0]))
  
    print("""
          NOTA IMPORTANTE : HO RAPPRESENTATO LA COLONNA ORIZZONTALE COME Y
          E LA LINEA VERTICLE COME X PER MOTIVI PURAMENTE DI SEMPLICITA DI
          PROGRAMMAZIONE SICCOME IL FOR LEGGE PRIMA LE RIGHE E POI LE COLONNE
          
          
-Possiamo ricercare Qualsiasi elemento della matrice a partire 
dalle sue coordinate ad esempio puoi cercare un pixel usando il metodo
Pixel_Utile = Matrice[coordinata x][coordinata y]
          
Prova a cercare i pixel tu stesso inserendo solo i numeri delle coordinate
[x][y] scrivi poi ok per uscire dall'esempio
          
          """)
    
    x = input("-Inserisci coordinate x > ")
    y = input ("-Inserisci coordinate y > ")
        
    print("\nPixel estratto = "+str(Matrix[int(x)][int(y)]))
    print("")
        
    exit_or_continue = input("Scrivi ok se vuoi proseguire, premi invio per riprovare > ")
        
    if "ok" in exit_or_continue:
        Keep_example_running = False
            
    print("-----------------------------------------------------------------")
    print("""
          
          -Quest' immagine ha quasi tutti pixel neri, il nero è rappresentato dalla tupla (0, 0, 0)
          Questo codice consente di trovare i pixel non neri nella matrice e registrarne le coordinate
          Tramite appunto le coordinate
          
          for x in range(len(Matrix)):
              for y in range(len(Matrix[x])):
                  if Matrix[x][y] != black_pixel:
                      ---restituisci coordinate
                 
          """)
black_pixel = (0, 0, 0)
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("Pixels non neri nella matrice/immagine:\n")
for x in range(len(Matrix)):
    for y in range(len(Matrix[x])):
        if Matrix[x][y] != black_pixel:
            print("- X "+str(x)+", Y "+str(y)+" --"+"Pixel : "+str(Matrix[x][y]))
            
            
            
