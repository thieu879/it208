import pandas as pd

name = ['An', 'Bình', 'Châu', 'Dũng']
age = [20, None, 22, 20]
score = [8.5, None, 6.5, 9.0]

df = pd.DataFrame({'name': name, 'age': age, 'score': score})

print("Dữ liệu thiếu kiểm tra bằng isna():")
print(df.isna())

print(df.fillna({
    'age': df['age'].mean().round()
}))

print(df.dropna())