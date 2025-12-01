import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(42)
scores = np.random.normal(7, 1.5, 200)
scores = np.clip(scores, 0, 10)

plt.figure(figsize=(8, 5))
sns.histplot(scores, bins=10, kde=True)
plt.title("Phân bố điểm thi")
plt.xlabel("Điểm")
plt.ylabel("Tần suất")
plt.show()