import numpy as np
import time

arr = np.arange(1, 21)
print(arr)

squared_arr = arr ** 2
print("Mảng sau khi bình phương mỗi phần tử:")
print(squared_arr)

sqrt_arr = np.sqrt(arr)
print("Mảng sau khi lấy căn bậc hai của mỗi phần tử:")
print(sqrt_arr)

arr_b = np.array([
    5, 10, 15, 20, 1, 2, 3, 4, 5, 6,
    7, 8, 9, 10, 11, 12, 13, 14, 15, 16
])
result_add_arrays = np.add(arr, arr_b)
print("Kết quả:", result_add_arrays)
result_multiply = np.multiply(arr, 5)
print("Kết quả:", result_multiply)
result_sqrt = np.sqrt(arr)
print("Kết quả:", result_sqrt)

arr2d = np.random.randint(1, 100, size=(1000, 1000))
start = time.time()
result_loop = np.zeros_like(arr2d)
for i in range(arr2d.shape[0]):
    for j in range(arr2d.shape[1]):
        result_loop[i, j] = arr2d[i, j] ** 2
loop_time = time.time() - start

start = time.time()
result_vec = arr2d ** 2
vec_time = time.time() - start

print(f"Thời gian vòng lặp: {loop_time:.6f}s")
print(f"Thời gian vectorization: {vec_time:.6f}s")