import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

majors = ['CNTT', "Kinh Tế", 'Ngôn ngữ']

scores = {
    'CNTT': [8.5, 7.0, 9.0, 6.5, 8.0],
    'Kinh Tế': [7.5, 8.0, 6.5, 7.0, 8.2],
    'Ngôn ngữ': [9.0, 8.5, 7.5, 8.0, 9.2]
}

data = []
for major, vals in scores.items():
    for val in vals:
        data.append((major, val))
df = pd.DataFrame(data, columns=["majors", "score"])

plt.figure(figsize=(8, 6))
sns.boxplot(x="majors", y="score", data=df, palette="Set3")
plt.title("Phân bố điểm theo ngành học")
plt.xlabel("Ngành học")
plt.ylabel("Điểm")
plt.ylim(0, 10)
plt.show()

plt.figure(figsize=(8, 6))
sns.violinplot(x="majors", y="score", data=df, palette="Set2")
plt.title("Phân bố điểm theo ngành học (Violin Plot)")
plt.xlabel("Ngành học")
plt.ylabel("Điểm")
plt.ylim(0, 10)
plt.show()