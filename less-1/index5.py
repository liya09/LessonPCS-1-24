cinema = {
    "Аватар": {"цена": 400, "места": 5},
    "Дюна": {"цена": 350, "места": 3},
    "Шрек": {"цена": 200, "места": 10},
    "Чебурашка": {"цена": 250, "места": 4}
}

def cinema_booking(cinema):
    cart = {}
    total = 0

    # Создаем вспомогательный словарь для поиска без учета регистра
    movie_lookup = {name.lower(): name for name in cinema}

    while True:
        movie_input = input("Введите название фильма (или 'стоп' для выхода): ").strip()
        movie_key = movie_input.lower()

        if movie_key == 'стоп':
            break

        if movie_key not in movie_lookup:
            print("Такого фильма нет в кинотеатре")
            continue

        movie = movie_lookup[movie_key]

        if cinema[movie]["места"] == 0:
            print("Билеты на этот фильм закончились")
            continue

        try:
            count = int(input(f"Сколько билетов хотите купить на '{movie}'? "))
        except ValueError:
            print("Введите корректное число")
            continue

        if count > cinema[movie]["места"]:
            print("Недостаточно билетов")
            continue

        price = cinema[movie]["цена"] * count
        total += price
        cinema[movie]["места"] -= count
        cart[movie] = cart.get(movie, 0) + count
        print(f"Куплено {count} билет(ов) на '{movie}' за {price} сом")

    if total > 1000:
        total *= 0.9
        print("Применена скидка 10%")

    if cart:
        print("\nКупленные билеты:")
        for movie, count in cart.items():
            print(f"{movie}: {count} билет(ов)")
        print(f"Итоговая сумма: {total:.2f} сом")
    else:
        print("Вы ничего не купили.")

cinema_booking(cinema)
