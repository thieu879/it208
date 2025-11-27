import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = 2 * x + 1
y2 = -x + 10

fig, ax = plt.subplots()

ax.plot(x, y1, color='blue', label='Đường 1')
ax.plot(x, y2, color='orange', label='Đường 2')

ax.set_title('Giao điểm của hai đường thẳng')
ax.set_xlabel('Trục x')
ax.set_ylabel('Trục y')
ax.grid(True)
ax.legend(loc='upper left')

plt.show()
