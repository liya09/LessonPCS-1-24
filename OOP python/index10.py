class BaseBook:
    def __init__(self, title, author, price):
        self._title = title
        self._author = author
        self.__price = None
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value >= 100:
            raise ValueError("не меньше 100")
        self.__price = value

    @abstractmethod
    def info(self):
        return f"{self._title} {self._author} {self.price}"


class Book(BaseBook):
    def info(self):
        return f"Книга: {self._title} — {self._author}, {self.price} сом"

class EBook(BaseBook):
    def __init__(self, title, author, price, file_size_mb):
        super().__init__(title, author, price)
        self._file_size_mb = file_size_mb

    def info(self):
        return f"Электронная книга: {self._title} — {self._author}, {self.price} сом, файл {self._file_size_mb} МБ"

class AudioBook(BaseBook):
    def __init__(self, title, author, price, duration_min):
        super().__init__(title, author, price)
        self._duration_min = duration_min

    def info(self):
        return f"Аудиокнига: {self._title} — {self._author}, {self.price} сом, {self._duration_min} мин"   

class Inventory:
    def init(self):
        self._books = []

    def add_books(self, *books):
        for book in books:
            if not isinstance(book, BaseBook):
                raise TypeError("только объекты книг")
            self._books.append(book)


    def find_books(self, **filters):
        result = self._books
        for attr, value in filters.items():
            result = [
                book for book in result
                if hasattr(book, f"_{book.__class__.__name__}__price") and attr == "price"
                and book.price == value
                or hasattr(book, f"_{attr}") and getattr(book, f"_{attr}") == value
            ]
        return result


class BookStore:
    def init(self, name):
        self.name = name
        self.inventory = Inventory()
        self.__income = 0

    @property
    def income(self):
        return self.__income

    def sell_book(self, title):
        for book in self.inventory._books:
            if book._title == title:
                self.inventory.remove_book(book)
                self.__income += book.price
                return book
        return None


def show_status(self):
        books_info = [book.info() for book in self.inventory.all_books()]
        return {
            "Магазин": self.name,
            "Доход": self.income,
            "Книги": books_info
            }