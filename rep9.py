# Задача: “Банковский счёт”
# Функционал:
balance = 0
def get_balance():
    return balance
def addSom(som):
    global balance
    if som <0:
        print("должно быть больше")
    elif som > 0:
        balance += som
        print(f"Пополнение на {som} сом. Теперь: {balance} сом")
def minSom(som):
    global balance
    if som <0:
        print("должно быть больше")
    elif som > 0:
        balance -= som
        print(f"Сняли {som} сом. Теперь: {balance} сом")
while True:
    print("""
    1. Проверить баланс и показывать сколько есть
    2. Пополнить баланс и показывать сколько стало
    3. Снять деньги и показывать сколько осталось
    4. Выход""")
    choice = input("Выберите действие: ")
    if choice == '1':
        print(f"Ваш баланс: {get_balance()} сом")
    elif choice == '2':
        addSom(float(input("Введите сумму")))
    elif choice == '3':
        minSom(float(input("Введите сумму")))
    elif choice == '4':
        break
    else:
        print("Пишите только числа")
        continue