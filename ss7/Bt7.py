import pandas as pd

date = ['2023-01-01', '2023-02-01', '2023-03-01']
name = ['An', 'Bình', 'Châu']

df = pd.DataFrame({
    'date': date,
    'name': name
})

df['date'] = pd.to_datetime(df['date'])
print("Date converted to datetime:")
print(df)

print("\nExtracted Year:")
print(df['date'].dt.year)

df['name'] = df['name'].astype('category')
print("\nCategory Type for name:")
print(df['name'])
