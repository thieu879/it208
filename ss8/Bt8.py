import json
import pandas as pd
from pathlib import Path
from datetime import datetime

logs_dir = Path('ss8/logs')
json_files = list(logs_dir.glob('*.json'))

print(f"Tìm thấy {len(json_files)} file JSON:")
for file in json_files:
    print(f"  - {file.name}")
print()

all_logs = []

for file_path in json_files:
    filename = file_path.stem
    date_str = filename.replace('log_', '')
    
    try:
        log_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        
        with open(file_path, 'r', encoding='utf-8') as f:
            logs = json.load(f)
        
        for log in logs:
            log['date'] = log_date
            all_logs.append(log)
    
    except ValueError:
        print(f"Không thể parse ngày từ file: {file_path.name}")
        continue

df = pd.DataFrame(all_logs)
print("DataFrame từ tất cả file log:")
print(df)
print()

daily_summary = df.groupby('date')['duration'].sum().reset_index()
daily_summary.columns = ['date', 'total_duration']

print("Tổng duration theo ngày:")
print(daily_summary)
print()

daily_summary.to_csv('ss8/daily_report.csv', index=False)
print("Đã xuất file daily_report.csv")
