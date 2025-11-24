import numpy as np

arr1 = np.arange(1, 11)
print(arr1[0])
print(arr1[-1])
print(arr1[5])

sliced_arr = arr1[2:5]
print(sliced_arr)

arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
row2 = arr2[1, :]
print(row2)
col3 = arr2[:, 2]
print(col3)