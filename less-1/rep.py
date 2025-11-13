# ====== Программа "Барбершоп" ======

usl = """
1. Показать список барберов и их услуги.
2. Записаться на услугу к выбранному барберу.
3. Отменить запись по имени клиента.
4. Показать все записи.
5. Найти самого популярного барбера (у кого больше всего клиентов).
6. Выйти.
"""

barbers = {
    "Алия": {"Стрижка": 500, "Бритьё": 300},
    "Давлет": {"Стрижка": 450, "Осветление": 800},
    "Ахмед": {"Модная стрижка": 700, "Укладка": 400}
}

# словарь для хранения записей клиентов
appointments = []  # [{'клиент': 'Имя', 'барбер': 'Алия', 'услуга': 'Стрижка'}]


def show_barbers():
    """Показать всех барберов и их услуги"""
    print("\nНаши барберы и услуги:")
    for barber, services in barbers.items():
        print(f"\nБарбер: {barber}")
        for service, price in services.items():
            print(f"   - {service}: {price} сом")


def make_appointment():
    """Записать клиента к барберу"""
    client = input("Введите ваше имя: ").title()
    show_barbers()
    barber = input("К какому барберу хотите записаться? ").title()

    if barber not in barbers:
        print("Такого барбера нет!")
        return

    print("Услуги этого барбера:")
    for service, price in barbers[barber].items():
        print(f"- {service}: {price} сом")

    service = input("Введите услугу: ").title()

    if service not in barbers[barber]:
        print("Такой услуги нет у этого барбера!")
        return

    appointments.append({"клиент": client, "барбер": barber, "услуга": service})
    print(f"{client} успешно записан к {barber} на услугу '{service}'.")


def cancel_appointment():
    """Отменить запись по имени клиента"""
    name = input("Введите имя клиента для отмены записи: ").title()

    for record in appointments:
        if record["клиент"] == name:
            appointments.remove(record)
            print(f" Запись клиента {name} успешно удалена.")
            return

    print("Такого клиента нет в списке записей.")


def show_appointments():
    """Показать все записи"""
    if not appointments:
        print("Записей пока нет.")
        return

    print("\n Список всех записей:")
    for record in appointments:
        print(f"Клиент: {record['клиент']}, Барбер: {record['барбер']}, Услуга: {record['услуга']}")


def popular_barber():
    """Найти самого популярного барбера"""
    if not appointments:
        print("Пока нет записей, чтобы определить популярного барбера.")
        return

    stats = {}
    for record in appointments:
        barber = record["барбер"]
        stats[barber] = stats.get(barber, 0) + 1

    # находим барбера с максимальным числом клиентов
    top_barber = max(stats, key=stats.get)
    print(f"Самый популярный барбер: {top_barber} ({stats[top_barber]} клиентов)")


# ====== Основной цикл ======
while True:
    print(usl)
    choice = input("Выберите пункт меню (1-6): ")

    if choice == '1':
        show_barbers()
    elif choice == '2':
        make_appointment()
    elif choice == '3':
        cancel_appointment()
    elif choice == '4':
        show_appointments()
    elif choice == '5':
        popular_barber()
    elif choice == '6':
        print("Спасибо, что выбрали наш барбершоп! До встречи!")
        break
    else:
        print("Неверный пункт меню. Попробуйте снова.")
