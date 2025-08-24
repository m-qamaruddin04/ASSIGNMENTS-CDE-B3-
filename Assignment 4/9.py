#9. Write a program to add two matrices of size n x m.

# Function to add two matrices
def add_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):          # iterate rows
        row = []
        for j in range(len(matrix1[0])):   # iterate columns
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

# Example matrices (3x3)
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Adding matrices
result = add_matrices(matrix1, matrix2)

# Display
print("Matrix 1:")
for row in matrix1:
    print(row)

print("\nMatrix 2:")
for row in matrix2:
    print(row)

print("\nResultant Matrix (Matrix1 + Matrix2):")
for row in result:
    print(row)
