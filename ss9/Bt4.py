import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 200)
y_sin = np.sin(x)
y_cos = np.cos(x)

fig, ax = plt.subplots()

ax.plot(x, y_sin, color='blue', linestyle='-', label='sin(x)')
ax.plot(x, y_cos, color='red', linestyle='--', label='cos(x)')

ax.set_title('So sánh sin(x) và cos(x)')
ax.set_xlabel('Góc (radian)')
ax.set_ylabel('Giá trị')
ax.grid(True)
ax.legend()

plt.show()
