class BankAccount:
    def __init__(self, owner ,balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Сумма должна быть положительный")
            return
        self.balance += amount
        print(f"{self.owner} пополнит счет на {amount}сом, теперь у ваc {self.balance}сом")

    def withdraw(self, amount):
        if amount > self.balance:
            print("не достатоно средств")
            return
        if amount <= 0:
            print("Сумма должна быть положительный")
            return
        self.balance -= amount
        print(f"{self.owner} снял со счет {amount}сом, теперь у ваc {self.balance}сом")
        
    def info(self):
        return f"Владелец: {self.owner}, Ваш баланс: {self.balance}" 

class Bank:
    def __init__(self,name):
        self.name = name
        self.accounts=[]

    def open_account(self, owner):
        account = BankAccount(owner)
        self.accounts.append(account)
        print(f"Открыть новый счет для{owner} в банке.{self.name}")
        return account

    def find_account(self,owner):
        for acc in self.accounts:
            if acc.owner == owner:
                print(f"{owner}зарегистрован в банке" )
                return acc
        print(f"Счет на имя:{owner} не найден")
        return None 

    def transfer(self,from_owner,to_owner,amount):    #перевод денег между 
        from_acc = self.find_account(from_owner)
        to_acc = self.find_account(to_owner)
        if not from_acc or not to_acc:
            print("Перевод невозможен")
            return
        if from_acc.balance < amount:
            print("Недостаточно средств")
            return 
        from_acc.withdraw(amount)
        to_acc.deposit(amount)
        print(f"Перевод {amount} сом от {from_owner} к {to_owner} выполнен")
        

bank = Bank('PKS-Bank')
acc1 = bank.open_account("Шоди")
acc2 = bank.open_account("Абай")
acc1.deposit(3000)
acc2.deposit(19000)
bank.transfer('Абай', 'Шоди', 3200)
acc1.info()
acc2.info()
