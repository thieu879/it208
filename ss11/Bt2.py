import numpy as np
import matplotlib.pyplot as plt

x = np.random.uniform(0, 50, 20)
y = np.random.uniform(0, 50, 20)

fig, ax = plt.subplots(figsize=(8, 6))

ax.scatter(x, y, color='red', marker='o', label='Điểm dữ liệu')

ax.set_title('Biểu đồ scatter của x và y')
ax.set_xlabel('Trục x')
ax.set_ylabel('Trục y')

plt.show()
