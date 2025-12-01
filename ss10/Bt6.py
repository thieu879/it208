import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(42)
day = np.arange(1, 31)
sales = 100 + day * 5 + np.random.normal(0, 20, size=30)

df = pd.DataFrame({'Day': day, 'Sales': sales})

plt.figure(figsize=(10, 5))
sns.lineplot(x='Day', y='Sales', data=df, marker='o')
plt.title('Doanh thu theo ngày')
plt.xlabel('Ngày')
plt.ylabel('Doanh thu')
plt.show()

plt.figure(figsize=(10, 5))
sns.regplot(
    x='Day',
    y='Sales',
    data=df,
    scatter_kws={'s': 50},
    line_kws={'color': 'red'}
)
plt.title('Xu hướng doanh thu theo ngày (Regplot)')
plt.xlabel('Ngày')
plt.ylabel('Doanh thu')
plt.show()

print("Nhận xét:")
print(
    "- Doanh thu có xu hướng tăng dần theo ngày."
)
print(
    "- Dữ liệu có một số biến động nhỏ do noise, "
    "nhưng xu hướng tổng thể vẫn rõ ràng."
)
print(
    "- Đường hồi quy tuyến tính cho thấy xu hướng "
    "tăng ổn định."
)
