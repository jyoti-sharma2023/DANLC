import numpy as np 

def matrix_multiply(A, B):
   
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])
    
    # Check if multiplication is possible
    if cols_A != rows_B:
        raise ValueError("Number of columns in A must be equal to number of rows in B.")
    
    # Initialize the result matrix with zeros
    result = [[0] * cols_B for _ in range(rows_A)]
    
    # Perform matrix multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            sum = 0
            for k in range(cols_A):
                sum += A[i][k] * B[k][j]
            result[i][j] = sum
    
    return result
A=[[1,2],[5,3]]
B=[[2,3],[4,2]]
result = matrix_multiply(A, B)
for row in result:
    print(row)