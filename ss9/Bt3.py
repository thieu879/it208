import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 20)
y = 2 * x + 3

fig, ax = plt.subplots()
ax.plot(x, y, color='blue', linewidth=3)

ax.set_title('Đường thẳng y = 2x + 3')
ax.set_xlabel('Trục x')
ax.set_ylabel('Trục y')
ax.grid(True)

plt.show()