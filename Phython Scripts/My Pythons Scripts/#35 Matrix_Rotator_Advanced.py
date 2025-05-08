"""
Matrix_Rotator_Ez
"""
#Matrix Samples

Matrix =    [[(44,44,44),(11,11,11),(0,1,0),(0,1,0),(55,55,55),(66,66,66)],
            [(33,33,33),(22,22,22),(0,1,0),(0,1,0),(99,99,99),(77,77,77)],
            [(0,3,0),(0,3,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)],
            [(0,3,0),(0,3,0),(0,0,0),(0,0,0),(0,2,0),(0,2,0)],
            [(3,3,3),(7,7,7),(0,0,0),(0,0,0),(0,2,0),(0,2,0)],
            [(51,51,51),(122,122,122),(0,0,0),(0,0,0),(0,0,0),(0,0,0)]]

Simple_Matrix = [[(12,12,12),(13,13,13),(14,14,14)],
                [(1,1,1),(34,34,34),(33,33,33)],
                [(46,46,46),(56,56,56),(100,100,100)]]
                  
#This Function creates a matrix of dimensions y_l,x_l
#Trought iteration and Range

def Empty_Matrix_Creator(y_l,x_l):
    black = (0,0,0)
    Matrix_empty = []
    for y in range(y_l):
        row = []
        for x in range(x_l):
            row.append(black)
        Matrix_empty.append(row)
    return(Matrix_empty)

#This function is used to print properly a matrix adding separators
def Print_Matrix(Matrix,operation_type):
    print("--------------------------    "+operation_type)
    for row in Matrix:
        print(row)
    print("--------------------------\n\n")
    return           
        
        
# This function rotates a Matrix to left 90 degrees
def _90_degrees_l_rotator(Matrix):
    
    Y_l = len(Matrix)
    X_l = len(Matrix[0])
    
    Matrix_empty = Empty_Matrix_Creator(Y_l,X_l)
    
    for y in range(Y_l):
        for x in range(X_l):
            X2 = y
            Y2 = X_l-1-x
            Matrix_empty[Y2][X2] = Matrix[y][x]
    Rotated_matrix = Matrix_empty
    Print_Matrix(Rotated_matrix,"Original Matrix rotated 90 degrees to left.")
    return Rotated_matrix
    
    
    
    
#This function rotates a matrix to the right 90 degrees
def _90_degrees_r_rotator(Matrix):
    Y_l = len(Matrix)
    X_l = len(Matrix[0])
    
    Matrix_empty = Empty_Matrix_Creator(Y_l,X_l)
    
    for y in range(Y_l):
        for x in range(X_l):
            X2 = Y_l-1-y
            Y2 = x
            Matrix_empty[Y2][X2] = Matrix[y][x]
    Rotated_matrix = Matrix_empty
    Print_Matrix(Rotated_matrix,"Original Matrix rotated 90 degrees to right.")
    return Rotated_matrix

#This Function Cut a Matrix into smaller rectangles and prints them
#A simple function that may be customized in base of cases in most complex scenarios
def Matrix_Cutter(Matrix, Size):
    Y_l = len(Matrix)
    X_l = len(Matrix[0])

    
    if Y_l % Size == 0 and X_l % Size == 0:
        print("\n-Rectangles :\n")
        for y in range(0,Y_l,Size):
            for x in range(0,X_l,Size):
                for y0 in range(0,Size):
                    Row = []
                    for x0 in range(0,Size):
                        Row.append(Matrix[y+y0][x+x0])
                    print(Row)
                print("----- ----- ---- ----")
        return
    else:
        raise KeyError("Your Matrix Cannot Be Properly Cutted!")
        return

print("Matrix Rotator and Cutter")
#Print_Matrix(Simple_Matrix, "Original Matrix")
#print(Empty_Matrix_Creator(3,4))
#print(_90_degrees_l_rotator(Simple_Matrix))
#_90_degrees_r_rotator(Simple_Matrix)
#Matrix_Cutter(Matrix,2)






    