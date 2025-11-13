def car_rental(cars, services):
    import copy

    user_name = input("Введите ваше имя: ")
    try:
        passengers = int(input("Введите количество пассажиров: "))
    except ValueError:
        print("Ошибка: нужно ввести число.")
        return

    orders = []
    cars_available = copy.deepcopy(cars)  # Копируем словарь, чтобы не портить оригинал

    while True:
        category = input("Введите категорию машины (или 'стоп' для завершения): ").strip().capitalize()

        if category.lower() == 'стоп':
            break

        if category not in cars_available:
            print("Такой категории нет. Попробуйте снова.")
            continue

        if cars_available[category]["машины"] <= 0:
            print("Нет свободных машин в этой категории.")
            continue

        if passengers > cars_available[category]["макс_пассажиров"]:
            print("Недостаточно мест для пассажиров.")
            continue

        try:
            days = int(input(f"Сколько дней вы хотите арендовать машину категории {category}? "))
        except ValueError:
            print("Ошибка: нужно ввести число.")
            continue

        service_input = input("Выберите дополнительные услуги через запятую (или оставьте пустым): ").strip()
        selected_services = []
        service_cost = 0

        if service_input:
            selected_services = [s.strip() for s in service_input.split(",")]
            for s in selected_services:
                if s in services:
                    service_cost += services[s] * days
                else:
                    print(f"Услуга '{s}' не найдена и будет пропущена.")

        car_price = cars_available[category]["цена"] * days
        total_price = car_price + service_cost

        # Сохраняем заказ
        orders.append({
            "категория": category,
            "дней": days,
            "услуги": selected_services,
            "стоимость": total_price
        })

        # Уменьшаем количество машин
        cars_available[category]["машины"] -= 1

        print(f"Машина категории {category} успешно арендована на {days} дней.")

    # Расчёт общей суммы
    total_sum = sum(order["стоимость"] for order in orders)
    discount = 0
    if total_sum > 25000:
        discount = total_sum * 0.10
        total_sum *= 0.90

    # Вывод результатов
    print("\n--- Список арендованных машин ---")
    for i, order in enumerate(orders, start=1):
        print(f"{i}. Категория: {order['категория']}, Дней: {order['дней']}, Услуги: {', '.join(order['услуги']) if order['услуги'] else 'Нет'}, Стоимость: {order['стоимость']} сом")

    print("\n--- Итог ---")
    if discount:
        print(f"Применена скидка 10%: -{discount:.2f} сом")
    print(f"Общая сумма к оплате: {total_sum:.2f} сом")

    print("\n--- Остаток машин по категориям ---")
    for category, data in cars_available.items():
        print(f"{category}: {data['машины']} машин(ы) осталось")

cars = {
    "Эконом": {"цена": 2000, "машины": 5, "макс_пассажиров": 4},
    "Комфорт": {"цена": 3500, "машины": 3, "макс_пассажиров": 5},
    "Бизнес": {"цена": 6000, "машины": 2, "макс_пассажиров": 5},
    "Внедорожник": {"цена": 8000, "машины": 2, "макс_пассажиров": 7}
}

services = {
    "Детское кресло": 500,
    "GPS-навигация": 700,
    "Страховка": 1500
}

car_rental(cars, services)