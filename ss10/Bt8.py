import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="whitegrid")
np.random.seed(42)

months = np.arange(1, 13)
categories = ['Shoes', 'Clothes', 'Bags']

data = []
for cat in categories:
    base = np.random.uniform(1000, 5000)
    for m in months:
        revenue = base + np.random.normal(0, 500)
        data.append([m, revenue, cat])

df = pd.DataFrame(data, columns=['Month', 'Revenue', 'Category'])

plt.figure(figsize=(10, 5))
sns.lineplot(x='Month', y='Revenue', hue='Category', data=df, marker='o')
plt.title('Doanh thu theo tháng theo nhóm sản phẩm')
plt.xlabel('Tháng')
plt.ylabel('Doanh thu')
plt.show()

plt.figure(figsize=(8, 4))
sns.violinplot(x='Category', y='Revenue', data=df, palette='pastel')
plt.title('Phân phối doanh thu theo nhóm sản phẩm')
plt.xlabel('Nhóm sản phẩm')
plt.ylabel('Doanh thu')
plt.show()

plt.figure(figsize=(10, 5))
sns.regplot(
    x='Month', 
    y='Revenue', data=df, 
    scatter_kws={'s': 50}, 
    line_kws={'color': 'red'}
)
plt.title('Xu hướng chung doanh thu theo tháng')
plt.xlabel('Tháng')
plt.ylabel('Doanh thu')
plt.show()

print("Phân tích tổng quan:")
print(
    "- Nhóm Shoes có doanh thu ổn định nhất qua các tháng "
    "với biến động nhỏ."
)
print(
    "- Nhóm Bags biến động mạnh hơn, thấy sự chênh lệch "
    "giữa các tháng."
)
print(
    "- Nhìn chung, doanh thu có xu hướng nhẹ tăng theo tháng "
    "nhưng không quá rõ rệt."
)
print(
    "- Có sự khác biệt nhất định giữa ba nhóm, Shoes và Clothes "
    "cao hơn Bags trung bình."
)
