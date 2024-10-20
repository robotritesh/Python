# 3D array (Tensor)
matrix_3d = [
    [  # First matrix
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ],
    [  # Second matrix
        [10, 11, 12],
        [13, 14, 15],
        [16, 17, 18]
    ]
]

# Accessing elements
print(matrix_3d[0][1][2])  # Output: 6 (first matrix, second row, third column)
print(matrix_3d[1][2][1])  # Output: 17 (second matrix, third row, second column)

# Iterating over the 3D array
for matrix in matrix_3d:
    for row in matrix:
        for elem in row:
            print(elem, end=" ")
        print()
    print("---")
