# -*- coding: utf-8 -*-
from pngmatrix import load_png8

def ex(file_png, file_txt, file_out):
    Matrix = load_png8(file_png)
    
    def all_rectangles_lister(Matrix): 
        Local_color = None
        black_pixel = (0, 0, 0)
        c0_0_is_activated = True
        start_pixels_list = []
        h_W_list =[]
        colors_list =[]
        results = ""
        
        def H_W_Calcultor(x, y):
            w = 0
            h = 0  
            H_and_W_calc_loop = True
            coord_0_0_checked = False
            reached_The_end = False
            added_x = 0
            added_y = 0
            number_of_rows = len(Matrix)
            number_of_columns = len(Matrix[0])
            while H_and_W_calc_loop == True:
                if Matrix[x][y] == Matrix[x+added_x][y] and reached_The_end == False:
                    added_x += 1
                if x + added_x  == number_of_rows -1:
                    H_and_W_calc_loop = False
                    reached_The_end = True
                    w =  added_x +1
                if Matrix[x][y] != Matrix[x+added_x-1][y] and reached_The_end == False:
                    H_and_W_calc_loop = False
                    w = added_x        
            h_W_list.append(w)
            return w
                
                    
                
        
        for x in range(len(Matrix)):
            for y in range(len(Matrix[x])):
                if Matrix[x][y] != black_pixel: 
                    #Questo if gestisce il pixel 0 0 e si attiva una sola volta per ogni matrice
                    if x == 0 and y == 0 and c0_0_is_activated == True :
                        start_pixels_list.append(x)
                        start_pixels_list.append(y)
                        H_W_Calcultor(x, y)
                        Local_color = Matrix[x][y]
                        colors_list.append(Local_color)                   
                        
                    if x == 0 and c0_0_is_activated == False:
                        if Matrix[x][y] != Matrix[x][y-1]:
                             #avvia nuovo quadrato
                             start_pixels_list.append(x)
                             start_pixels_list.append(y)
                             Local_color = Matrix[x][y]
                             colors_list.append(Local_color)
                             H_W_Calcultor(x, y)
                             
                        if Matrix[x][y] == Matrix[x][y-1]:
                            pass
                             
                             
                    if y == 0 and c0_0_is_activated == False:#verifica pix sopra
                        if Matrix[x][y] != Matrix[x-1][y]:
                             #avvia nuovo quadrato
                             start_pixels_list.append(x)
                             start_pixels_list.append(y)
                             Local_color = Matrix[x][y]
                             colors_list.append(Local_color)
                             H_W_Calcultor(x, y)
                             

                        if Matrix[x][y] == Matrix[x-1][y]:
                            pass
                             
                    if x != 0 and y != 0:       
                        if Matrix[x][y] == Matrix[x-1][y] or Matrix[x][y] == Matrix[x][y-1] and c0_0_is_activated == False:
                            pass
                            
                        if Matrix[x][y] != Matrix[x-1][y] and Matrix[x][y] != Matrix[x][y-1] and c0_0_is_activated == False:
                            start_pixels_list.append(x)
                            start_pixels_list.append(y)
                            Local_color = Matrix[x][y]
                            colors_list.append(Local_color)
                            H_W_Calcultor(x, y)
                    c0_0_is_activated = False
                    
        
        print(start_pixels_list)
        print(colors_list)
        print(h_W_list)
        
        
    print(all_rectangles_lister(Matrix))
    
ex("image1.png", 677, 778)
