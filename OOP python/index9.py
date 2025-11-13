class Tour:
    def __init__(self, id, price, days):
        self.__id = id
        self.__price = price
        self._is_booked = False
        self._client = None
        self._days = days 
    
    @property
    def id(self):
        return self.__id

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value >= 5000:
            self.__price = value
        else:
            print("Цена не может быть ниже 5000 сом")

    def book(self, client):
        if self._is_booked:
            print(f"Тур {self.__id} уже забронирован клиентом {self._client.name}")
            return False
        self._is_booked = True
        self._client = client
        print(f"Тур {self.__id} успешно забронирован клиентом {client.name}")
        return True

    def cancel_booking(self):
        if not self._is_booked:
            print(f"Тур {self.__id} не забронирован")
            return
        print(f"Бронь тура {self.__id} отменена (клиент {self._client.name})")
        self._is_booked = False
        self._client = None

    def info(self):
        status = "Забронирован" if self._is_booked else "Свободен"
        client_name = self._client.name if self._client else "-"
        return f"Тур {self.__id}: {self.__price} сом, {self._days} дней, статус: {status}, клиент: {client_name}"


class Client:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def pay(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            print(f"{self.name}, недостаточно средств для оплаты тура ({amount} сом)")
            return False

    def add_balance(self, amount):
        self.balance += amount
        print(f"{self.name} пополнил баланс на {amount} сом. Текущий баланс: {self.balance} сом")

    def info(self):
        return f"Клиент: {self.name}, баланс: {self.balance} сом"


class Agency:
    def __init__(self, name):
        self.name = name
        self.tours = []
        self._income = 0 

    def add_tour(self, tour):
        self.tours.append(tour)
        print(f"Тур {tour.id} добавлен в агентство {self.name}")

    def show_available_tours(self):
        print(f"\nДоступные туры в агентстве {self.name}:")
        for tour in self.tours:
            if not tour._is_booked:
                print(tour.info())

    def book_tour(self, client, tour_id):
        for tour in self.tours:
            if tour.id == tour_id:
                if tour._is_booked:
                    print(f"Тур {tour_id} уже забронирован.")
                    return
                if client.pay(tour.price):
                    tour.book(client)
                    self._income += tour.price
                return
        print(f"Тур с id {tour_id} не найден.")

    def cancel_all_bookings(self):
        for tour in self.tours:
            if tour._is_booked:
                tour.cancel_booking()
        print("Все брони отменены.")

    def show_status(self):
        print(f"\nСостояние агентства {self.name}:")
        for tour in self.tours:
            print(tour.info())
        print(f"Текущая выручка: {self._income} сом")
