import images

"""
Funzione per creare una matrice usando la funzione di images fornita dal docente
"""
def matrix_gen(input_file):
    Matrix = images.load(input_file)
    return Matrix

"""
Funzione che verifica il contenuto di una matrice avendo in imput una matrice
Essa ricava un colore di sfondo e verifica se tutti i pixel sono uguali a quel
colore di sfondo se almeno uno non è uguale al colore di sfondo immediatamente returna false
e blocca l'esecuzione risparmiando risorse
"""
def empty_detect(Matrix):
    background_col = Matrix[0][0]
    for row in Matrix:
        for pix in row:
            if pix != background_col:
                return False
    return True

"""
Funzione Che ricava un rettangolo di pixel avendo in imput le coordinate di inizio e di fine del rettangolo e 
la matrice di partenza 
"""
def Rect_Creator(rect, start_x, start_y, end_x, end_y):
    rectangle = [row[start_x:end_x+1] for row in rect[start_y:end_y+1]]
    return rectangle

"""
Funzione centrale ricorsiva inizia verificando se il caso base rettangolo vuoto si è verificato
Poi cerca l'intersezione tra due linee diverse dallo sfondo di colore uniforme, ricava il pixel centrale di intersezione e le matrici dei rettangoli
creati dai pixels adiacenti al pix centrale e dai pixels agli angoli del rettangolo su queste matrici viene rieseguito la funzione fino a quando non si raggiungerà il caso base matrix vuota
la funzione ogni volta che trova un intersezione aggiunge la tupla che rappresenta il colore di quell'intersezione al risultato, lo scopo dell'esercizio è appunto tenere traccia di queste intersezioni
e la loro gerarchia l'ordinamento delle chiamate dei rettangoli è cruciale fà si che l'ordine custom dell'esercizio sia rispettato e che il risultato sia 
riportato in ordine
"""
def CreateColors(Matrix,result):
    #res=[len(result)]
    #filepath = str(res)+".png"
    #images.save(Matrix, filepath)
    #flag di stop dei cicli
    end = False
    #Empty_Detect ci dice se 
    empty_swich = empty_detect(Matrix)
    #Caso base significa che abbiamo concluso la scansione di questo ramo di problema 
    if empty_swich == True:
        return
    
    #Ricerca intersezione
    if empty_swich == False:
        for index , row in enumerate(Matrix):
            if end == True :
                break
            if all(pix == row[0] for pix in row):
               Mast_Pix_Y = index
               Master_Col = row[0]
               for x, current_pix in enumerate(row):
                   if end == True:
                       break
                   if Matrix[Mast_Pix_Y-1][x] == Master_Col and Matrix[Mast_Pix_Y+1][x] == Master_Col:
                       Mast_Pix_X = x
                       result.append(Master_Col)
                       end = True
                       break
    
    Total_Colums_number = len(Matrix)-1  #this is the y number of columns this indicates y coordinates
    Total_rows_lenght = len(Matrix[0])-1 #This is the x numer of rows this indicates x coordinates
    
    #Creazioni coordinate pixels dei rettangoli
    sx1,sy1 = 0,0
    ex1,ey1 = Mast_Pix_X-1,Mast_Pix_Y-1
    
    sx2,sy2 = Mast_Pix_X+1, 0
    ex2,ey2 = Total_rows_lenght, Mast_Pix_Y-1
    
    sx3,sy3 = 0, Mast_Pix_Y+1
    ex3,ey3 = Mast_Pix_X-1,Total_Colums_number
    
    sx4,sy4 = Mast_Pix_X+1,Mast_Pix_Y+1
    ex4,ey4 = Total_rows_lenght , Total_Colums_number
    
    #Creazione delle matrici tramite le coordinate dei pixels di inizio e di arrivo di ciascun rettangolo
    Rec4 = Rect_Creator(Matrix,sx4,sy4,ex4,ey4)
    Rec3 = Rect_Creator(Matrix,sx3,sy3,ex3,ey3)
    Rec2 = Rect_Creator(Matrix,sx2,sy2,ex2,ey2)
    Rec1 = Rect_Creator(Matrix,sx1,sy1,ex1,ey1)

    #Esecuzione ricorsiva del codice sulle nuove matrici appena create
    Secondary_Rec_4 = CreateColors(Rec4, result)
    Secondary_Rec_3 = CreateColors(Rec3, result)
    Secondary_Rec_2 = CreateColors(Rec2, result)
    Secondary_Rec_1 = CreateColors(Rec1, result)
    return result

"""
Funzione per contare i rettangoli utilizza un metodo arguto che considera la casistica di ogni pixel nella matrice 
un pixel viene contato come rettangolo se ha il pixel sopra e il pixel a sinistra sono di un colore diverso dal colore di sfondo
e il pixel in questione è uguale al colore di sfondo, la casistica prevede eccezzioni per i pixel di bordo matrice che
vengano contati i rettangoli solo se il pixel sopra loro è di un colore diverso dallo sfondo(per quelli y 0)
mentre per quelli x = 0 vengono verificati solo i pixel a sinistra con lo steso metodo e concetto di fondo

"""
def rect_counter(Matrix):
    rect_numb = 1
    Total_Rows_number = len(Matrix)-1
    Total_rows_lenght = len(Matrix[0])-1
    background_color = Matrix[0][0]
    for y in range(Total_Rows_number):
        for x in range(Total_rows_lenght):
            # 0 0 non va verificato tanto non c'è mai un pixel per rettangoli li
            if x == 0 and y != 0:
                if Matrix[y-1][x] != background_color:
                    rect_numb += 1
            if y == 0 and x != 0:
                if Matrix[y][x] != background_color:
                    rect_numb += 1
            if y != 0 and x != 0 and Matrix[y-1][x] != background_color and Matrix[y][x-1] != background_color and Matrix[y][x] == background_color:
                rect_numb += 1              
    return rect_numb

"""
Funzione di avvio del programma si occupa di eseguire i vari compiti del programma e restituire i risultati
"""
def ex1(input_file,  output_file):
    result = []
    file_out_path = str(output_file)    
    Matrix = matrix_gen(input_file)
    result.append(Matrix[0][0])
    rect_numb = rect_counter(Matrix)
    empty_swich = empty_detect(Matrix)
    if empty_swich == False:
        result = [CreateColors(Matrix,result)]
    images.save(result, file_out_path)
    return rect_numb