journal = {
    "Алиса": {"математика": [5, 4, 5], "русский": [4, 4, 3]},
    "Бек": {"математика": [3, 2, 4], "русский": [5, 5, 5]},
    "Дана": {"математика": [5, 5, 5], "русский": [4, 5, 4]}
}
#Написать функцию analyze_journal(journal), которая:
 #1. Спрашивает у пользователя имя ученика.
 #2. Если такого ученика нет → «Ученика нет в журнале».
 #3. Если есть → выводит:
 #• список всех предметов и среднюю оценку по каждому,
 #• общую среднюю оценку по всем предметам.
 #4. Если средняя оценка ≥ 4.5 → «Отличник»,
#если ≥ 3 → «Хорошист»,
#иначе → «Нужно подтянуть учёбу».

def analyze_journal(journal):
    student_name = input("Имя ученика: ").strip()
    if not student_name:
        print("Имя ученика не введено.")
        return
    if student_name not in journal:
        print("Такого ученика нет в журнале")
        return

    grades_by_subject = journal[student_name]
    
    print(f"\nУспеваемость ученика {student_name}:")
    
    all_grades_sum = 0
    all_grades_count = 0

    for subject, grades in grades_by_subject.items():
        if not grades: 
            avg_subject = 0.0
        else:
            avg_subject = sum(grades) / len(grades)
        print(f"  - {subject}: Средняя оценка = {avg_subject:.2f}")
        
        all_grades_sum += sum(grades)
        all_grades_count += len(grades)
    if all_grades_count == 0:
        overall_avg = 0.0
    else:
        overall_avg = all_grades_sum / all_grades_count

    print(f"\nОбщая средняя оценка по всем предметам: {overall_avg:.2f}")

    if overall_avg >= 4.5:
        print("Отличник")
    elif overall_avg >= 3:
        print("Хорошист")
    else:
        print("Нужно подтянуть учёбу")

journal = {
    "Алиса": {"математика": [5, 4, 5], "русский": [4, 4, 3]},
    "Бек": {"математика": [3, 2, 4], "русский": [5, 5, 5]},
    "Дана": {"математика": [5, 5, 5], "русский": [4, 5, 4]}
}

analyze_journal(journal)