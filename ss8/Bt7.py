import pandas as pd
import numpy as np

data = {
    'name': ['An', 'Bình', 'Châu', 'Dũng'],
    'age': [20, np.nan, 22, 21],
    'score': [8.5, np.nan, 7.0, 9.0],
    'city': ['Hà Nội', 'HCM', np.nan, 'Hà Nội']
}

df = pd.DataFrame(data)
print("Bảng dữ liệu ban đầu:")
print(df)

print("Kiểm tra dữ liệu thiếu (isna()):")
print(df.isna())
print(f"\nTổng số giá trị thiếu: \n{df.isna().sum()}")

df['age'] = df['age'].fillna(df['age'].mean())
df['score'] = df['score'].fillna(df['score'].median())
df['city'] = df['city'].fillna('Unknown')

print(f"age_cleaned = {df['age'].tolist()}")
print(f"score_cleaned = {df['score'].tolist()}")
print(f"city_cleaned = {df['city'].tolist()}")

df['city'] = df['city'].astype('category')
print(f"Kiểu dữ liệu city: {df['city'].dtype}")


def classify_score(score):
    if score >= 8.5:
        return 'Good'
    elif score >= 7.0:
        return 'Average'
    else:
        return 'Bad'


df['score_level'] = df['score'].apply(classify_score)
print(f"score_level = {df['score_level'].tolist()}")

df['age_normalized'] = (df['age'] - df['age'].mean()) / df['age'].std()
print(f"age_normalized = {df['age_normalized'].tolist()}")

print("DataFrame cuối cùng:")
print(df)
