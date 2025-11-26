import numpy as np

arr = np.arange(12).reshape(3, 4)

row_2 = arr[1]
print(f"Hàng 2: {row_2}")

col_3 = arr[:, 2]
print(f"Cột 3: {col_3}")

submatrix = arr[1:3, 1:3]
print(f"Submatrix: {submatrix}")

arr_float = arr.astype(np.float64)
print(f"Dtype mới: {arr_float.dtype}")
