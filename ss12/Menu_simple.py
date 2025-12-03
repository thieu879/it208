import csv
import json
import os
import matplotlib.pyplot as plt

students = []


def calculate_average(math, physics, chemistry):
    """Calculate average score"""
    return round((math + physics + chemistry) / 3, 2)


def classify_grade(average):
    """Classify grade based on average score"""
    if average >= 8.5:
        return "Excellent"
    elif average >= 7.0:
        return "Good"
    elif average >= 5.0:
        return "Average"
    else:
        return "Poor"


def load_data():
    """Function 1: Load data from CSV or JSON file"""
    global students
    
    if os.path.exists('ss12/data.csv'):
        with open('ss12/data.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            students = []
            for row in reader:
                students.append({
                    'id': row['id'],
                    'name': row['name'],
                    'math': float(row['math']),
                    'physics': float(row['physics']),
                    'chemistry': float(row['chemistry']),
                    'average': float(row['average']),
                    'grade': row['grade']
                })
        print(f"\nLoaded {len(students)} students from data.csv")
    elif os.path.exists('ss12/data.json'):
        with open('ss12/data.json', 'r', encoding='utf-8') as f:
            students = json.load(f)
        print(f"\nLoaded {len(students)} students from data.json")
    else:
        print("\nNo data file found. Starting with empty list.")


def display_students():
    """Function 1: Display student list"""
    if not students:
        print("\nList is empty!")
        return
    
    print("\n" + "="*80)
    print(f"{'ID':<10} {'Name':<20} {'Math':<6} {'Physics':<6} {'Chemistry':<6} {'Avg':<6} {'Grade':<15}")
    print("="*80)
    for student in students:
        print(f"{student['id']:<10} {student['name']:<20} {student['math']:<6.1f} {student['physics']:<6.1f} "
              f"{student['chemistry']:<6.1f} {student['average']:<6.2f} {student['grade']:<15}")
    print("="*80)


def add_student():
    """Function 2: Add new student"""
    print("\n--- ADD NEW STUDENT ---")
    
    student_id = input("Student ID: ").strip()
    
    if any(s['id'] == student_id for s in students):
        print("Student ID already exists!")
        return
    
    name = input("Name: ").strip()
    
    try:
        math = float(input("Math score (0-10): "))
        physics = float(input("Physics score (0-10): "))
        chemistry = float(input("Chemistry score (0-10): "))
        
        if not (0 <= math <= 10 and 0 <= physics <= 10 and 0 <= chemistry <= 10):
            print("Scores must be between 0 and 10!")
            return
        
        avg = calculate_average(math, physics, chemistry)
        grade = classify_grade(avg)
        
        students.append({
            'id': student_id,
            'name': name,
            'math': math,
            'physics': physics,
            'chemistry': chemistry,
            'average': avg,
            'grade': grade
        })
        
        print(f"Added student {name} - Average: {avg} - {grade}")
        
    except ValueError:
        print("Scores must be numbers!")


def update_student():
    """Function 3: Update student information"""
    print("\n--- UPDATE STUDENT ---")
    student_id = input("Enter Student ID to update: ").strip()
    
    student = next((s for s in students if s['id'] == student_id), None)
    if not student:
        print("Student not found!")
        return
    
    print(f"Current student: {student['name']} - Average: {student['average']}")
    
    try:
        math = float(input(f"New Math score [{student['math']}]: ") or student['math'])
        physics = float(input(f"New Physics score [{student['physics']}]: ") or student['physics'])
        chemistry = float(input(f"New Chemistry score [{student['chemistry']}]: ") or student['chemistry'])
        
        if not (0 <= math <= 10 and 0 <= physics <= 10 and 0 <= chemistry <= 10):
            print("Scores must be between 0 and 10!")
            return
        
        student['math'] = math
        student['physics'] = physics
        student['chemistry'] = chemistry
        student['average'] = calculate_average(math, physics, chemistry)
        student['grade'] = classify_grade(student['average'])
        
        print(f"Updated - New average: {student['average']} - {student['grade']}")
        
    except ValueError:
        print("Scores must be numbers!")


def delete_student():
    """Function 4: Delete student"""
    print("\n--- DELETE STUDENT ---")
    student_id = input("Enter Student ID to delete: ").strip()
    
    student = next((s for s in students if s['id'] == student_id), None)
    if not student:
        print("Student not found!")
        return
    
    confirm = input(f"Are you sure you want to delete {student['name']}? (y/n): ").lower()
    if confirm == 'y':
        students.remove(student)
        print(f"Deleted student {student['name']}")
    else:
        print("Delete operation cancelled")


def search_student():
    """Function 5: Search student"""
    print("\n--- SEARCH STUDENT ---")
    keyword = input("Enter Name or ID: ").strip().lower()
    
    results = [s for s in students 
               if keyword in s['name'].lower() or keyword in s['id'].lower()]
    
    if not results:
        print("No student found!")
        return
    
    print(f"\nFound {len(results)} student(s):")
    print("="*80)
    print(f"{'ID':<10} {'Name':<20} {'Average':<6} {'Grade':<15}")
    print("="*80)
    for student in results:
        print(f"{student['id']:<10} {student['name']:<20} {student['average']:<6.2f} {student['grade']:<15}")


def sort_students():
    """Function 6: Sort student list"""
    print("\n--- SORT LIST ---")
    print("1. Sort by Average (descending)")
    print("2. Sort by Name (A-Z)")
    
    choice = input("Choose sorting method (1/2): ").strip()
    
    if choice == '1':
        students.sort(key=lambda x: x['average'], reverse=True)
        print("Sorted by Average (descending)")
    elif choice == '2':
        students.sort(key=lambda x: x['name'])
        print("Sorted by Name (A-Z)")
    else:
        print("Invalid choice!")


def statistics():
    """Function 7: Statistics by grade"""
    if not students:
        print("\nList is empty!")
        return
    
    stats = {'Excellent': 0, 'Good': 0, 'Average': 0, 'Poor': 0}
    
    for student in students:
        stats[student['grade']] += 1
    
    print("\n--- GRADE STATISTICS ---")
    print(f"Excellent:  {stats['Excellent']} students")
    print(f"Good:       {stats['Good']} students")
    print(f"Average:    {stats['Average']} students")
    print(f"Poor:       {stats['Poor']} students")
    print(f"Total:      {len(students)} students")
    
    return stats


def draw_chart():
    """Function 8: Draw statistics chart"""
    if not students:
        print("\nList is empty!")
        return
    
    stats = statistics()
    
    labels = [k for k, v in stats.items() if v > 0]
    sizes = [v for v in stats.values() if v > 0]
    colors = ['#4CAF50', '#2196F3', '#FFC107', '#F44336']
    
    plt.figure(figsize=(8, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
    plt.title('Grade Distribution Statistics', fontsize=14, fontweight='bold')
    plt.axis('equal')
    plt.show()


def save_to_csv():
    """Function 9: Save to CSV file"""
    if not students:
        print("\nNo data to save!")
        return
    
    with open('data.csv', 'w', encoding='utf-8', newline='') as f:
        fieldnames = ['id', 'name', 'math', 'physics', 'chemistry', 'average', 'grade']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerows(students)
    
    print(f"\nSaved {len(students)} students to data.csv")


def menu():
    """Main menu"""
    load_data()
    
    while True:
        print("\n" + "="*50)
        print("    STUDENT MANAGEMENT SYSTEM")
        print("="*50)
        print("1.  Display student list")
        print("2.  Add new student")
        print("3.  Update student information")
        print("4.  Delete student")
        print("5.  Search student")
        print("6.  Sort student list")
        print("7.  Grade statistics")
        print("8.  Draw statistics chart")
        print("9.  Save to CSV file")
        print("10. Exit")
        print("="*50)
        
        choice = input("Choose function (1-10): ").strip()
        
        if choice == '1':
            display_students()
        elif choice == '2':
            add_student()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            search_student()
        elif choice == '6':
            sort_students()
        elif choice == '7':
            statistics()
        elif choice == '8':
            draw_chart()
        elif choice == '9':
            save_to_csv()
        elif choice == '10':
            save_to_csv()
            print("\nThank you for using the program!")
            break
        else:
            print("\nInvalid choice!")


if __name__ == "__main__":
    menu()
