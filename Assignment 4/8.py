#8. Find the sum of each row of matrix of size m x n. For example for the following matrix output will be 
#like this : 
#2	11	7	12
#5	2	9	15
#8	3	10	42
#Sum of row 1 = 32 
#Sum of row 3 = 63

# Function to find sum of each row
def row_sums(matrix):
    for i in range(len(matrix)):
        row_sum = 0
        for j in range(len(matrix[i])):
            row_sum += matrix[i][j]
        print(f"Sum of row {i+1} = {row_sum}")

# Example matrix
matrix = [
    [2, 11, 7, 12],
    [5, 2, 9, 15],
    [8, 3, 10, 42]
]

# Display matrix
print("Matrix:")
for row in matrix:
    print("\t".join(map(str, row)))

# Find row sums
row_sums(matrix)
