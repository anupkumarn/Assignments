#*******************************************
# Name: Anup Kumar N
#*******************************************

import numpy as np 

# Create a matrix of shape (3,5) made of random numbers
A = np.matrix(np.random.random(15)).reshape(3,5,order ='C')
print('Matrix of shape (3,5) with random numbers is: ')
print(A)

# Print size and length of matrix A
#print(A.shape)
#print(type(A))
#print(len(A))
print('Size of matrix A is: ', A.size, ' and its length is: ', A.nbytes)

# Resize matrix A to size (3,4)
A = A[:3,:4]
print('The slice of matrix A after resize to (3,4) is: ')
print(A)
#print(A.shape)

# Create matrix B as transpose of matrix A
B = A.T 
print('Transpose of matrix A is: ')
print(B)
#print(type(B))
#print(B.shape)

# Find minimum of values in column 1 of matrix B
print('Minimum value in column 1 of matrix B is: ',B.min(axis=0)[:,0])

# Find minimum and maximum of all values in matrix B
print('For matrix B minimum value is: ', B.min(), ' and maximum value is: ', B.max())

# Find minimum of all values in matrix B
#print(B.max())

# Create a vector array X with 4 random values
X=np.random.random(4)
#print(type(X))
#print(X.shape)
print('Vector with 4 random numbers is: ', X)

# Create definition to multiply an array and matrix by passing them as inputs
def multiply_func(fn_arr, fn_matr):
    fn_ret = np.dot(fn_arr,fn_matr.T) 
    return(fn_ret)

# Call the multiply function using X and A as inputs assigning output to D
D = multiply_func(X,A)
print('Product of vector X and matrix A is: ',D)
#print(type(D))
#print(D.shape)

# Create a complex number with non-zero real and absolute values
Z = np.random.rand(1,2).view(dtype=np.complex128)
print('Complex number generated is: ',Z)

# Show complex number Z' real, imgainary and absolute values
print('Real part is ', Z.real, ', Imaginary part is ', Z.imag, ' and Absolute value is ', abs(Z))

# Multiply D with absolute of Z and assign to C
C = D.T * abs(Z)
print('Product of matrix D with absolute of complex number Z is: ')
print(C)

# Convert and overwrite matrix B to its string format
B=str(B)
print(' String format of matrix B is: ')
print(B)

# Print end of homework !!!!!
print('Anup Kumar is done with HW2')



