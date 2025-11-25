import pandas as pd

name = ['An', 'Bình', 'Châu', 'Dũng']
age = [20, 21, 22, 20]
score = [8.5, 7.0, 6.5, 9.0]

df = pd.DataFrame({
    'name': name,
    'age': age,
    'score': score
})

print("DataFrame gốc:")
print(df)
print()

print("="*60)
print("PHẦN 1: GROUPBY VÀ AGGREGATION")
print("="*60)

grouped = df.groupby('age').agg({
    'score': ['mean', 'min', 'max']
})

grouped_result = df.groupby('age')['score'].agg([
    ('mean_score', 'mean'),
    ('min_score', 'min'),
    ('max_score', 'max')
]).reset_index()

print("\nGroupby age:")
print(grouped_result)

print("\n" + "="*60)
print("PHẦN 2: CHI TIẾT TỪNG NHÓM")
print("="*60)

for age_group, data in df.groupby('age'):
    print(f"\nNhóm tuổi {age_group}:")
    print(data)
    print(f"Mean score: {data['score'].mean()}")
    print(f"Min score: {data['score'].min()}")
    print(f"Max score: {data['score'].max()}")

print("\n" + "="*60)
print("PHẦN 3: CẬP NHẬT DỮ LIỆU")
print("="*60)

df.loc[df['name'] == 'Bình', 'name'] = 'Bình (Updated)'

print("\nDataFrame sau khi cập nhật:")
print(df)
