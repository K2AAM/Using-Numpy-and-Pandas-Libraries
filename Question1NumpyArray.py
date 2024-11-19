import numpy as np

# Create a NumPy array with integers from 1 to 20
arr = np.arange(1, 21)

# Reshape the array into a 4x5 matrix
matrix = arr.reshape(4, 5)

# Print the matrix
print(matrix)

# This outputs:
# [[ 1  2  3  4  5]
# [ 6  7  8  9 10]
# [11 12 13 14 15]
# [16 17 18 19 20]]
