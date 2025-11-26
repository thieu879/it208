import numpy as np

a = np.array([[1], [2], [3], [4]])
print("Mảng a (4,1):")
print(a)
print(f"Shape: {a.shape}\n")

b = np.array([[10, 20, 30, 40, 50]])
print("Mảng b (1,5):")
print(b)
print(f"Shape: {b.shape}\n")

result = a * b
print("Kết quả a * b (broadcasting):")
print(result)

result_sqrt = np.sqrt(result)
print("sqrt(a * b):")
print(result_sqrt)

result_log = np.log(result)
print("log(a * b):")
print(result_log)

print("Thống kê theo axis=1")
print(f"min theo axis=1: {np.min(result, axis=1)}")
print(f"max theo axis=1: {np.max(result, axis=1)}")
print(f"mean theo axis=1: {np.mean(result, axis=1)}")
print(f"std theo axis=1: {np.std(result, axis=1)}")
