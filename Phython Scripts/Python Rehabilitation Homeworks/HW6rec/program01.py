# -*- coding: utf-8 -*-
from pngmatrix import load_png8

"""
Questa funzione è quella chiamata dall'esercizio
"""
def ex(file_png, file_txt, file_out):
    Raw_Output = []
    
    def matrix_creator(file_png):
        Matrix = load_png8(file_png)
        return Matrix
   
    matrix = matrix_creator(file_png)


    def Find_Rectngles(matrix):
        rectangles = []
    
        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                Current_Color = matrix[row][column]
                if Current_Color != (0, 0, 0):
                    start_row, start_column, end_row, end_column = Find_Measures(matrix, row, column, Current_Color)
                    altezza = end_row - start_row + 1
                    larghezza = end_column - start_column + 1
    
                    rectangles.append({
                        'colore': Current_Color,
                        'inizio': (start_column, start_row),
                        'altezza': altezza,
                        'larghezza': larghezza                     
                    })
                    for i in range(start_row, end_row + 1):
                        for j in range(start_column, end_column + 1):
                            matrix[i][j] = (0, 0, 0)
    
        return rectangles
    
    def Find_Measures(matrix, row, column, Current_Color):
        start_row, start_column, end_row, end_column = row, column, row, column
        while end_row < len(matrix) and matrix[end_row][column] == Current_Color:
            end_row += 1
    
        while end_column < len(matrix[0]) and matrix[row][end_column] == Current_Color:
            end_column += 1
    
        return start_row, start_column, end_row - 1, end_column - 1
    
    Found_Rect = Find_Rectngles(matrix)
    
    for obj in Found_Rect:
        colore = obj['colore']
        inizio = obj['inizio']
        altezza = obj['altezza']
        larghezza = obj['larghezza']
        row = str(inizio)+","+str(larghezza)+","+str(altezza)+","+str(colore)
        result = row.replace("(", "").replace(")", "").replace(" ", "")
        Raw_Output.append(result)
    Output = sorted(Raw_Output, key=lambda s: (-int(s.split(',')[1]), int(s.split(',')[0])))
    with open(file_out, 'w') as file:
        for item in Output:
            file.write(item+"\n")
    
    
    matrix = matrix_creator(file_png)
    
    def Landing_Algoritm(file_txt,matrix):
        def check_black_rect(matrix,w,h,d):
            def rect_scanner3000(S_X, S_Y, E_X , E_Y, matrix):
                Scan_Rec_Result = True                
                black = (0,0,0)   
                for y in range(S_Y, E_Y+1):
                    if Scan_Rec_Result == False:
                        break
                    for x in range(S_X, E_X+1):
                        try:
                            if matrix[y][x] != black:
                                Scan_Rec_Result = False
                        except IndexError:
                            Scan_Rec_Result = False
                return Scan_Rec_Result
       
            black = (0,0,0)
            Good_Pix = False
            check_rect_main = False
            check_rec_sud1 = False
            check_rec_nord2 = False
            check_rec_est3 = False
            check_rec_ovest4 = False
            check_full_fig = False
            Stop = False
            
            for x in range(len(matrix)):
                if Stop == True :
                    break
                for y in range(len(matrix[0])):
                    if matrix[x][y] == black:
                        try:
                            Test_pix_left = matrix[x-d][y]
                            Test_pix_right = matrix[x+w-1+d][y]
                            Test_pix_up = matrix[x][y-d]
                            Test_pix_down = matrix[x][y+h-1+d]
                            Good_Pix = True
                            
                        except IndexError:
                            pass
                        
                    if Good_Pix == True:
                        #RETT_PRINCIPALE OK
                        S_X = x
                        S_Y = y
                        E_X = x+w-1
                        E_Y = y+h-1
                        check_rect_main = rect_scanner3000(S_X, S_Y, E_X, E_Y, matrix)
                        if check_rect_main == True:
                            #RETT_BASSO =OK
                            S_X = x
                            S_Y = y+h-1+1
                            E_X = x+w-1
                            E_Y = y+h-1+d
                            check_rec_sud1 = rect_scanner3000(S_X, S_Y, E_X, E_Y, matrix)
                            if check_rec_sud1 == True:
                                #RETT_ALTO OK
                                S_X = x
                                S_Y = y-d
                                E_X = x+w-1
                                E_Y = y-1
                                check_rec_nord2 = rect_scanner3000(S_X, S_Y, E_X, E_Y, matrix)
                                if check_rec_nord2 == True:
                                    #RETT DESTRA ok
                                    S_X = x+w-1+1
                                    S_Y = y
                                    E_X = x+w-1+d
                                    E_Y = y+h-1
                                    check_rec_est3 = rect_scanner3000(S_X, S_Y, E_X, E_Y, matrix)
                                    if check_rec_est3 == True:
                                        S_X = x-d
                                        S_Y = y
                                        E_X = x-1
                                        E_Y = y+h-1
                                        check_rec_ovest4 = rect_scanner3000(S_X, S_Y, E_X, E_Y, matrix)
                                        if check_rec_ovest4 == True:
                                            check_full_fig = True
                                        
                    Good_Pix = False
                    check_rect_main = False
                    check_rec_sud1 = False
                    check_rec_nord2 = False
                    check_rec_est3 = False
                    check_rec_ovest4 = False
                    
            return check_full_fig
                        
                           
        Landing_Test_Results = []
        numb_list = []
        with open(file_txt, 'r')as text:
            numbers = text.read()
        numbers_cleaned = numbers.strip()
        numbers_cleaned1 = numbers_cleaned.replace("  ", " ")
        for number in numbers_cleaned1.split():
          numb = int(number)
          numb_list.append(numb)         
        for i in range(0, len(numb_list), 3):
            j = numb_list[i:i+3]
            w, h, d = j
            #print(w,h,d)
            Landing_Test_Result = check_black_rect(matrix,w,h,d)
            Landing_Test_Results.append(Landing_Test_Result)
        return Landing_Test_Results

    Landing_Test_Results = Landing_Algoritm(file_txt,matrix)
    #print(Landing_Test_Results)
    return Landing_Test_Results

#ex("image7.png", "rectangles7.txt", "outt.txt")

