import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

matrix = np.random.randint(0, 100, size=(10, 10))

fig, ax = plt.subplots(figsize=(10, 8))

sns.heatmap(matrix, 
            annot=True,
            fmt='d',
            cmap='YlOrRd',
            cbar=True,
            linewidths=0.5,
            linecolor='gray',
            ax=ax)

ax.set_title(
    'Heatmap ma trận 10x10 với giá trị ngẫu nhiên', 
    fontsize=14, 
    fontweight='bold'
)
ax.set_xlabel('Cột')
ax.set_ylabel('Hàng')

plt.tight_layout()
plt.show()
