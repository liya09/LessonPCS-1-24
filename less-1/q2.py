def show_store(store):
    for category, items in store.items():
        print(f"{category}:")
        for name, price in items.items():
            print(f"  {name} — {price} сом.")


def add_to_cart(store, cart):
    product = input("Введите название товара: ").capitalize()
    for category, items in store.items():
        if product in items:
            cart[product] = items[product]
            print(f"{product} добавлен в корзину.")
            return
    print("Такого товара нет в магазине.")


def remove_from_cart(cart):
    if not cart:
        print("Корзина пуста.")
        return
    product = input("Введите название товара для удаления: ").capitalize()
    if product in cart:
        del cart[product]
        print(f"{product} удалён из корзины.")
    else:
        print("Такого товара нет в корзине.")


def show_cart(cart):
    if not cart:
        print("Корзина пуста.")
        return
    print("Корзина")
    total = 0
    for name, price in cart.items():
        print(f"{name} — {price}сом.")
        total += price
    print(f"Итоговая сумма: {total} сом.")


def find_price_extremes(store):
    all_items = {}
    for category, items in store.items():
        all_items.update(items)
    most_expensive = max(all_items, key=all_items.get)
    cheapest = min(all_items, key=all_items.get)
    print(f"Самый дорогой товар: {most_expensive} — {all_items[most_expensive]} сом.")
    print(f"Самый дешёвый товар: {cheapest} — {all_items[cheapest]} сом.")


def count_products(store):
    total_count = sum(len(items) for items in store.values())
    print(f"Всего товаров в магазине: {total_count}")


def supermarket():
    store = {
        "Хлебобулочные": {"Хлеб": 30, "Булочка": 20},
        "Мясо": {"Курица": 150, "Говядина": 700},
        "Напитки": {"Сок": 100, "Вода": 30}
    }

    cart = {}

    while True:
        print("1. Показать все товары по категориям")
        print("2. Добавить товар в корзину")
        print("3. Удалить товар из корзины")
        print("4. Показать корзину")
        print("5. Найти самый дорогой и самый дешёвый товар")
        print("6. Показать количество товаров в магазине")
        print("7. Выйти")

        choice = input("Выберите пункт меню (1-7): ")

        if choice == "1":
            show_store(store)
        elif choice == "2":
            add_to_cart(store, cart)
        elif choice == "3":
            remove_from_cart(cart)
        elif choice == "4":
            show_cart(cart)
        elif choice == "5":
            find_price_extremes(store)
        elif choice == "6":
            count_products(store)
        elif choice == "7":
            print("Выход из программы. До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


supermarket()
