concerts = {
"Рок-фестиваль": {"цена": 4000, "билеты": 50, "возраст": 16},
"Джазовый вечер": {"цена": 3000, "билеты": 40, "возраст": 12},
"Классика в зале": {"цена": 2500, "билеты": 30, "возраст": 0},
"Поп-шоу": {"цена": 5000, "билеты": 20, "возраст": 10}
}

services = {
"VIP-место": 2000,
"Сувенир": 1000,
"Backstage-проход": 5000
}
def concert_booking(concerts, services):
    # Спросим имя и возраст
    name = input("Введите ваше имя: ")
    try:
        age = int(input("Введите ваш возраст: "))
    except ValueError:
        print("Возраст должен быть числом.")
        return

    total_orders = []
    total_cost = 0

    while True:
        print("\nДоступные концерты:")
        for concert, info in concerts.items():
            print(f"- {concert} | Цена: {info['цена']} | Остаток билетов: {info['билеты']} | Возрастное ограничение: {info['возраст']}+")

        choice = input("\nВведите название концерта, который хотите посетить (или 'стоп' для завершения): ")
        if choice.lower() == "стоп":
            break

        if choice not in concerts:
            print("Такого концерта нет. Попробуйте снова.")
            continue

        concert_info = concerts[choice]

        if age < concert_info["возраст"]:
            print(f"Вам не хватает возраста для посещения этого концерта (нужно {concert_info['возраст']}+).")
            continue

        try:
            ticket_count = int(input("Сколько билетов вы хотите купить? "))
        except ValueError:
            print("Введите корректное число билетов.")
            continue

        if ticket_count <= 0:
            print("Количество билетов должно быть больше 0.")
            continue

        if ticket_count > concert_info["билеты"]:
            print(f"Недостаточно билетов. Осталось только {concert_info['билеты']} штук.")
            continue

        # Выбор дополнительных услуг
        print("\nДоступные услуги:")
        for service, price in services.items():
            print(f"- {service}: {price} сом")

        service_input = input("Введите дополнительные услуги через запятую (или оставьте пустым, если не нужно): ").strip()
        chosen_services = [s.strip() for s in service_input.split(",") if s.strip()]
        invalid_services = [s for s in chosen_services if s not in services]

        if invalid_services:
            print(f"Некорректные услуги: {', '.join(invalid_services)}. Они будут проигнорированы.")
            chosen_services = [s for s in chosen_services if s in services]

        # Расчёт стоимости
        ticket_price = concert_info["цена"]
        services_price = sum(services[s] for s in chosen_services)
        total_price = (ticket_price + services_price) * ticket_count

        # Обновляем количество билетов
        concerts[choice]["билеты"] -= ticket_count

        # Сохраняем заказ
        total_orders.append({
            "концерт": choice,
            "билеты": ticket_count,
            "услуги": chosen_services,
            "сумма": total_price
        })

        total_cost += total_price
        print(f"Заказ добавлен: {choice} — {ticket_count} билетов, услуги: {', '.join(chosen_services) if chosen_services else 'нет'}, сумма: {total_price} сом.")

    print("\n--- Итог ---")
    if not total_orders:
        print("Вы не сделали ни одного заказа.")
        return

    for i, order in enumerate(total_orders, 1):
        print(f"{i}. Концерт: {order['концерт']}")
        print(f"   Билеты: {order['билеты']}")
        print(f"   Услуги: {', '.join(order['услуги']) if order['услуги'] else 'нет'}")
        print(f"   Сумма: {order['сумма']} сом")

    if total_cost > 50000:
        discount = int(total_cost * 0.25)
        final_price = total_cost - discount
        print(f"\nОбщая сумма: {total_cost} сом")
        print(f"Скидка 25%: -{discount} сом")
        print(f"Итого к оплате: {final_price} сом")
    else:
        print(f"\nИтого к оплате: {total_cost} сом")

    print("\nОставшиеся билеты по концертам:")
    for concert, info in concerts.items():
        print(f"- {concert}: {info['билеты']} билетов")
# Пример запуска
concerts = {
    "Рок-фестиваль": {"цена": 4000, "билеты": 50, "возраст": 16},
    "Джазовый вечер": {"цена": 3000, "билеты": 40, "возраст": 12},
    "Классика в зале": {"цена": 2500, "билеты": 30, "возраст": 0},
    "Поп-шоу": {"цена": 5000, "билеты": 20, "возраст": 10}
}

services = {
    "VIP-место": 2000,
    "Сувенир": 1000,
    "Backstage-проход": 5000
}

# Запуск функции
concert_booking(concerts, services)
