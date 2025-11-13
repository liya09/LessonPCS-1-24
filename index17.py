# Задача: Система управление колледжем
# Ты пишешь программу, которая помагает колледжу управлять студентами, предметами и оценками.
# Система должна уметь: 
# 1. Регистрировать студентов (имя, группа, возраст).
# 2. Добавлять предметы (название, преподаветель )
# 3. Назначать оценки студентам по предметам.
# 4. Вычислять средний балл каждого студента.
# 5. Показывать топ студентов группы.
# 6. Проверять кто подлежит отчисление (если средний балл < 50)


def add_students(students):
    name = input("Введите имя студента: ").title().strip()
    group = input("Введите группу: ").upper()
    try:
      age = int(input("Введите возраст: "))
    except ValueError:
        print("Вводите только числа")
        return
    if name in students:
        print("такой уже существует")
        return
    students[name] = {"группа": group, "возраст": age, "оценки": {}}
    print(f"Студент {name} зарегистрирован.")

def add_subject(subject):
    name = input("Введите название предмета: ")
    teacher = input("Введите имя преподавателя: ")
    if name in subjects:
        print("Такой предмет уже есть")
        return
    subjects[name] = teacher
    print(f" Предмет '{name}' добавлен (преподаватель: {teacher}).")

def add_mark(students,subjects):
    name = input("Введите имя студента: ").title().strip()
    if name not in students:
        print("Студент не найден")
        return
    subject = input("Введите предмет: ").title().strip()
    if subject not in subjects:
        print("Предмет не найден.")
        return
    try:
        mark = int(input("Введите оценку (0-100):"))
    except ValueError:
        print("Ошибка! введите только число")
        return
    if mark < 0 or mark > 100:
        print("оценка должна быть от 0 до 100")
        return
    students[name]["оценки"][subjects] = mark
    print(f"{name} получил {mark} по предмету")

    
def show_student_info(students):
    pass

def calculate_average(markes):
    pass

def show_top_students(students):
    pass

def expel_students(students):
    pass


students = {}
subject = {}
while True:
    print("""
    1. Регистрировать студентов (имя,группа,возраст).
    2. Добавлять предметы(название,группа,предподаватель).
    3. Назначать оценки студентам по предметам.
    4. Вычислять средний балл каждого студента.
    5. Показывать топ студентов группы.
    6. Проверять кто подлежит отчисление (если средний балл < 50)""")
    choice = input("Выберите пункт из меню:")

    if choice == '1':
        add_students(students)
    elif choice == '2':
        add_subject(subjects)
    elif choice == '3':
        add_mark(students, subjects)
    elif choice == '4':
        show_student_info(students)
    elif choice == '5':
        show_top_students(students)
    elif choice == '6':
        expel_students(students)
    elif choice == '0':
        break
    else:
        print("Ошибка,Выберите пункт из меню")