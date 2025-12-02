import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x = np.linspace(0, 2 * np.pi, 100)

fig, ax = plt.subplots(figsize=(10, 6))
line, = ax.plot(x, np.sin(x), 'b-', linewidth=2)

ax.set_title('Đồ thị động y = sin(x + t)', fontsize=14, fontweight='bold')
ax.set_xlabel('Trục x')
ax.set_ylabel('Trục y')
ax.set_ylim(-1.5, 1.5)
ax.grid(True, linestyle='--', alpha=0.7)


def update(frame):
    y = np.sin(x + 0.1 * frame)
    line.set_ydata(y)
    return line,


ani = FuncAnimation(
    fig, update, frames=200, interval=30, blit=True, repeat=True
)

plt.tight_layout()
plt.show()

# ani.save('ss11/sin_wave.gif', writer='pillow', fps=20)
