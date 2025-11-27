import matplotlib.pyplot as plt

thang = list(range(1, 13))
nhiet_do = [20, 22, 25, 28, 30, 32, 31, 30, 28, 26, 23, 21]
luong_mua = [10, 15, 30, 120, 200, 250, 280, 220, 150, 80, 30, 15]

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(thang, nhiet_do, color='red', linestyle='-', linewidth=2, 
        label='Nhiệt độ trung bình (°C)')

ax.scatter(thang, luong_mua, color='blue', s=80, label='Lượng mưa (mm)')

ax.set_title('Nhiệt độ và lượng mưa Hà Nội 2025')
ax.set_xlabel('Tháng')
ax.set_ylabel('Giá trị')
ax.grid(True)
ax.legend()

plt.show()
