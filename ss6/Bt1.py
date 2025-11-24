import numpy as np

arr1 = np.arange(1, 11).astype(np.int32)
print(arr1)

shape1 = arr1.shape
dtype1 = arr1.dtype
print("Shape:", shape1)
print("Data type:", dtype1)

arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).astype(np.int32)
print(arr2)

shape2 = arr2.shape
dtype2 = arr2.dtype
print("Shape:", shape2)
print("Data type:", dtype2)

arr2_float = arr2.astype(np.float32)
print("Mảng 2 chiều sau khi chuyển sang float32:")
print(arr2_float)
print("Dtype mới:", arr2_float.dtype)