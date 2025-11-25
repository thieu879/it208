import pandas as pd

series = pd.Series([1, 2, 3, 4, 5])
print("Chuỗi Pandas:")
print(series)

name = ['An', 'Bình', 'Châu', 'Dũng']
score = [8.5, 7.0, 6.5, 9.0]
df = pd.DataFrame({'Tên': name, 'Điểm': score})

print("DataFrame Pandas:")
df.info()

print("DataFrame describe:")
print(df.describe())