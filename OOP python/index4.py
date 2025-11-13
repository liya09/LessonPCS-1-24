class Flight:
    def __init__(self, number, route, seats_eco, seats_bus, price_eco, price_bus):
        self.number = number
        self.route = route
        self.seats_eco = seats_eco
        self.seats_bus = seats_bus
        self.sold_eco = 0
        self.sold_bus = 0
        self.price_eco = price_eco
        self.price_bus = price_bus

    def sell_ticket(self, seat_class):
        if seat_class == "eco" and self.sold_eco < self.seats_eco:
            self.sold_eco += 1
            print(f"Продан эконом билет на рейс {self.number}")
        elif seat_class == "bus" and self.sold_bus < self.seats_bus:
            self.sold_bus += 1
            print(f"Продан бизнес билет на рейс {self.number}")
        else:
            print("жопу поднял, место потерял!")

    def cancel_ticket(self, seat_class):
        if seat_class == "eco" and self.sold_eco > 0:
            self.sold_eco -= 1
            print("Эконом билет возвращён")
        elif seat_class == "bus" and self.sold_bus > 0:
            self.sold_bus -= 1
            print("Бизнес билет возвращён")

    def revenue(self):
        return self.sold_eco * self.price_eco + self.sold_bus * self.price_bus

    def info(self):
        print(f"Рейс {self.number}: {self.route}")
        print(f"Эко: {self.sold_eco}/{self.seats_eco}  Бизнес: {self.sold_bus}/{self.seats_bus}")
        print(f"Выручка: {self.revenue()} сом.\n")


class Airline:
    def __init__(self, name):
        self.name = name
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)
        print(f"Добавлен рейс {flight.number}")

    def total_revenue(self):
        return sum(f.revenue() for f in self.flights)

    def show_all(self):
        print(f"\nАвиакомпания {self.name}")
        for f in self.flights:
            f.info()
        print(f"Общая выручка: {self.total_revenue()} сом.\n")


class Client:
    def __init__(self, name):
        self.name = name
        self.tickets = []

    def buy_ticket(self, flight, seat_class):
        flight.sell_ticket(seat_class)
        self.tickets.append((flight, seat_class))

    def cancel_ticket(self, flight, seat_class):
        flight.cancel_ticket(seat_class)
        self.tickets = [t for t in self.tickets if not (t[0] == flight and t[1] == seat_class)]

    def info(self):
        print(f"\nКлиент {self.name}")
        if not self.tickets:
            print("Нет билетов.")
        else:
            for flight, cls in self.tickets:
                print(f"{flight.number} ({flight.route}) — {cls}")


if __name__ == "__main__":
    airline = Airline("SkyWings")

    f1 = Flight("SW101", "Манас → Германия", 3, 2, 5000, 15000)
    f2 = Flight("SW202", "Бишкек → Япония", 2, 1, 7000, 20000)

    airline.add_flight(f1)
    airline.add_flight(f2)

    Lolu = Client("Лолу")
    Pepe = Client("Пепе")

    Lolu.buy_ticket(f1, "eco")
    Pepe.buy_ticket(f1, "bus")
    Lolu.buy_ticket(f2, "eco")

    Pepe.cancel_ticket(f1, "bus")

    airline.show_all()
    Lolu.info()
    Pepe.info()
