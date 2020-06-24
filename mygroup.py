groupmates = [
    {
        "name": "Петр",
        "surname": "Петров",
        "exams": ["Информатика", "Алгебра", "Геометрия"],
        "marks": [5, 5, 3]
    },
    {
        "name": "Иван",
        "surname": "Иванов",
        "exams": ["История", "География", "Экономика"],
        "marks": [4, 5, 4]
    },
    {
        "name": "Сергей",
        "surname": "Сергеев",
        "exams": ["Философия", "География", "Геометрия"],
        "marks": [2, 2, 2]
    },
    {
        "name": "Кирилл",
        "surname": "Кириллов",
        "exams": ["История", "Алгебра", "Геометрия"],
        "marks": [3, 4, 4]
    },
    {
        "name": "Андрей",
        "surname": "Андреев",
        "exams": ["Геометрия", "География", "Информатика"],
        "marks": [3, 3, 5]
    }
]


def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10),
          u"Экзамены".ljust(45), u"Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15),
              student["surname"].ljust(10), str(student["exams"]).ljust(45),
              str(student["marks"]).ljust(20))


def get_average(marks):
    return sum(marks) / len(marks)


def filter_students(students, average):
    students = filter(lambda x: get_average(x.get('marks')) > average, students)
    print_students(students)


print_students(groupmates)
print('-' * 100)
average_mark = float(input('Введите заданный средний балл: '))
filter_students(groupmates, average_mark)
