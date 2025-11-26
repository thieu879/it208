import json

lines_to_write = [
    "Đây là dòng thứ nhất\n",
    "Đây là dòng thứ hai\n",
    "Đây là dòng thứ ba\n",
    "Đây là dòng thứ tư\n",
    "Đây là dòng thứ năm\n"
]

with open('ss8/data.txt', 'w', encoding='utf-8') as f:
    f.writelines(lines_to_write)

with open('ss8/data.txt', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f, 1):
        print(f"Dòng {i}: {line.strip()}")

student = {
    "name": "An",
    "age": 20,
    "scores": [8, 9, 7]
}

with open('ss8/student.json', 'w', encoding='utf-8') as f:
    json.dump(student, f, ensure_ascii=False, indent=2)

with open('ss8/student.json', 'r', encoding='utf-8') as f:
    student_data = json.load(f)

print(f"JSON đọc từ file: {student_data}")
