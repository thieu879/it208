import numpy as np

arr = np.array([[88, 35, 62], [11, 98, 34], [64, 24, 48]])
print(arr)

value_min = np.min(arr)
print("Giá trị nhỏ nhất trong mảng là:", value_min)
value_max = np.max(arr)
print("giá trị lớn nhất trong mảng là:", value_max)
value_sum = np.sum(arr)
print("tổng giá trị trong mảng là:", value_sum)
value_mean = np.mean(arr)
print("giá trị trung bình trong mảng là:", value_mean)
value_std = np.std(arr)
print("độ lệch chuẩn trong mảng là:", value_std)

sum_of_columns = np.sum(arr, axis=0)
print("Tổng các cột trong mảng là:", sum_of_columns)
mean_of_columns = np.mean(arr, axis=0)
print("Giá trị trung bình các cột trong mảng là:", mean_of_columns)

sum_of_rows = np.sum(arr, axis=1)
print("Tổng các hàng trong mảng là:", sum_of_rows)
mean_of_rows = np.mean(arr, axis=1)
print("Giá trị trung bình các hàng trong mảng là:", mean_of_rows)