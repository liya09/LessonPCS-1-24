class Person:
    def __init__(self, name, age, balance=0):
        self.name = name
        self.age = age
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount


    def withdraw(self, amount):   # — снятие со счёта.
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.name} снятие со счёта {amount}")
        else:
            print("Недостаточно средств!")

    def info(self):
        return f"{self.name}, {self.age} лет, баланс: {self.balance} сом."


class Bank:
    def __init__(self, name):
        self.name = name
        self.clients = []
        self.products = []  # список всех операций
        self.income = 0  #доход

    def add_client(self, client):
        self.clients.append(client)
        print(f"Клиент {client.name} добавлен")

    def add_product(self, product):
        self.products.append(product)
        print(f"Продукт добавлен")

    def add_income(self, amount):
        self.income += amount 

    def calculate_total_profit(self):
        return self.income
    
    def show_clients(self):
        print("Наши клиенты:")
        for c in self.clients:
            print(f".      {c.info()}")


    def show_products(self):
        print("Наши продукты:")
        for c in self.products:
            print(f".      {c.info()}")


class BankProduct:
    def __init__ (self,client,amount,interest_rate,term_months):
        self.client = client
        self.amount = amount
        self.interest_rate = interest_rate
        self.term_months = term_months

    def calculate_interest(self):
        return self.amount*(self.interest_rate/100)*(self.term_months/12)


    def info(self):
       print(f"{self.client.name},сумма: {self.amount}сом , ставка:{self.interest_rate}% , срок: {self.term_months} мес")


class Deposit(BankProduct):
    def __init__(self, client, amount, interest_rate, term_months):
        super().__init__(client, amount, interest_rate, term_months)
        client.balance -= amount
        print(f"Вклад открыт {amount} для {client.name}. Баланс: {client.balance}")

    def close_deposit(self):
        if self.is_closed:
            print("Вклад уже закрыт.")
            return
        profit = self.amount * self.interest_rate * self.term_months / 12
        total = self.amount + profit
        self.client.balance += total
        self.is_closed = True
        print(f"Вклад закрыт. {self.client.name} получил {total:.2f}. Баланс: {self.client.balance:.2f}")


class Credit(BankProduct):
    def __init__(self, client, amount, interest_rate, term_months):
        super().__init__(client, amount, interest_rate, term_months)
        client.balance += amount
        print(f"Выдан кредит {amount} клиенту {client.name}. Баланс: {client.balance}")

    def monthly_payment(self):
        r = self.interest_rate / 12
        n = self.term_months
        if r == 0:
            return self.amount / n
        return self.amount * (r * (1 + r) ** n) / ((1 + r) ** n - 1)

class Installment:
    def __init__(self, product_name, commission_rate):
        self.product_name = product_name
        self.commission_rate = commission_rate

    def monthly_payment(self, total_price, months):
        total_with_commission = total_price * (1 + self.commission_rate / 100)
        return total_with_commission / months

    def close_installment(self):
        print(f"Рассрочка продукт '{self.product_name}' закрыта.")
