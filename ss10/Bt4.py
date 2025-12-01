import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

classes = ["A", "A", "A", "B", "B", "C", "C"]

scores = [7.5, 8.0, 9.0, 6.5, 7.0, 8.2, 8.7]

df = pd.DataFrame({"class": classes, "score": scores})

plt.figure(figsize=(8, 6))
sns.barplot(x="class", y="score", data=df, ci=None)
plt.title("Điểm trung bình theo lớp")
plt.xlabel("Lớp")
plt.ylabel("Điểm trung bình")
plt.ylim(0, 10)
plt.show()