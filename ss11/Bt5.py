import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 50)
y1 = x
y2 = x**2

x_rand1 = np.random.uniform(0, 10, 50)
y_rand1 = np.random.uniform(0, 50, 50)

x_rand2 = np.random.uniform(0, 10, 50)
y_rand2 = np.random.uniform(0, 100, 50)

fig, axs = plt.subplots(2, 2, figsize=(12, 10))

axs[0, 0].plot(x, y1, 'b-', linewidth=2, label='y = x')
axs[0, 0].set_title('Đường thẳng y = x')
axs[0, 0].set_xlabel('Trục x')
axs[0, 0].set_ylabel('Trục y')
axs[0, 0].grid(True, linestyle='--', alpha=0.7)
axs[0, 0].legend()

axs[1, 0].plot(x, y2, 'r-', linewidth=2, label='y = x²')
axs[1, 0].set_title('Đường cong y = x²')
axs[1, 0].set_xlabel('Trục x')
axs[1, 0].set_ylabel('Trục y')
axs[1, 0].grid(True, linestyle='--', alpha=0.7)
axs[1, 0].legend()

axs[0, 1].scatter(
    x_rand1, y_rand1, color='green', alpha=0.6, label='Điểm ngẫu nhiên'
)
axs[0, 1].set_title('Scatterplot ngẫu nhiên 1')
axs[0, 1].set_xlabel('Trục x')
axs[0, 1].set_ylabel('Trục y')
axs[0, 1].grid(True, linestyle='--', alpha=0.7)
axs[0, 1].legend()

axs[1, 1].scatter(
    x_rand2, y_rand2, color='purple', alpha=0.6, label='Điểm ngẫu nhiên'
)
axs[1, 1].set_title('Scatterplot ngẫu nhiên 2')
axs[1, 1].set_xlabel('Trục x')
axs[1, 1].set_ylabel('Trục y')
axs[1, 1].grid(True, linestyle='--', alpha=0.7)
axs[1, 1].legend()

plt.tight_layout()

plt.show()
