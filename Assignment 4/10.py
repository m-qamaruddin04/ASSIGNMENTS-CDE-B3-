#10. Write a program to multiply two matrices 

# Function to multiply two matrices
def multiply_matrices(A, B):
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    for i in range(len(A)):            # iterate rows of A
        for j in range(len(B[0])):     # iterate columns of B
            for k in range(len(B)):    # iterate rows of B
                result[i][j] += A[i][k] * B[k][j]
    return result


# Example matrices
A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8],
    [9, 10],
    [11, 12]
]

# Multiply A × B
result = multiply_matrices(A, B)

# Display
print("Matrix A:")
for row in A:
    print(row)

print("\nMatrix B:")
for row in B:
    print(row)

print("\nResultant Matrix (A × B):")
for row in result:
    print(row)
