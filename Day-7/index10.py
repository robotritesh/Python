import numpy as np

# Create a 1D array using NumPy
one_dimensional_array = np.array([1, 2, 3, 4, 5])

# Create a 2D array using NumPy
two_dimensional_array = np.array([[1, 2, 3],
                                 [4, 5, 6],
                                 [7, 8, 9]])

# Access elements in arrays
print(one_dimensional_array[0])  # Output: 1
print(two_dimensional_array[1][2])  # Output: 6

# Modify elements in arrays
one_dimensional_array[2] = 10
two_dimensional_array[2][1] = 20
print(one_dimensional_array)  # Output: [1 2 10 4 5]
print(two_dimensional_array)  # Output: [[1 2 3]
                                   #        [4 5 6]
                                   #        [7 20 9]]

# Perform array operations
sum_of_arrays = one_dimensional_array + two_dimensional_array[0]
print(sum_of_arrays)  # Output: [2 4 13 4 5]

# Create an array from a list
list_of_numbers = [10, 20, 30]
array_from_list = np.array(list_of_numbers)
print(array_from_list)  # Output: [10 20 30]

# Access array attributes
print(array_from_list.shape)  # Output: (3,)
print(array_from_list.dtype)  # Output: int64

# Reshape an array
reshaped_array = array_from_list.reshape(1, 3)
print(reshaped_array)  # Output: [[10 20 30]]

# Create an array of zeros
zeros_array = np.zeros((2, 3))
print(zeros_array)  # Output: [[0. 0. 0.]
                                #        [0. 0. 0.]]

# Create an array of ones
ones_array = np.ones((3, 2))
print(ones_array)  # Output: [[1. 1.]
                                #        [1. 1.]
                                #        [1. 1.]]

# Create an array of random numbers
random_array = np.random.rand(2, 3)
print(random_array)  # Output: [[0.63591417 0.95829143 0.47236184]
                               #        [0.06237726 0.47643271 0.75820242]]