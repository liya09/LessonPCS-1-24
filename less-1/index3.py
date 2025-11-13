flights = {
    "Москва": {"цена": 8000, "места": 5},
    "Стамбул": {"цена": 12000, "места": 3},
    "Париж": {"цена": 15000, "места": 2},
    "Бишкек": {"цена": 5000, "места": 6}
}

def airline_booking(flights):
    cart = {}
    total = 0

    # Вспомогательный словарь для поиска без учета регистра
    city_lookup = {city.lower(): city for city in flights}

    while True:
        city_input = input("Введите город (или 'стоп' для выхода): ").strip()
        city_key = city_input.lower()

        if city_key == 'стоп':
            break

        if city_key not in city_lookup:
            print("Такого направления нет")
            continue

        city = city_lookup[city_key]

        if flights[city]['места'] == 0:
            print("Билеты закончились")
            continue

        try:
            count = int(input(f"Сколько билетов хотите купить в {city}? "))
        except ValueError:
            print("Введите корректное число")
            continue

        if count > flights[city]['места']:
            print(f"Недостаточно мест. Осталось: {flights[city]['места']}")
            continue

        price = flights[city]['цена'] * count
        total += price
        flights[city]['места'] -= count
        cart[city] = cart.get(city, 0) + count
        print(f"Куплено {count} билет(ов) в {city} за {price} сом")

    if total > 20000:
        total *= 0.8
        print("Применена скидка 20%")

    print("\nКупленные билеты:")
    for city, count in cart.items():
        print(f"{city}: {count} билет(ов)")
    print(f"Общая стоимость: {total:.2f} сом")

    print("\nОстаток мест по направлениям:")
    for city, info in flights.items():
        print(f"{city}: {info['места']} мест(а)")

airline_booking(flights)
