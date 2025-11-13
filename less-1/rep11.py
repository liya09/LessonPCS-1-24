balance = 0.0

while True:
    print("\n1 - Баланс")
    print("2 - Пополнить")
    print("3 - Снять")
    print("4 - Выход")

    choice = input("Ваш выбор: ")

    if choice == '1':
        print("Баланс:", balance)

    elif choice == '2':
        amount = float(input("Сколько пополнить: "))
        balance += amount
        print("Баланс пополнен.")

    elif choice == '3':
        amount = float(input("Сколько снять: "))
        balance -= amount
        print("Деньги сняты.")

    elif choice == '4':
        print("Пока!")
        break

    else:
        print("Неверный выбор.")
