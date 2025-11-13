#

usl = """
1. Показать всех учеников и предметы оценки.
2. Добавить ученика.
3. Добавить предмет ученику.
4. Добавить оценку по предмету ученика.
5. Показать все предметы и оценки ученика.
6. Посчитать среднюю оценку ученика.
7. Посчитать общую среднюю оценку по всему классу.
8. Выйти.
"""

students = {
    "Алия": {
        "Математика": [5, 4],
        "История": [3, 4]
    },
    "Малика": {
        "Физика": [4, 5],
        "Литература": [5]
    }
}

print(usl)

while True:
    req = input("Выберите действие (1-8): ")

    # 1. Показать всех учеников и оценки
    if req == '1':
        for name, subjects in students.items():
            print(f"\n {name}:")
            for subject, grades in subjects.items():
                print(f" {subject}: {grades}")

    # 2. Добавить ученика
    elif req == '2':
        name = input("Введите имя ученика: ").title()
        if name in students:
            print(" Такой ученик уже есть.")
        else:
            students[name] = {}
            print(" Ученик добавлен.")

    # 3. Добавить предмет ученику
    elif req == '3':
        name = input("К какому ученику добавить предмет? ").title()
        if name in students:
            subject = input("Введите название предмета: ").title()
            if subject in students[name]:
                print(" Такой предмет уже есть у ученика.")
            else:
                students[name][subject] = []
                print(" Предмет добавлен.")
        else:
            print(" Такого ученика нет.")

    # 4. Добавить оценку по предмету
    elif req == '4':
        name = input("Имя ученика: ").title()
        if name in students:
            subject = input("Введите предмет: ").title()
            if subject in students[name]:
                try:
                    grade = int(input("Введите оценку (1–5): "))
                    if 1 <= grade <= 5:
                        students[name][subject].append(grade)
                        print(" Оценка добавлена.")
                    else:
                        print(" Оценка должна быть от 1 до 5.")
                except ValueError:
                    print("Введите число.")
            else:
                print(" У ученика нет такого предмета.")
        else:
            print("Такого ученика нет.")

    # 5. Показать все предметы и оценки ученика
    elif req == '5':
        name = input("Введите имя ученика: ").title()
        if name in students:
            print(f"\n Оценки ученика {name}:")
            for subject, grades in students[name].items():
                print(f"  {subject}: {grades}")
        else:
            print(" Такого ученика нет.")

    # 6. Средняя оценка ученика
    elif req == '6':
        name = input("Введите имя ученика: ").title()
        if name in students:
            total, count = 0, 0
            for grades in students[name].values():
                total += sum(grades)
                count += len(grades)
            if count > 0:
                avg = round(total / count, 2)
                print(f" Средняя оценка {name}: {avg}")
            else:
                print("У этого ученика пока нет оценок.")
        else:
            print(" Такого ученика нет.")

    # 7. Общая средняя по классу
    elif req == '7':
        total_sum, total_count = 0, 0
        for subjects in students.values():
            for grades in subjects.values():
                total_sum += sum(grades)
                total_count += len(grades)

        if total_count > 0:
            class_avg = round(total_sum / total_count, 2)
            print(f" Средняя оценка по классу: {class_avg}")
        else:
            print("В журнале пока нет оценок.")

    # 8. Выход
    elif req == '8':
        print(" Выход из журнала. До свидания!")
        break

    else:
        print("Неверный пункт меню. Попробуйте снова.")
