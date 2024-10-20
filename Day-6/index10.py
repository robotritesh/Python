# 2D array (Matrix)
matrix_2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements
print(matrix_2d[0][0])  # Output: 1 (first row, first column)
print(matrix_2d[1][2])  # Output: 6 (second row, third column)

# Iterating over the 2D array
for row in matrix_2d:
    for elem in row:
        print(elem, end=" ")
    print()
