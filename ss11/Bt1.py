import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 20)
y = x**2 + 2*x

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(x, y, 'b-', linewidth=2, marker='o', markersize=5, label='y = x² + 2x')

ax.set_title('Biểu đồ đầu tay của [Tên]')

ax.set_xlabel('Trục x')
ax.set_ylabel('Trục y')

ax.grid(True, linestyle='--', alpha=0.7)

plt.show()
