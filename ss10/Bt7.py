import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="whitegrid")
np.random.seed(42)

n = 500
hours = np.random.uniform(1, 10, n)
noise = np.random.normal(0, 5, n)
score = np.clip(hours * 10 + noise, 0, 100)
majors = np.random.choice(['A', 'B', 'C'], n)

df = pd.DataFrame({
    'Hours': hours,
    'Score': score,
    'Major': majors
})

plt.figure(figsize=(8, 4))
sns.histplot(df['Score'], bins=20, kde=True, color='skyblue')
plt.title('Phân phối điểm thi')
plt.xlabel('Điểm')
plt.ylabel('Số lượng sinh viên')
plt.show()

plt.figure(figsize=(8, 4))
sns.scatterplot(x='Hours', y='Score', data=df, hue='Major', palette='Set2')
plt.title('Mối quan hệ giữa giờ học và điểm')
plt.xlabel('Số giờ học')
plt.ylabel('Điểm thi')
plt.show()

plt.figure(figsize=(8, 4))
sns.boxplot(x='Major', y='Score', data=df, palette='pastel')
plt.title('So sánh điểm theo nhóm ngành')
plt.xlabel('Nhóm ngành')
plt.ylabel('Điểm thi')
plt.show()

print("Nhận xét:")
print(
    "1. Phân phối: Điểm thi có dạng gần chuẩn, tập trung quanh 50–70, "
    "nhưng có một số ngoại lệ cao hoặc thấp."
)
print(
    "2. Quan hệ: Có mối quan hệ dương giữa số giờ học và điểm thi, "
    "học nhiều điểm cao hơn, nhưng vẫn có nhiễu."
)
print(
    "3. Nhóm ngành: Nhóm A, B, C có điểm trung bình khá tương đồng, "
    "nhưng nhóm nào có khoảng biến động rộng hơn thể hiện sự không đồng đều "
    "giữa sinh viên."
)
