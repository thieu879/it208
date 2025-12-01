import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

hours = np.arange(1, 11)
noise = np.random.normal(0, 1, len(hours))
scores = hours * 1.2 + noise

df = pd.DataFrame({"hours": hours, "scores": scores})

plt.figure(figsize=(8, 6))
plt.scatter(df["hours"], df["scores"])
plt.xlabel("Số giờ học")
plt.ylabel("Điểm số")
plt.title("Mối quan hệ giữa thời gian học và điểm thi")
plt.grid(True)
plt.show()