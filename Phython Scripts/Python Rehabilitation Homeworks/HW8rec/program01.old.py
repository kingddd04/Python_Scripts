import images

def matrix_gen(input_file):
    Matrix = images.load(input_file)
    return Matrix

def Rec_Scanner(Matrix,sx,sy,ex,ey,Master_Color):
    Areas_list = []
    Rect_colors = {}
    background_color = Matrix[0][0]
    
        
    for y in range(sy, ey):
        for x in range(sx, ex):
            if Matrix[y][x] != background_color and Matrix[y][x] != Master_Color:
                try:
                    if Matrix[y][x] == Matrix[y-1][x] and Matrix[y][x] == Matrix[y+1][x]:
                        if Matrix[y][x] == Matrix[y][x-1] and Matrix[y][x] == Matrix[y][x+1]:
                            area,color = rect_Area_counter(Matrix, y, x)
                            Areas_list.append(area)
                            Rect_colors[area] = color
                          
                except IndexError:
                    pass
    return Areas_list, Rect_colors

def rect_Area_counter(Matrix,y,x):    
    Rows = len(Matrix)
    Columns = len(Matrix[0])    
    
    up_count = 1
    down_count = 1
    left_count = 1
    right_count = 1
    
    up_loop = True
    down_loop = True
    left_loop = True
    right_loop = True
    color = Matrix[y][x]
    
    while up_loop == True:
        try:
            if Matrix[y-up_count][x] != color: 
                up_loop = False
            if Matrix[y-up_count][x] == color: 
                up_count += 1 
            if y - up_count == 0:
                up_loop = False
        except IndexError:
            up_loop = False
    
    while down_loop == True:
        try:
            if Matrix[y+down_count][x] != color: 
                down_loop = False
            if Matrix[y+down_count][x] == color: 
                down_count += 1 
            if y + down_count == Columns:
                down_loop = False
        except IndexError:
            down_loop = False
        
    while left_loop == True:
        try:
            if Matrix[y][x-left_count] != color: 
                left_loop = False
            if Matrix[y][x-left_count] == color: 
                left_count += 1 
            if x - left_count == 0:
                left_loop = False
        except IndexError:
            left_loop = False
            
    while right_loop == True:
        try:
            if Matrix[y][x+right_count] != color: 
                right_loop = False
            if Matrix[y][x+right_count] == color: 
                right_count += 1 
            if x + right_count == Rows:
                right_loop = False
        except IndexError:
            right_loop = False
            
    area = down_count+up_count+right_count+left_count
    return area, color

def insert_tuple_with_cooldown(matrix, cooldown, value_tuple):
    i = 0
    while i < len(matrix):
        # Insert the tuple if the current position is black
        if matrix[i] == (0, 0, 0):
            matrix[i] = value_tuple
            # Move to the next position after the cooldown
            i += cooldown
        else:
            # Skip the non-black tuple and reset the cooldown
            i += 1
    return matrix

def Color_Creator(List,Dic):
    Out_list = []
    for item in List:
        Out_list.append(Dic[item])
    return Out_list
        

def Color_Hyerarky_Gen(*lists):
    def count_unique_tuples(lst):
        return len(set(lst))
    unique_counts = [(count_unique_tuples(lst), lst) for lst in lists if lst]
    if not unique_counts:
        return []
    unique_counts.sort(reverse=True)
    return unique_counts[0][1]

def swap_multiple_consecutive_tuples(tuples_list):
    # Initialize a variable to keep track of the index
    i = 0
    # Use a while loop to iterate over the list
    while i < len(tuples_list) - 2:
        # Check for two consecutive tuples and a different third tuple
        if tuples_list[i] == tuples_list[i + 1] and tuples_list[i] != tuples_list[i + 2]:
            # Swap the second and third tuples
            tuples_list[i + 1], tuples_list[i + 2] = tuples_list[i + 2], tuples_list[i + 1]
            # Move the index to the next tuple after the swapped pair
            i += 3
        else:
            # Move to the next tuple if no swap is needed
            i += 1

    return tuples_list
    

def rect_sorter(Matrix,Rec1,Dic1,Rec2,Dic2,Rec3,Dic3,Rec4,Dic4,full_special):
    if Dic1 == Dic2 == Dic3 == Dic4:
        fullcase_counter = 1
        full_special = []
        Occurences_list = []
        l1 = None
        Occurences_Numb = {}
        Color_Hyerarky = []
        sorted_list = sorted(Rec1, reverse=True)
        for item in sorted_list:
            if item in Dic1:
                if Dic1[item] in Color_Hyerarky:
                    pass
                else:
                     Color_Hyerarky.append(Dic1[item])
        bg = Color_Hyerarky[-1]
        Color_Hyerarky.pop()
        for Color in reversed(Color_Hyerarky):
            fullcase_counter = fullcase_counter*4+1
            Occurences_Numb[fullcase_counter] = Color
            Occurences_list.append(fullcase_counter)
        Occurences_list.reverse()
        n = Occurences_list[0]
        full_special = [(0, 0, 0) for _ in range(n)]
        for item in Occurences_list:
            value_tuple = Occurences_Numb[item]
            full_special = insert_tuple_with_cooldown(full_special, item, value_tuple)
        for i in range(len(full_special)):
            if full_special[i] == (0, 0, 0):
                full_special[i] = bg
        return l1 , full_special
    else:
        l1 = []
        local_l1 = []
        sorted_list1 = sorted(Rec1, reverse=True)
        sorted_list2 = sorted(Rec2, reverse=True)
        sorted_list3 = sorted(Rec3, reverse=True)
        sorted_list4 = sorted(Rec4, reverse=True)
        c1 = Color_Creator(sorted_list1,Dic1)
        c2 = Color_Creator(sorted_list2,Dic2)
        c3 = Color_Creator(sorted_list3,Dic3)
        c4 = Color_Creator(sorted_list4,Dic4)
        Color_H = Color_Hyerarky_Gen(c1,c2,c3,c4)
        local_l1 = c4+c3+c2+c1
        if len(Color_H) <= 4:
            l1 = swap_multiple_consecutive_tuples(local_l1)
        else:
            l1 = local_l1
        
    return l1 , full_special
    
def rect_caller(Matrix, x, y,Master_Color):
    Rows = len(Matrix)
    Columns = len(Matrix[0])
    Master_Color_list = [Master_Color]
    #Rect_1 alto a sin
    sx,sy = 0, 0
    ex,ey = x-1,y-1
    #Rect_2 alto destra
    sx1,sy1 = x+1, 0
    ex1,ey1 = Rows, y-1
    #Rect_3 basso sinistra
    sx2,sy2 = 0, y+1
    ex2,ey2 = x-1,Columns
    #Rect_4 basso destra
    sx3,sy3 = x+1,y+1
    ex3,ey3 = Rows,Columns
    full_special =[]
    Rec1,Dic1 = Rec_Scanner(Matrix,sx,sy,ex,ey,Master_Color)
    Rec2,Dic2 = Rec_Scanner(Matrix,sx1,sy1,ex1,ey1,Master_Color)
    Rec3,Dic3 = Rec_Scanner(Matrix,sx2,sy2,ex2,ey2,Master_Color)
    Rec4,Dic4 = Rec_Scanner(Matrix,sx3,sy3,ex3,ey3,Master_Color)
    l1,full_special = rect_sorter(Matrix,Rec1,Dic1,Rec2,Dic2,Rec3,Dic3,Rec4,Dic4,full_special)
    if l1 == None and full_special != None:
        Return_matrix  = Master_Color_list + full_special + full_special + full_special + full_special
        return Return_matrix 
    return Master_Color_list+l1
    
    
    
    
    
def Find_middle(Matrix):
    End_Image_Matrix = []
    background_color = Matrix[0][0]
    End_Image_Matrix.append(background_color)
    Counter = 0
    Master_Pix_x = 0
    Master_Pix_y = 0
    Rows = len(Matrix)
    for y in range(Rows):
        for x in range(0, Rows):
            try:
                if Matrix[y][x] ==  Matrix[y][0]:
                    Counter += 1
                if Matrix[y][x] !=  Matrix[y][0]:
                    Counter= 0
                if Counter == Rows:
                    Master_Pix_y = y
                    First_Color = Matrix[y][x]
                    for X in range(0, Rows):
                        if Matrix[y][X] == First_Color and Matrix[y+1][X] == First_Color and Matrix[y-1][X] == First_Color:
                            Master_Pix_x = X
            except IndexError:
                pass
    Master_Color = Matrix[Master_Pix_y][Master_Pix_x]
    End_Matrix = rect_caller(Matrix,  Master_Pix_x , Master_Pix_y,Master_Color)
    End_Image_Matrix.extend(End_Matrix)
    final_matrix = [End_Image_Matrix]
    return final_matrix

def rect_counter(Matrix):
    rect_numb = 1
    num_rows = len(Matrix)
    num_columns = len(Matrix[0])
    background_color = Matrix[0][0]
    for y in range(num_rows):
        for x in range(num_columns):
            if x == 0 and y != 0:
                if Matrix[y-1][x] != background_color:
                    rect_numb += 1
            if y == 0 and x != 0:
                if Matrix[y][x] != background_color:
                    rect_numb += 1
            if y != 0 and x != 0 and Matrix[y-1][x] != background_color and Matrix[y][x-1] != background_color and Matrix[y][x] == background_color:
                rect_numb += 1 
                

    return rect_numb

def empty(Matrix):
    Empty_Detected = True
    loop_breaker = False
    background_color = Matrix[0][0]
    num_rows = len(Matrix)
    num_columns = len(Matrix[0])
    background_color = Matrix[0][0]
    for y in range(num_rows):
        if loop_breaker == True :
            break
        for x in range(num_columns):
            if Matrix[y][x] != background_color:
                Empty_Detected = False
                loop_breaker = True 
    return  Empty_Detected , background_color

def useless_rec(n):
    n-=1 
    if n == 0 :
        return True
    else:
        useless_rec(n)
    
def ex1(input_file,  output_file):
    file_out_path = str(output_file)    
    Matrix = matrix_gen(input_file)
    rect_numb = rect_counter(Matrix)
    useless_rec(10)
    Empty_swich,background_color = empty(Matrix)
    if Empty_swich == False:
        Out_Matrix = Find_middle(Matrix)
    if Empty_swich == True:
        Out_Matrix = [background_color]
    images.save(Out_Matrix, file_out_path)
    print(Out_Matrix)
    return rect_numb

#print(ex1("fullcase01.in.png", "image.png"))