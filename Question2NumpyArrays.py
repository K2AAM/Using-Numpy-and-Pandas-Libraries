import numpy as np

A = np.array([1, 2, 3, 4, 5])
B = np.array([5, 4, 3, 2, 1])
C = np.array([6, 7, 8, 9, 10])  # Corrected C to have 5 elements

# Element-wise addition
add_result = A + B + C
print("Element-wise Addition:", add_result)

# Element-wise multiplication
mul_result = A * B * C
print("Element-wise Multiplication:", mul_result)

# Element-wise subtraction
sub_result = A - B
print("Element-wise Subtraction:", sub_result)

# Element-wise division
div_result = A / B
print("Element-wise Division:", div_result)

# This outputs:
# Element-wise Addition: [12 13 14 15 16]
# Element-wise Multiplication: [30 56 72 72 50]
# Element-wise Subtraction: [-4 -2  0  2  4]
# Element-wise Division: [0.2 0.5 1.  2.  5. ]
