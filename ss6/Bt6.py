import numpy as np

arr = np.array([[3, 7, 4, 5], [3, 5, 2, 4], [6, 3, 9, 7], [4, 8, 3, 5]])
print(arr)

sum_of_columns = np.sum(arr, axis=0)
print("Tổng các phần tử theo cột:")
print(sum_of_columns)
mean_of_columns = np.mean(arr, axis=0)
print("Giá trị trung bình các phần tử theo cột:")
print(mean_of_columns)
std_of_columns = np.std(arr, axis=0)
print("Độ lệch chuẩn các phần tử theo cột:")
print(std_of_columns)

sum_of_rows = np.sum(arr, axis=1)
print("Tổng các phần tử theo hàng:")
print(sum_of_rows)
mean_of_rows = np.mean(arr, axis=1)
print("Giá trị trung bình các phần tử theo hàng:")
print(mean_of_rows)
std_of_rows = np.std(arr, axis=1)
print("Độ lệch chuẩn các phần tử theo hàng:")
print(std_of_rows)