import numpy  # Importing numpy library
 
array = numpy.array([1, 2, 3, 4, 5]) # Creating a numpy array like a list but static

matrix = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # Creating a 2D numpy array (matrix)

multidimensionalArray = numpy.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]) # Creating a 3D numpy array called a tensor

matrixOnes = numpy.ones((3, 3)) # Creating a 3D numpy array filled with ones

randomMatrix = numpy.random.rand(3, 3) # Creating a 3D numpy array filled with random numbers

matrixproduct = matrix @ randomMatrix # Matrix multiplication

matrixSum = matrix + matrixOnes# Matrix addition
matrixSubtraction = matrix - matrixOnes # Matrix subtraction

print(array)
print("\n")
print(matrix)
print("\n")
print(matrixOnes)
print("\n")
print(matrixproduct)
print("\n")
print(matrixSum)
print("\n")
print(matrixSubtraction)
print("\n")
print(randomMatrix)
print("\n")
print(multidimensionalArray)
print("\n")
print(randomMatrix.flatten())

print("Greatest number in the matrix is: ", matrixproduct.max())
print("Smallest number in the matrix is: ", matrixproduct.min())
print("Sum of all numbers in the matrix is: ", str(matrixproduct.sum()))
print("Matrix Dimension are : " + str(matrixproduct.shape))
