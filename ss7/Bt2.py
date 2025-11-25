import pandas as pd

name = ['An', 'Bình', 'Châu', 'Dũng']
age = [20, 21, 22, 20]
score = [8.5, 7.0, 6.5, 9.0]

df = pd.DataFrame({'Tên': name, 'Tuổi': age, 'Điểm': score})

print("DataFrame filtered by loc[]:")
print(df.loc[df['Điểm'] >= 8])
print()

print("DataFrame filtered by iloc[]:")
print(df.iloc[:, [1]])
print()

print("DataFrame filtered by query():")
print(df.query('`Điểm` > 7 and `Tuổi` < 23'))
