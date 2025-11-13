# ====== ФУНКЦИИ ======

# функция без аргументов
def HelloPrint():
    return 'Hello world'

print(HelloPrint())


# функция с аргументами
def HelloPrint(name):
    return f'Добро пожаловать, вождь {name}!'

print(HelloPrint("Шах"))


# ====== КАЛЬКУЛЯТОР ======
def calculator(num1, num2, symbol):
    if symbol == '+':
        return num1 + num2
    elif symbol == '-':
        return num1 - num2
    elif symbol == '*':
        return num1 * num2
    elif symbol == '/':
        try:
            return num1 / num2
        except ZeroDivisionError:
            return "Ошибка: на ноль делить нельзя"
    elif symbol == '//':
        return num1 // num2
    elif symbol == '**':
        return num1 ** num2
    elif symbol == '%':
        return num1 % num2
    else:
        return "Введите только + - * / // ** %"


# Пример использования
# a = int(input('первое: '))
# b = int(input("второе: "))
# c = input("символ: ")
# print(calculator(a, b, c))


# ====== ЗАКАЗ В РЕСТОРАНЕ ======
def order(menuDef):
    total = 0               # итоговая сумма
    ordered = []            # список заказанных блюд

    while True:
        item = input("Что закажете? (или 'стоп' для выхода): ").lower()

        if item == 'стоп':
            break
        elif item in menuDef:
            total += menuDef[item]
            ordered.append(item)
            print(f"{item} добавлено в заказ ({menuDef[item]} сом).")
        else:
            print("Такого блюда нет!")

    print("\nВаш заказ:", ordered)
    print("Итоговая сумма:", total, "сом")

menuList = {
    "бургер": 300,
    "пицца": 400,
    "салат": 200,
    "суп": 180,
    "чай": 30
}
# order(menuList)


# ====== БИБЛИОТЕКА ======
def library_system(library):
    taken_books = []  # список взятых книг

    while True:
        book = input("Какую книгу хотите взять? (или 'стоп' для выхода): ")

        if book == "стоп":
            break
        elif book not in library:
            print("Такой книги нет.")
        elif library[book] == 0:
            print("Эта книга закончилась.")
        else:
            library[book] -= 1
            taken_books.append(book)
            print(f"Вы взяли: {book}")
            print("Остаток книг в библиотеке:", library)

    print("\nВаш список книг:", taken_books)


library = {
    "Гарри Поттер": 3,
    "Властелин колец": 2,
    "Мастер и Маргарита": 1,
    "Три мушкетёра": 2
}

# library_system(library)
