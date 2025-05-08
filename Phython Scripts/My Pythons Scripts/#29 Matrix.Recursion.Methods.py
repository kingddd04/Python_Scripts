# -*- coding: utf-8 -*-
"""
Matrix Slicing 
"""

Hyper_Matrix = [[(0,0,0),(0,0,0),(0,0,0),(0,0,0)],
               [(0,0,0),(44,44,44),(44,44,44),(0,0,0)],
               [(0,0,0),(44,44,44),(44,44,44),(0,0,0)],
               [(0,0,0),(0,0,0),(0,0,0),(0,0,0)]]
              
print("\n-Recursion for each row y in the matrix and then for each tuple in the row, basic iteration-\n")
for y in Hyper_Matrix:
    print("\n")
    for x in y:
        print(x, end=" ")
        
print("""
-This ia an avanced method for recurson that uses a recursion with range and two integers that indicates y and the x
 This method is very useful to scan a part of the image because the integers syolize the coords of a pixel so given to each of the range
 commands the coordinates of any rectangle pixels the range will scan that custom area if you cannot understand just play a bit with the code
 
-Matrix[y][x] can access the pixel of matrix when given the pixel coordinates with all the combinations given by range that returns all numbers 
 from the first to the biggest resulting in a required area scan

      """)

Total_Row_Numb = len(Hyper_Matrix)
Total_Columns_Numb = len(Hyper_Matrix[0])
for y in range(Total_Columns_Numb):
    for x in range(Total_Row_Numb):
        print(Hyper_Matrix[y][x])
        