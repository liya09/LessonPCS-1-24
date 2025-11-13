products = [
    {"название": "Футболка", "цена": 800, "размер": "M", "категория": "мужская"},
    {"название": "Платье", "цена": 1500, "размер": "L", "категория": "женская"},
    {"название": "Куртка", "цена": 3500, "размер": "XL", "категория": "мужская"},
    {"название": "Шорты", "цена": 1200, "размер": "S", "категория": "детская"},
    {"название": "Джинсы", "цена": 2200, "размер": "L", "категория": "мужская"},
]

def show_products():
    if not products:
        print("Список товаров пуст.")
    for i, product in enumerate(products, 1):
        print(f"{i}. {product['название']} - {product['цена']} руб, размер: {product['размер']}, категория: {product['категория']}")

def add_product():
    name = input("Введите название товара: ")
    try:
        price = int(input("Введите цену товара: "))
    except ValueError:
        print("Цена должна быть числом.")
        return
    size = input("Введите размер товара: ")
    category = input("Введите категорию товара: ")
    products.append({"название": name, "цена": price, "размер": size, "категория": category})
    print("Товар добавлен.")

def find_by_category():
    cat = input("Введите категорию для поиска: ")
    filtered = [p for p in products if p["категория"].lower() == cat.lower()]
    if filtered:
        for product in filtered:
            print(f"{product['название']} - {product['цена']} руб, размер: {product['размер']}")
    else:
        print("Товары в этой категории не найдены.")

def find_most_expensive():
    if not products:
        print("Список товаров пуст.")
        return
    most_expensive = max(products, key=lambda x: x["цена"])
    print(f"Самый дорогой товар: {most_expensive['название']} - {most_expensive['цена']} руб")

def filter_cheaper_than():
    try:
        price_limit = int(input("Введите максимальную цену: "))
    except ValueError:
        print("Цена должна быть числом.")
        return
    filtered = [p for p in products if p["цена"] < price_limit]
    if filtered:
        for product in filtered:
            print(f"{product['название']} - {product['цена']} руб")
    else:
        print("Нет товаров дешевле заданной цены.")

def increase_prices():
    for product in products:
        old_price = product["цена"]
        product["цена"] = int(old_price * 1.05)
    print("Цены всех товаров подняты на 5%.")

def main():
    while True:
        print("\nМеню:")
        print("1. Показать все товары")
        print("2. Добавить новый товар")
        print("3. Найти товары по категории")
        print("4. Найти самый дорогой товар")
        print("5. Отфильтровать товары дешевле заданной цены")
        print("6. Поднять цену всем товарам на 5%")
        print("7. Выйти из программы")
        
        choice = input("Выберите пункт меню: ")
        
        if choice == '1':
            show_products()
        elif choice == '2':
            add_product()
        elif choice == '3':
            find_by_category()
        elif choice == '4':
            find_most_expensive()
        elif choice == '5':
            filter_cheaper_than()
        elif choice == '6':
            increase_prices()
        elif choice == '7':
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")

if __name__ == "__main__":
    main()
