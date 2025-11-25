import pandas as pd

name = ['An', 'Bình', 'Châu', 'Dũng']
age = [20, 21, 22, 20]
score = [8.5, 7.0, 6.5, 9.0]

df = pd.DataFrame({'name': name, 'age': age, 'score': score})

df['age_group'] = df['age'].apply(lambda x: 'Young' if x <= 20 else 'Adult')
print("DataFrame sau khi áp dụng apply():")
print(df)

score_mapping = {
    8.5: 'Excellent', 7.0: 'Good', 6.5: 'Average', 9.0: 'Excellent'
}
df['score_level'] = df['score'].map(score_mapping)
print("DataFrame sau khi map():")
print(df[['name', 'age', 'score', 'score_level']])

df_int = df.copy()
df_int['score'] = df_int['score'].astype(int)
print("DataFrame sau khi astype():")
print(df_int[['name', 'age', 'score']])

df_original = pd.DataFrame({'name': name, 'age': age, 'score': score})
df_original['name'] = df_original['name'].replace('Bình', 'Bình (Updated)')
print("DataFrame sau khi replace():")
print(df_original)
