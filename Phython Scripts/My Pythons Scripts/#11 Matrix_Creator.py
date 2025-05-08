
def matrix_creator(number_of_x, number_of_y):
    black_tuple = (255,255,255)
    matrix = []  # This will hold the rows of the matrix
    y = 0
    while y < number_of_y:
        row = []  # This will hold the elements of a row
        x = 0
        while x < number_of_x:
            row.append(black_tuple)  # Add a zero to the row
            x += 1
        matrix.append(row)  # Add the row to the matrix
        y += 1
    return matrix

def Paint_Rectangle(Color, b, h, c_x, c_y, matrix):
    # Iterate over the height of the rectangle
    for y in range(h):
        # Check if the current row is within the matrix
        if c_y + y < len(matrix):
            # Iterate over the width of the rectangle
            for x in range(b):
                # Check if the current column is within the matrix
                if c_x + x < len(matrix[0]):
                    # Set the color of the current pixel
                    matrix[c_y + y][c_x + x] = Color
    return matrix

def Draw_Pixel(matrix,x,y,Color):
    matrix[x][y] = Color
    return matrix

def ruota_sx(img):
    altezza, larghezza = len(img), len(img[0]) # ottengo le dimensioni della matrice
    img2 = matrix_creator(altezza, larghezza) # creo una immagine nera con altezza e larghezza scambiate
    for y, riga in enumerate(img): # per ogni pixel della immagine originale
        for x, pixel in enumerate(riga):
            X = y # calcolo le coordinate X,Y della destinazione
            Y = larghezza - 1 - x
            img2[Y][X] = pixel # e copio il pixel nella destinazione
    return img2

def print_Matrix(matrix) :
    print("\n")
    for row in matrix:
        print(row)
    print("\n")
    return

matrix = matrix_creator(4, 4)
matrix = Paint_Rectangle((23,23,12), 2, 2, 0, 0, matrix)
print_Matrix(matrix)
matrix = ruota_sx(matrix)
print_Matrix(matrix)
matrix = ruota_sx(matrix)
print_Matrix(matrix)