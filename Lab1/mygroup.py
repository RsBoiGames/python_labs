groupmates = [
    {
        "name": "Сергей",
        "surname": "Марюнин",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Иван",
        "surname": "Кузмичов",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [2, 2, 2]
    },
    {
        "name": "Дмитрий",
        "surname": "Ковшов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Алексей",
        "surname": "Кузмичев",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Олег",
        "surname": "Дмитриев",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    }
]

def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))
print_students(groupmates)


def filter_students_by_avg(students, min_avg):
    result = []
    for s in students:
        marks = s.get("marks", [])
        if marks:
            avg = sum(marks) / len(marks)
            if avg > min_avg:
                result.append(s)
    return result

def run_filter_and_print(students):
    raw = input("Введите минимальный средний балл: ").strip().replace(",", ".")
    try:
        min_avg = float(raw)
    except ValueError:
        print("Ошибка ввода: требуется число")
        return

    filtered = filter_students_by_avg(students, min_avg)
    if filtered:
        print_students(filtered)
    else:
        print(f"Студентов со средним баллом выше {min_avg} не найдено.")

def main():
    run_filter_and_print(groupmates)

main()