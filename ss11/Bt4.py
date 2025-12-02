import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 100)

y1 = x
y2 = x**2
y3 = x**3

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(x, y1, 'b-', linewidth=2, label='y = x')
ax.plot(x, y2, 'r-', linewidth=2, label='y = x²')
ax.plot(x, y3, 'g-', linewidth=2, label='y = x³')

ax.set_title('So sánh ba hàm: y = x, y = x², y = x³')
ax.set_xlabel('Trục x')
ax.set_ylabel('Trục y')

ax.legend()

ax.grid(True, linestyle='--', alpha=0.7)

plt.show()
