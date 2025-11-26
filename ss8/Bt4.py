import pandas as pd

name = ['An', 'Bình', 'Châu', 'Dũng', 'Hà']
age = [20, 21, 22, 20, 23]
score = [7.5, 8.0, 6.5, 9.0, 8.5]

score_series = pd.Series(score, index=name)
print("Series điểm sinh viên:")
print(score_series)
print()

df = pd.DataFrame({
    'name': name,
    'age': age,
    'score': score
})

print("DataFrame:")
print(df)
print()

print("=== df.info() ===")
df.info()
print()

print("=== df.describe() ===")
print(df.describe())
print()

high_score_students = df[df['score'] >= 8.0]
print("Sinh viên >= 8 điểm:")
print(high_score_students.values.tolist())
