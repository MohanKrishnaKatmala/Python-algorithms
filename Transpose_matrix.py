"""
Transpose matrix is the rows become columns and column becomes rows.
Like interchange of the rows and columns.
That should a matrix of 1*2 makes as the 2*1 as tranpose of the matrix.
Output:
Give the output as transpose a matrix.
"""
def Transpose_matrix(matrix):
    horizontal=len(matrix)
    vertical=len(matrix[0])
    transpose_matrix=[[None for a in range(horizontal)]for a in range(vertical)] # Take the transpose matrix as all none values.
    for row in range(vertical):
        for column in range(horizontal):
            transpose_matrix[row][column]=matrix[column][row]
    return transpose_matrix
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
print("original matrix is this below.")
for row in matrix:
    print(row)
print()
print("Transpose matrix or interchange rows and columns is this below.")
for row in Transpose_matrix(matrix):
    print(row)
