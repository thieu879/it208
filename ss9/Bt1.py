import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 50)
y = np.sin(x)

fig, ax = plt.subplots()

ax.plot(x, y)

ax.set_title('Biểu đồ đầu tay của [Tên]')
ax.set_xlabel('Trục x')
ax.set_ylabel('Trục y')
ax.grid(True, linestyle='--')

plt.show()
