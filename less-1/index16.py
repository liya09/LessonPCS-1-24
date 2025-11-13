tariffs = {
    "1 день": 150,
    "1 неделя": 800,
    "1 месяц": 2500,
    "3 месяца": 6000,
    "VIP-год": 15000
}


class Client:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.balance = 300  # бонус при регистрации
        self.history = []
        self.visits = 0

    def check_balance(self):
        print(f"Баланс: {self.balance} сом")

    def top_up(self, amount):
        self.balance += amount
        print(f"Баланс пополнен на {amount} сом")

    def buy_tariff(self):
        for name, price in tariffs.items():
            print(f"{name} — {price} сом")
        choice = input("Выберите тариф: ").strip()
        if choice in tariffs:
            price = tariffs[choice]
            if self.balance >= price:
                self.balance -= price
                self.history.append(choice)
                cashback = int(price * 0.05)
                self.balance += cashback
                print(f"Куплено '{choice}'. Кэшбэк: {cashback} сом")
            else:
                print("Недостаточно средств")
        else:
            print("Нет такого тарифа")

    def show_history(self):
        if not self.history:
            print("История покупок пуста")
        else:
            print("История покупок:", ", ".join(self.history))

    def get_bonus(self):
        self.visits += 1
        if self.visits % 5 == 0:
            self.balance += 200
            print("Бонус 200 сом за активность!")
        else:
            print(f"Посещений: {self.visits}")


class IronBodyPro:
    def __init__(self):
        self.clients = {}

    def start(self):
        print("Добро пожаловать в Iron Body PRO!")
        name = input("Введите имя: ").strip()
        if name in self.clients:
            password = input("Введите пароль: ").strip()
            client = self.clients[name]
            if password != client.password:
                print("Неверный пароль. Вход не выполнен.")
                return
        else:
            password = input("Придумайте пароль: ").strip()
            client = Client(name, password)
            self.clients[name] = client
            print("Регистрация успешна! Баланс +300 сом")

        while True:
            print("""
1. Проверить баланс
2. Пополнить баланс
3. Купить абонемент
4. Посмотреть историю покупок
5. Получить бонус за посещения
6. Выйти
""")
            choice = input("Выберите пункт: ")
            if choice == "1":
                client.check_balance()
            elif choice == "2":
                amount = int(input("Сумма пополнения: "))
                client.top_up(amount)
            elif choice == "3":
                client.buy_tariff()
            elif choice == "4":
                client.show_history()
            elif choice == "5":
                client.get_bonus()
            elif choice == "6":
                print("Выход из программы")
                break
            else:
                print("Неверный пункт")

club = IronBodyPro()
club.start()
