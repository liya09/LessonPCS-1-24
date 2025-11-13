tarif = {
    '3 часа': 150,
    '5 часа': 220,
    '7 часа': 330
}

clients = {
    "Agent007": {'password':'qwerty','balance':300 }
}

def comp_club():
    print("Добро пожаловать в Комп-Клуб!")
    played = input("Вы уже играли в нашу игру? : ").lower()

    if played == "нет":
        login = input("Придумайте логин: ")
        password = input("Придумайте пароль: ")
        clients[login] = {'password': password, 'balance': 0}
        print(f"Регистрация успешна! Ваш логин: {login}")
    elif played == "да":
        login = input("Введите ваш логин: ")
        if login in clients:
            password = input("Введите пароль: ")
            if password != clients[login]['password']:
                print("Неверный пароль")
                return
            print("Добро пожаловать в бойцовский клуб!")
        else:
            print("Такого игрока нет. Зарегистрируйтесь сначала.")
            return
    else:
        print("Введите 'да' или 'нет'.")
        return

    while True:
        print("\n1. Проверить баланс\n2. Пополнить баланс\n3. Купить тариф\n4. Выйти")
        choice = input("Выберите пункт: ")

        if choice == "1":
            print("Баланс:", clients[login]['balance'], "сом")
        elif choice == "2":
            amount = int(input("Введите сумму: "))
            clients[login]['balance'] += amount
            print("Баланс пополнен. Текущий:", clients[login]['balance'])
        elif choice == "3":
            print("Тарифы:")
            for t, price in tarif.items():
                print(f"{t} — {price} сом")
            chosen = input("Выберите тариф: ")
            if chosen in tarif:
                if clients[login]['balance'] >= tarif[chosen]:
                    clients[login]['balance'] -= tarif[chosen]
                    print(f"Вы купили '{chosen}'. Остаток: {clients[login]['balance']}")
                else:
                    print("Недостаточно средств")
            else:
                print("Нет такого тарифа")
        elif choice == "4":
            print("Выход")
            break
        else:
            print("Неверный выбор")

comp_club()
