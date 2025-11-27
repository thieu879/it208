import matplotlib.pyplot as plt
import numpy as np

nam = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
dan_so = [92, 93, 94, 95, 96, 97, 98, 99, 100, 101]

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(nam, dan_so, color='blue', linestyle='-', linewidth=2, 
        marker='o', markersize=6, label='Dân số Việt Nam')

ax.set_title('Tăng trưởng dân số Việt Nam 2015–2024', fontsize=14)
ax.set_xlabel('Năm')
ax.set_ylabel('Dân số (triệu người)')
ax.grid(True)
ax.legend()

plt.show()
