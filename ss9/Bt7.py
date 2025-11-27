import matplotlib.pyplot as plt

san_pham = ['Áo', 'Quần', 'Giày', 'Túi', 'Mũ', 'Tất']
doanh_so = [150, 120, 200, 90, 65, 80]

fig, ax = plt.subplots()

bars = ax.bar(san_pham, doanh_so, color='green', edgecolor='black')

for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height,
            f'{int(height)}',
            ha='center', va='bottom',
            color='white', fontweight='bold')

ax.set_title('Doanh số bán hàng tháng 10/2025')

plt.show()
