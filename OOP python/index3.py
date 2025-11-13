class BankAccount:
    def __init__(self, owner, pin_code, balance):
        self.__owner = owner
        self.__pin_code = pin_code
        self.__balance = balance

    def get_balance(self, pin):
        if pin == self.__pin_code:
            return self.__balance
        else:
            print("Неверный пин-код")
            return None

    def deposit(self, dengi):
        self.__balance += dengi
        print(f"Счёт пополнен на {dengi} сом. Новый баланс: {self.__balance} сом")

    def withdraw(self, dengi, pin):
        if pin != self.__pin_code:
            print("Неверный пин-код")
            return False
        if dengi > self.__balance:
            print("Недостаточно средств")
            return False
        self.__balance -= dengi
        print(f"Снято {dengi} сом. Остаток: {self.__balance} сом")
        return True

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.__pin_code:
            self.__pin_code = new_pin
            print("Пин-код успешно изменён")
            return True
        else:
            print("Неверный старый пин-код")
            return False

    def info(self):
        print(f"Владелец: {self.__owner}")
        print(f"Баланс: **** сом")  



account = BankAccount("Алия Миллионер", 2009, 5000000)

account.info()
print("Баланс:", account.get_balance(2009))
account.deposit(1000000)
account.withdraw(2000000, 2009)
account.change_pin(2009, 9002)
account.withdraw(1000000, 2009)  
account.withdraw(1000000, 9002)