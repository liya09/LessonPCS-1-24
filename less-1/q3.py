def toy_store():
    toys = {
        "мяч": {"цена": 100, "количество": 5},
        "кукла": {"цена": 300, "количество": 2},
        "машинка": {"цена": 250, "количество": 3},
        "пазл": {"цена": 150, "количество": 4},
        "медвежонок": {"цена": 500, "количество": 1}
    }

    cart = {} 
    total = 0

    while True:
        toy_name = input("Введите название игрушки (или стоп для завершения): ").lower()
        if toy_name == "стоп":
            break

        if toy_name not in toys:
            print("Такой игрушки нет.")
            continue

        if toys[toy_name]["количество"] == 0:
            print("Этой игрушки нет в наличии.")
            continue

        try:
            qty = int(input("Сколько хотите купить? "))
        except ValueError:
            print("Введите число.")
            continue

        if qty <= 0:
            print("Количество должно быть больше нуля.")
            continue

        if qty > toys[toy_name]["количество"]:
            print("Недостаточно на складе.")
            continue

       
        toys[toy_name]["количество"] -= qty

      
        if toy_name in cart:
            cart[toy_name]["количество"] += qty
        else:
            cart[toy_name] = {"цена": toys[toy_name]["цена"], "количество": qty}

       
        total += toys[toy_name]["цена"] * qty
        print(f"Добавлено в корзину: {toy_name} x{qty}. Текущая сумма: {total} сом.")

    
    if cart:
        print("Ваши покупки:")
        for name, info in cart.items():
            print(f"{name.capitalize()} — {info['количество']} шт. по {info['цена']} сом.")
        print(f"Общая сумма: {total} сом.")
    else:
        print("Вы ничего не купили.")

toy_store()
