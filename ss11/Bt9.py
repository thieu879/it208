import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

start_date = datetime(2025, 12, 1)
dates = [start_date + timedelta(days=i) for i in range(30)]

np.random.seed(42)

trend = np.linspace(20, 28, 30)
noise = np.random.normal(0, 2, 30)
temperature = trend + noise

temperature[5] += 8
temperature[15] -= 10
temperature[25] += 6

fig, ax = plt.subplots(figsize=(14, 7))

ax.plot(
    dates, 
    temperature, 
    'b-', 
    linewidth=2, marker='o', markersize=5, label='Nhiệt độ hàng ngày'
)

z = np.polyfit(range(30), temperature, 1)
trendline = np.polyval(z, range(30))
ax.plot(dates, trendline, 'r--', linewidth=2, label='Đường xu hướng')

special_days = [5, 15, 25]
special_labels = [
    'Nóng bất thường\n+8°C', 'Lạnh đột ngột\n-10°C', 'Nóng đột ngột\n+6°C'
]
colors = ['orange', 'cyan', 'magenta']

for day, label, color in zip(special_days, special_labels, colors):
    ax.scatter(
        dates[day], 
        temperature[day], 
        s=200, c=color, 
        zorder=5, 
        edgecolors='black', 
        linewidths=2
    )
    
    ax.annotate(label, 
                xy=(dates[day], temperature[day]), 
                xytext=(15, 15), 
                textcoords='offset points',
                bbox=dict(boxstyle='round,pad=0.5', 
                          facecolor=color, alpha=0.7, edgecolor='black'),
                arrowprops=dict(arrowstyle='->', color='black', lw=1.5),
                fontsize=10, 
                fontweight='bold')

ax.set_title(
    'Chuỗi thời gian nhiệt độ hàng ngày - Tháng 12/2025', 
    fontsize=16, 
    fontweight='bold'
)
ax.set_xlabel('Ngày', fontsize=12)
ax.set_ylabel('Nhiệt độ (°C)', fontsize=12)

ax.grid(True, linestyle='--', alpha=0.5)

ax.legend(loc='upper left', fontsize=11)

plt.xticks(rotation=45, ha='right')

plt.tight_layout()

plt.show()
