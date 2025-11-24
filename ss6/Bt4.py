import numpy as np

A = np.array([[5, 6, 8], [7, 2, 4], [1, 6, 3]])
B = np.array([10, 20, 30])

C = A + B
D = A - B

print("Kết quả phép cộng ma trận A và B:")
print(C)
print("Kết quả phép trừ ma trận A và B:")
print(D)