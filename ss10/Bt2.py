import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

subjects = [
    "Toán", "Văn", "Anh", "Lý", "Hóa", "Sinh",
    "Sử", "Địa", "GDCD", "Công nghệ", "Thể dục"
]

base_scores = [7.5, 8.0, 6.5, 9.0, 5.5, 7.0, 8.5, 6.0, 7.8, 9.2, 5.8]

records = list(zip(subjects, base_scores))

for subject in subjects:
    subject_scores = np.random.normal(
        loc=np.random.uniform(6, 8), scale=1, size=50
    )
    subject_scores = np.clip(subject_scores, 0, 10)
    records.extend([(subject, float(s)) for s in subject_scores])

df = pd.DataFrame(records, columns=["subject", "score"])

sns.displot(
    df, x="score", hue="subject", kind="kde", fill=True, height=5, aspect=1.5
)
plt.title("Phân bố điểm thi theo môn học")
plt.xlabel("Điểm")
plt.ylabel("Mật độ")
plt.show()