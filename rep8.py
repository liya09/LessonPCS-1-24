
balance = 0
while True:
    print ("""
    1.проверить баланс и показать сколько есть
    2.пополнить баланс и показать сколько стало
    3.снять деньги и показать сколько осталось
    4.выход""")
    choice = input("Выберите действие: ")

    if choice == '1':
        def get_balance():
            return balance

    elif choice == '2':
        def addSom (som):
           pass
    elif choice == '3':
        def minSom (som):
           pass
    elif choice == '4':
        print("\n гуууд баай!")
        break

    else:
        # Неверный ввод
        print("\n Неверный выбор. Пожалуйста, введите число от 1 до 4.")