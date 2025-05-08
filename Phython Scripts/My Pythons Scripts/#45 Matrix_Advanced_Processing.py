# -*- coding: utf-8 -*-
#  Opus Club
"""
Created on Thu Nov 21 19:32:02 2024

@author: davide

This file contains a series of functions that can be used to manipulate matrices of pixels 
or lists of lists of tuples that represent the colors of the pixels in an image .png
A color is represented by a tuple of three integers that represent the red, green and blue components 
of the cololor of the pix
"""

# This function takes in a matrix and prints it row after row using a simple for loop
def Stampa_Matrice_Easy(Matrice):
    for row in Matrice:
        print(row)
    return
        
# This function takes in a matrix and prints it row after row using a nested for loop
# The first for loop iterates over the rows of the matrix
# The second for loop iterates over the elements of the row
# This method is useful when you need to access the elements of the matrix using coordinates to eventually modify them
def Matrice_Iterator(Matrice):
    for y in range(len(Matrice)):
        for x in range(len(Matrice[0])):
            print("Pixel Analizzato : " + str(Matrice[y][x]))

# This function takes in a Dictionary and prints it row after row using a simple for loop
def Stampa_Dizionario(Diz):
    print("\nLinee Trovate :\n")
    for chiave in Diz:
        print("Colore Linea = " + str(chiave) + " Lunghezza = " + str(Diz[chiave]))
    return

# This function takes in a List of Strings and prints it row after row using a simple for loop
def Stampa_Lista_Stringhe(L_S):
    print("\n Result : \n")
    for stringa in L_S:
        print(stringa)
    print("\n")
    return

# This function takes in a matrix and finds all the unique colors in it and returns them in a set
def Trova_Colori_Nuovi(Matrice): 
    The_Colors = {pix for row in Matrice for pix in row}
    return The_Colors
    
# This function prints a matrix in a very readable way with indexes for both rows and columns
def Stampa_matrice_con_indici(matrice):

    # Trova la lunghezza massima di un elemento per la formattazione
    max_len = max(len(str(item)) for row in matrice for item in row)
    num_rows = len(matrice)
    num_cols = len(matrice[0]) if num_rows > 0 else 0

    # Stampa gli indici delle colonne
    header = "    " + "  ".join(f"{str(i).rjust(max_len)}" for i in range(num_cols))
    print(header)
    print("   " + "-" * (len(header) - 3))

    # Stampa le righe con gli indici delle righe
    for i, row in enumerate(matrice):
        row_str = f"{str(i).rjust(2)} | " + "  ".join(f"{str(item).rjust(max_len)}" for item in row)
        print(row_str)
    
# This function takes in a matrix and the coordinates of the top left and bottom right corners of a rectangle
# And returns the part of the matrix corresponding to the rectangle
# Questa funzione prende in imput una matrice, delle coordinate dei pixels di partenza e di arrivo e restituisce
# la parte di matrice corrispondente ritagliata
def Ritaglia_Matrice(Matrice, sx,sy,ex,ey):
    # Nota Bene il Range esegue dal numero iniziale compreso a quello finale non compreso
    # Quindi se inseriamo da x 0 a x 6 l'ultimo pixel scansiomato sarà x 5 che tuttavia è
    #IL sesto siccome le liste partono da 0 fino alla lunghezza del indicata dal len()
    # Tuttavia il range sara eseguito comunque 6 volte da 0 a 5
    cropped_Matrix = []     
    Number_of_Rows = len(Matrice)
    Number_of_Columns = len(Matrice[0])
    assert sx <= Number_of_Columns and  ex <= Number_of_Columns and sy <= Number_of_Rows and ey <= Number_of_Rows, "Index Out of Range"
    for y in range(sy, ey):
        row = []
        for x in range(sx, ex):
            row.append(Matrice[y][x])
        cropped_Matrix.append(row)    #
    return cropped_Matrix

# This function takes in a matrix and a smaller matrix and the coordinates of the top left corner of the smaller matrix
# And pastes the smaller matrix into the bigger matrix at the specified coordinates
# However the function does not check if the smaller matrix fits into the bigger matrix

# Questa funzione prende in imput una matrice e una matrice più piccola e le coordinate del pixel di partenza
# e incolla la matrice più piccola nella matrice più grande alle coordinate specificate
# Tuttavia la funzione non controlla se la matrice più piccola si adatta nella matrice più grande
def Incolla_Matrice_Rettangolare(Matrice1, Matrice2, coordx,coordy):
    for y in range(len(Matrice2)):
        for x in range(len(Matrice2[0])):
            Matrice1[y + coordy][x + coordx] = Matrice2[y][x]
    return Matrice1

#This function takesin a Matrix an integer that represents the thickness of the lateral border
# an integer that represents the thickness of the top border and a tuple that represents the color of the border
# and returns the matrix with the border applied
def Crea_Bordo(Matrice, Spessore_Bordo_Laterale, Spessore_Bordo_Alto, Colore_Bordo):
    for y in range(len(Matrice)):
        for x in range(len(Matrice[0])):
            if x < Spessore_Bordo_Laterale or  x >= len(Matrice[0]) - Spessore_Bordo_Laterale:
                Matrice[y][x] = Colore_Bordo  
            elif y < Spessore_Bordo_Alto or  y >= len(Matrice) - Spessore_Bordo_Alto:
                Matrice[y][x] = Colore_Bordo        
    return Matrice

#This function takes in a matrix and returns a new matrix with the colors of the pixels converted to grayscale
def Filtro_Grigio(Matrice):
    for y in range(len(Matrice)):
        for x in range(len(Matrice[0])):
            media = round(sum(Matrice[y][x]) / 3)
            Matrice[y][x] = (media,media,media)
    return Matrice

#This function takes in a matrix and returns a new matrix with the colors of the pixels converted to negative
def Filtro_Negativo(Matrice):
    for y in range(len(Matrice)):
        for x in range(len(Matrice[0])):
            pix = Matrice[y][x]
            Matrice[y][x] = (255-pix[0],255-pix[1],255-pix[2])
    return Matrice

#This function takes in a matrix and a float that represents the brightness modifier
# and returns a new matrix with the brightness modified
def Modifica_Luminosità(Matrice, modificatore):
    for y in range(len(Matrice)):
        for x in range(len(Matrice)):
            pix = list(Matrice[y][x])            
            for color_index in range(3):
                pix[color_index] = round(pix[color_index]*modificatore)
                if pix[color_index] > 255 :
                    pix[color_index] = 255
                if pix[color_index] < 0:
                    pix[color_index] = 0
            Matrice[y][x] = tuple(pix)
    return Matrice

#This function takes in a matrix and a float that represents the contrast modifier
# and returns a new matrix with the contrast modified
def Modifica_Contrasto(Matrice, modificatore):
    for y in range(len(Matrice)):
        for x in range(len(Matrice[0])):
            Color_List = list(Matrice[y][x])
            for n in range(3):
                Temp_color_Value = round((Color_List[n]-128)*modificatore+128)
                if Temp_color_Value > 255 :
                    Color_List[n] = 255
                elif Temp_color_Value < 0:
                    Color_List[n] = 0
                else:
                    Color_List[n] = Temp_color_Value
            Matrice[y][x] = tuple(Color_List)         
    return Matrice
                
# This function counts the number and the lenght of horizontal lines of the same color in a matrix
# and returns a list of strings with the color of the line, the row and the lenght of the line
def Conta_Linee_Orizzontali(Matrice):
    Linee = []
    count = 1
    previus_Color = None
    for y in range(len(Matrice)):
        for x in range(len(Matrice[0])-1):
            pix = Matrice[y][x]
            if pix != (0,0,0):
                if pix == previus_Color:
                    count += 1 
                if pix != previus_Color:
                    count = 1 
                previus_Color = pix 
            if pix == (0,0,0):
                count = 1 
                previus_Color = None
            if count > 1 and Matrice[y][x+1] != pix:
                stringa = "Colore: " + str(pix) + " Riga: " +str(y)+ " Lunghezza: "+ str(count)
                Linee.append(stringa)
                previus_Color = None
                count = 1
            if x == len(Matrice[0])-2:
                if  Matrice[y][x+1] == pix and pix != (0,0,0):
                    count+= 1 
                    stringa = "Colore: " + str(pix) + " Riga: " +str(y)+ " Lunghezza: "+ str(count)
                    Linee.append(stringa)
                    previus_Color = None
                    count = 1
            
    return Linee

# This function counts the number and the lenght of vertical lines of the same color in a matrix
# and returns a list of strings with the color of the line, the column and the lenght of the line
def Conta_Linee_Verticali(Matrice):
    Linee = []
    count = 1
    previus_Color = None
    for x in range(len(Matrice[0])):
        for y in range(len(Matrice)-1):
            pix = Matrice[y][x]
            if pix != (0,0,0):
                if pix == previus_Color:
                    count += 1 
                if pix != previus_Color:
                    count = 1 
                previus_Color = pix 
            if pix == (0,0,0):
                count = 1 
                previus_Color = None
            if count > 1 and Matrice[y+1][x] != pix:
                stringa = "Colore: " + str(pix) + " Colonna: " +str(x)+ " Lunghezza: "+ str(count)
                Linee.append(stringa)
                previus_Color = None
                count = 1
            if y == len(Matrice)-2:
                if  Matrice[y+1][x] == pix and pix != (0,0,0):
                    count+= 1 
                    stringa = "Colore: " + str(pix) + " Colonna: " +str(x)+ " Lunghezza: "+ str(count)
                    Linee.append(stringa)
                    previus_Color = None
                    count = 1
    return Linee

# This function takes in a matrix and the coordinates of the top left corner of a rectangle
# and returns a string with the coordinates of the top left corner, the base, the height and the color of the rectangle
def Trova_Base_E_Altezza(Matrice,y,x):
    pix = Matrice[y][x]
    y_swich = True
    counter = 0
    h = 0
    while y_swich == True:
        if Matrice[y+counter][x] == pix:
            counter +=1 
        if y+counter == len(Matrice) or Matrice[y+counter][x] != pix:
            y_swich = False 
            h = counter 
    x_swich = True 
    counter = 0
    b = 0
    while x_swich == True:
        if Matrice[y][x+counter] == pix:
            counter +=1 
        if x+counter == len(Matrice[0]) or Matrice[y][x+counter] != pix:
            x_swich = False 
            b = counter
    Dati_Rettangolo = " Coordinate y : "+str(y)+ " , Coordinate x : "+str(x)+ " , Base : " + str(b) + " , Altezza : " + str(h) + " , Colore : " + str(pix)
    return Dati_Rettangolo
    
# This function takes in a matrix and returns a list of strings with the coordinates of the top left corner, the base, the height and the color of the rectangles found
def Conta_Rettangoli(Matrice):
    black = (0,0,0)
    Rettangoli_Res = []
    for y in range(len(Matrice)-1):
        for x in range(len(Matrice[0])-1):
            pix = Matrice[y][x]
            if x == 0 and y == 0:
                if pix != black:
                    if pix == Matrice[y+1][x] and pix == Matrice[y][x+1]:
                        stringa_result = Trova_Base_E_Altezza(Matrice, y, x)
                        Rettangoli_Res.append(stringa_result)
            elif y != 0 and x == 0:
                if pix != black:
                    if pix == Matrice[y+1][x] and Matrice[y-1][x] != pix :
                        stringa_result = Trova_Base_E_Altezza(Matrice, y, x)
                        Rettangoli_Res.append(stringa_result) 
            elif y == 0 and x != 0:
                if pix != black:
                    if pix == Matrice[y][x+1] and Matrice[y][x-1] != pix :
                        stringa_result = Trova_Base_E_Altezza(Matrice, y, x)
                        Rettangoli_Res.append(stringa_result) 
            
            elif y != 0 and x != 0:
                if pix != black:
                    if pix == Matrice[y+1][x] and pix == Matrice[y][x+1]:
                        if pix != Matrice[y-1][x] and pix != Matrice[y][x-1]:
                            stringa_result = Trova_Base_E_Altezza(Matrice, y, x)
                            Rettangoli_Res.append(stringa_result) 
    return Rettangoli_Res

# This function takes in a matrix and returns a new matrix with the colors of the pixels rotated 90 degrees to the left
def ruota_Matrice_A_Sinistra(Matrice,Matrice_Empty):
    for y in range(len(Matrice)): # per ogni pixel della immagine originale
        for x in range(len(Matrice[0])):
            X = y # calcolo le coordinate X,Y della destinazione
            Y = len(Matrice[0]) - 1 - x
            Matrice_Empty[Y][X] = Matrice[y][x] # e copio il pixel nella destinazione
    return Matrice_Empty

# This function creates  black enpty matrix with the specified number of rows and columns (rows=y,colums = x)
def crea_matrice(num_rows, num_cols):
    return [[(0, 0, 0) for _ in range(num_cols)] for _ in range(num_rows)]

                                  
"""
Variabili Globali per test
"""

#               0        1       2        3       4       5       6

Matrice = [[(1,23,134),(1,23,134),(1,23,134),(0,0,0),(0,0,0),(123,334,213),(123,334,213)],                  #  0
          [(1,23,134),(1,23,134),(0,0,0),(0,0,0),(0,0,0),(123,334,213),(123,334,213)],                      #  1
          [(1,23,134),(0,0,0),(0,0,0),(0,0,0),(33,33,33),(123,334,213),(123,334,213)],                      #  2 
          [(0,0,0),(0,0,0),(0,321,0),(200,200,200),(200,200,200),(200,200,200),(0,141,0)],                  #  3
          [(200,200,200),(200,200,200),(25,60,60),(200,200,200),(200,200,200),(200,200,200),(0,0,0)],       #  4
          [(200,200,200),(200,200,200),(0,0,131),(200,200,200),(200,200,200),(200,200,200),(255,255,255)],  #  5
          [(200,200,200),(200,200,200),(0,0,0),(200,200,200),(200,200,200),(255,255,255),(255,255,255)]]    #  6

#                    0       1      2        3       4       5       6
Matrice_Empty = [[(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)], #0
                [(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)],  #1
                [(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)],  #2
                [(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)],  #3
                [(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)],  #4
                [(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)],  #5
                [(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)]]  #6
                 
Mini_Matrix = [[(100,100,100),(100,100,100),(100,100,100)],
              [(120,120,120),(120,120,120),(120,120,120)],
              [(170,170,170),(170,170,170),(170,170,170)]]

"""
Test di esempio per la funzione incolla matrice rettangolare
"""

#Pasted_Matrix = Incolla_Matrice_Rettangolare(Matrice,Mini_Matrix,1,2)
#Stampa_matrice_con_indici(Mini_Matrix)
#Stampa_matrice_con_indici(Pasted_Matrix)

"""
Test di esempio per la funzione ritaglia_Matrice
"""

#Matrix_Tagliata = Ritaglia_Matrice(Matrice, 2, 2, 4, 4)
#Stampa_matrice_con_indici(Matrice)
#Stampa_matrice_con_indici(Matrix_Tagliata)

"""
Test per accedere ai dati della Matrice
"""

print(len(Matrice))
print(len(Matrice[0]))

"""
Test per La funzione Crea_Bordo
"""

#Matrice_con_Bordo = Crea_Bordo(Matrice, 1, 1, (9,9,9))
#Stampa_matrice_con_indici(Matrice)

"""
Test Debug per Filtro grigio
"""

#Stampa_matrice_con_indici(Matrice)
#Matrice_Grigia = Filtro_Grigio(Matrice)
#Stampa_matrice_con_indici(Matrice_Grigia)

"""
Test Debug Filtro_Negativo
"""

#Stampa_matrice_con_indici(Matrice)
#Matrice_Negativa = Filtro_Negativo(Matrice)
#Stampa_matrice_con_indici(Matrice_Negativa) 

"""
Test Debug Modificatore Luminosita
"""

#Matrice_Luminosita_modificata = Modifica_Luminosità(Matrice, 0.5))
#Stampa_matrice_con_indici(Matrice_Luminosa_O_Buia)

"""
Test Debug Modificatore di contrasto
"""
#Stampa_matrice_con_indici(Matrice)
#Matrice_Contrastata = Modifica_Contrasto(Matrice, 1.2)
#Stampa_matrice_con_indici(Matrice_Contrastata)

"""
Test Debug conta linee 
"""

#Stampa_matrice_con_indici(Matrice)
#Lista_Di_Stringhe_Orizzontali = Conta_Linee_Orizzontali(Matrice)
#Stampa_Lista_Stringhe(Lista_Di_Stringhe)

"""
Test Debug conta linee orizzontali
"""

#Stampa_matrice_con_indici(Matrice)
#Lista_Di_Stringhe_Orizzontali = Conta_Linee_Orizzontali(Matrice)
#Stampa_Lista_Stringhe(Lista_Di_Stringhe_Orizzontali)

"""
Test Debug conta linee verticali
"""

#Stampa_matrice_con_indici(Matrice)
#Lista_Di_Stringhe_Verticali = Conta_Linee_Verticali(Matrice)
#Stampa_Lista_Stringhe(Lista_Di_Stringhe_Verticali)

"""
Test per Debug trova colori
"""
#Stampa_Matrice_Easy(Matrice)
#print("\nColori Diversi Nella Matrice : \n\n" + str(Trova_Colori_Nuovi(Matrice)))

"""
Test Debug trova Rettangoli
"""

#Stampa_matrice_con_indici(Matrice)
#Lista_Di_Stringhe = Conta_Rettangoli(Matrice)
#Stampa_Lista_Stringhe(Lista_Di_Stringhe)

"""
Test Ruota Matrice
"""

#Stampa_matrice_con_indici(Matrice)
#Matrix = ruota_Matrice_A_Sinistra(Matrice, Matrice_Empty)
#Stampa_matrice_con_indici(Matrix)

"""
Test Crea_Matrice
"""

New_Matrix = crea_matrice(3, 4)
Stampa_matrice_con_indici(New_Matrix)

"""
Finito
"""