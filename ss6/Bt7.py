import numpy as np
import time

A = np.array([
    [8, 12, 14, 6, 4],
    [18, 13, 2, 2, 12],
    [6, 18, 5, 10, 10],
    [9, 2, 4, 12, 12],
    [2, 3, 2, 17, 3]
])

B = np.array([10, 20, 30, 40, 50])

C = A + B
D = A - B   
print("Kết quả phép cộng ma trận A và B:")
print(C)
print("Kết quả phép trừ ma trận A và B:")
print(D)
value_sqrt = np.sqrt(A)
print("Kết quả lấy căn bậc hai của ma trận A:")
print(value_sqrt)

value_add_5 = np.add(A, 5)
print("Kết quả thêm 5 vào mỗi phần tử của ma trận A:")
print(value_add_5)

large_A = np.random.randint(1, 100, size=(1000, 1000))
large_B = np.random.randint(1, 100, size=1000)

start = time.time()
result_loop = np.zeros_like(large_A)
for i in range(large_A.shape[0]):
    for j in range(large_A.shape[1]):
        result_loop[i, j] = large_A[i, j] + large_B[j]
loop_time = time.time() - start

start = time.time()
result_broadcast = large_A + large_B
broadcast_time = time.time() - start

print(f"\nThời gian thực thi vòng lặp thủ công: "
      f"{loop_time:.6f} giây")
print(f"Thời gian thực thi broadcasting: "
      f"{broadcast_time:.6f} giây")
print(f"Broadcasting nhanh hơn: "
      f"{loop_time/broadcast_time:.2f}")