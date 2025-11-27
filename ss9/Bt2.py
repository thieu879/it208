import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 100)
y = x ** 3

fig, ax = plt.subplots(figsize=(8, 6))

ax.plot(x, y, color='red', linewidth=3)

ax.set_title('Đồ thị hàm bậc ba y = x³')
ax.set_xlabel('Giá trị x')
ax.set_ylabel('Giá trị y')
ax.grid(True, linestyle='--', alpha=0.6)

plt.show()
