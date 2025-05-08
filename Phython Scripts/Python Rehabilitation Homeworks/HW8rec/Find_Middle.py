

Matrix = [

    [(17, 0, 70), (0, 0, 0), (200, 200, 200), (0, 90, 0), (0, 0, 0), (40, 0, 22)],
    [(0, 0, 0), (0, 0, 0), (200, 200, 200), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
    [(0, 0, 0), (0, 0, 33), (200, 200, 200), (0, 0, 0), (0, 0, 0), (0, 1, 0)],
    [(200, 200, 200), (200, 200, 200), (200, 200, 200), (200, 200, 200), (200, 200, 200), (200, 200, 200)],
    [(0, 0, 7), (0, 44, 0), (200, 200, 200), (32, 0, 0), (0, 0, 0), (0, 0, 0)],
    [(0, 0, 0), (0, 0, 0), (200, 200, 200), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
    [(22, 0, 40), (0, 6, 0), (200, 200, 200), (0, 0, 0), (0, 0, 0), (70, 33, 12)]
    
    ]

for index , row in enumerate(Matrix):
    if all(pix == row[0] for pix in row):
        Y = index
        Master_Col = row[0]
        for x, current_pix in enumerate(row):
            print(x)
            if Matrix[Y-1][x] == Master_Col and Matrix[Y+1][x] == Master_Col:
                print(Matrix[Y][x])
                break
        
Total_Colums_number = len(Matrix)-1
Total_rows_lenght = len(Matrix[0])-1

#print(row_lenght,colums_lenght)


Mast_Pix_X = 2
Mast_Pix_Y = 3


sx1,sy1 = 0,0
ex1,ey1 = Mast_Pix_X-1,Mast_Pix_Y-1

sx2,sy2 = Mast_Pix_X+1, 0
ex2,ey2 = Total_rows_lenght, Mast_Pix_Y-1

sx3,sy3 = 0, Mast_Pix_Y+1
ex3,ey3 = Mast_Pix_X-1,Total_Colums_number

sx4,sy4 = Mast_Pix_X+1,Mast_Pix_Y+1
ex4,ey4 = Total_rows_lenght , Total_Colums_number

print(Matrix[sy1][sx1])
print(Matrix[ey1][ex1])
print("")
print(Matrix[sy2][sx2])
print(Matrix[ey2][ex2])
print("")
print(Matrix[sy3][sx3])
print(Matrix[ey3][ex3])
print("")
print(Matrix[sy4][sx4])
print(Matrix[ey4][ex4])




