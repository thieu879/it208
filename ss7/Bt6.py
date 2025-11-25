import pandas as pd

df1 = pd.DataFrame({
    'id': [1, 2, 3],
    'name': ['An', 'Bình', 'Châu']
})

df2 = pd.DataFrame({
    'id': [1, 2, 3],
    'score': [8.5, 7.0, 6.5]
})

merged_df = pd.merge(df1, df2, on='id')
print("Merged DataFrame:")
print(merged_df)

df3 = pd.DataFrame({'age': [20, 21, 22]})
concatenated_df = pd.concat([merged_df, df3], axis=1)
print("\nConcatenated DataFrame:")
print(concatenated_df)
