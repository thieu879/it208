from datetime import datetime
import os

filename = 'ss5/log.txt'

if not os.path.exists(filename):
    print("File không tồn tại.")
else:
    today = datetime.today().date()
    timestamp_format = '%Y-%m-%d %H:%M:%S'

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split(' ', 2)
            if len(parts) < 3:
                continue

            timestamp_str = parts[0] + ' ' + parts[1]

            try:
                timestamp = datetime.strptime(timestamp_str, timestamp_format)
                if timestamp.date() == today:
                    print(line.strip())
            except ValueError:
                continue
