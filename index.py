def cinema_booking(cinema):
    basket = {}       # корзина с билетами
    total = 0         # итоговая сумма

    while True:
        film = input("Введите название фильма (или 'стоп' для выхода): ")

        if film.lower() == "стоп":
            break

        if film not in cinema:
            print("Такого фильма нет в кинотеатре.")
            continue

        if cinema[film]["места"] == 0:
            print("Билеты на этот фильм закончились.")
            continue

        try:
            count = int(input(f"Сколько билетов вы хотите на '{film}'? "))
        except ValueError:
            print("Введите число.")
            continue

        if count > cinema[film]["места"]:
            print("Недостаточно билетов.")
            continue

        # Покупка
        cinema[film]["места"] -= count
        basket[film] = basket.get(film, 0) + count
        total += cinema[film]["цена"] * count
        print(f"Вы купили {count} билет(ов) на '{film}'.")

    # Проверка на скидку
    if total > 1000:
        discount = total * 0.1
        total -= discount
        print(f"Применена скидка 10%: -{discount} сом.")

    # Итог
    print("\nВаши покупки:")
    for film, count in basket.items():
        print(f"{film}: {count} билет(ов)")
    print(f"Итоговая сумма: {total} сом")