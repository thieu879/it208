import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(0, 1, 1000)

fig, ax = plt.subplots(figsize=(10, 6))

ax.hist(
    data, 
    bins=30, 
    color='skyblue', 
    edgecolor='black', 
    alpha=0.7, 
    label='Phân phối chuẩn'
)

ax.set_title('Histogram phân phối chuẩn (1000 giá trị, 30 bins)')
ax.set_xlabel('Giá trị')
ax.set_ylabel('Tần suất')

ax.legend()

ax.grid(True, linestyle='--', alpha=0.5)

plt.show()
