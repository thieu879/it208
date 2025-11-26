import pandas as pd

students_data = """id,name
1,An
2,Binh
3,Chau"""

with open('ss8/students.csv', 'w', encoding='utf-8') as f:
    f.write(students_data)

scores_data = """id,score
1,8
2,9
3,7"""

with open('ss8/scores.csv', 'w', encoding='utf-8') as f:
    f.write(scores_data)

df_students = pd.read_csv('ss8/students.csv')
df_scores = pd.read_csv('ss8/scores.csv')

print("DataFrame students:")
print(df_students)
print("\nDataFrame scores:")
print(df_scores)

df_merged = pd.merge(df_students, df_scores, on='id')
print("\nDataFrame sau khi merge:")
print(df_merged)

df_report = df_merged.groupby(['id', 'name'])['score'].agg(
    score_min='min',
    score_max='max',
    score_mean='mean'
).reset_index()

print("\nReport (min, max, mean):")
print(df_report)

df_report.to_csv('ss8/report.csv', index=False)
print("\nFile report.csv đã được lưu")
