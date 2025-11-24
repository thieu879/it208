import numpy as np

arr = np.array([[6, 9, 7], [2, 1, 5], [7, 8, 3]])

value_inv = np.linalg.inv(arr)
print("Ma trận nghịch đảo:")
print(value_inv)

eigenvectors, eigenvalues = np.linalg.eig(arr)
print("Vector riêng:")
print(eigenvectors)
print("Giá trị riêng:")
print(eigenvalues)