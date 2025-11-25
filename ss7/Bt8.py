import pandas as pd
import json
import os
from pathlib import Path

os.makedirs('logs', exist_ok=True)

with open('logs/log_2024-01-01.json', 'w') as f:
    f.write('{"user":"A","action":"login","duration":5}\n')

with open('logs/log_2024-01-02.json', 'w') as f:
    f.write('{"user":"B","action":"logout","duration":3}\n')

all_logs = []

for log_file in sorted(Path('logs').glob('log_*.json')):
    date_str = log_file.stem.replace('log_', '')
    date = pd.to_datetime(date_str)
    
    with open(log_file, 'r') as f:
        for line in f:
            log_entry = json.loads(line.strip())
            log_entry['date'] = date
            all_logs.append(log_entry)

df = pd.DataFrame(all_logs)
print("DataFrame:")
print(df)

daily_summary = df.groupby('date')['duration'].sum().reset_index()
daily_summary.columns = ['date', 'total_duration']

print("\nBáo cáo:")
for _, row in daily_summary.iterrows():
    print(f"Date: {row['date'].strftime('%Y-%m-%d')}, "
          f"Total Duration: {row['total_duration']}")

daily_summary.to_csv('daily_duration_report.csv', index=False)
print("\nĐã xuất báo cáo ra: daily_duration_report.csv")
