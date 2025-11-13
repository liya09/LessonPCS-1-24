class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount): # пополнение денег
        if amount <= 0:
            print("Сумма должна быть положительной")
            return
        self.balance += amount
        print(f"{self.owner} пополнил счет на {amount}сом, теперь у вас {self.balance}сом")

    def withdraw(self, amount): # снятие денег
        if amount > self.balance:
            print("Недостаточно средств")
            return
        if amount <= 0:
            print("Сумма должна быть положительной")
            return
        self.balance -= amount
        print(f"{self.owner} сняли со счета {amount}сом, Ваш{self.balance}сом")

    def info(self):
        print(f"Владелец: {self.owner}, Счет: {self.balance}")


class Bank:
    def __init__(self, name):
        self.name = name  # имя банка
        self.accounts = []
   
    def open_account(self, owner): #создаёт новый счёт
        account = BankAccount(owner)
        self.accounts.append(account)
        print(f"Открыт счет на имя {owner} в банке {self.name}")
        return account

    def find_account(self, owner): #возвращает счёт по имени
        for acc in self.accounts:
            if acc.owner == owner:
                print(f"{owner} зарегистрирован в банке")
                return acc
        print(f"Не найден {owner}")
        return None

    def transfer(self, from_owner, to_owner,amount): #перевод между счетами
        from_acc =self.find_account(from_owner)
        to_acc = self.find_account(to_owner)
        if not from_acc or not to_acc:
            print("Перевод невозможен")
            return
        if from_acc.balance < amount:
            print("Недостаточно средств")
            return
        from_acc.withdraw(amount)
        to_acc.deposit(amount)
        print(f"Перевод {amount}сом от {from_owner} к {to_owner} выполнен")

bank = Bank('PKS-Bank')
acc1 = bank.open_account("Aijan")
acc2 = bank.open_account("Denis")
acc1.deposit(3000)
acc2.deposit(19000)
bank.transfer('Denis', 'Aijan', 3200)
acc1.info()
acc2.info()