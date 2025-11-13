def cinema_booking(cinema):
    cart = {}
    total = 0

    while True:
        movie = input("Введите название фильма (или 'стоп' для выхода): ").strip()
        if movie.lower() == 'стоп':
            break
        if movie not in cinema:
            print("Такого фильма нет в кинотеатре")
            continue
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

    print("\nКупленные билеты:")
    for movie, count in cart.items():
        print(f"{movie}: {count} билет(ов)")
    print(f"Итоговая сумма: {total:.2f} сом")

    cinema_booking(cinema)
