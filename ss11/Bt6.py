import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(x, y, 'b-', linewidth=2, label='y = sin(x)')

x_point = np.pi / 2
y_point = np.sin(x_point)

ax.plot(x_point, y_point, 'ro', markersize=8)

ax.annotate('Giá trị cực đại\n(x = π/2, y = 1)', 
            xy=(x_point, y_point),
            xytext=(x_point + 1, y_point - 0.3),
            arrowprops=dict(facecolor='red', arrowstyle='->', lw=2),
            fontsize=12, 
            fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.7))

ax.set_title('Đồ thị y = sin(x) với chú thích tại x = π/2')
ax.set_xlabel('Trục x')
ax.set_ylabel('Trục y')

ax.legend()

ax.grid(True, linestyle='--', alpha=0.7)

plt.show()
