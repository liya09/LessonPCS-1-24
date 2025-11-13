movies = {
    "Интерстеллар": {"цена": 300, "ограничение": 12},
    "Начало": {"цена": 250, "ограничение": 16},
    "Матрица": {"цена": 200, "ограничение": 16},
    "Аватар": {"цена": 350, "ограничение": 12},
}

tickets = {}

print("Добро пожаловать в систему кинотеатра!")

while True:
    print("\n" + "="*40)
    print("1. Показать список фильмов")
    print("2. Купить билет")
    print("3. Отменить билет")
    print("4. Показать все билеты")
    print("5. Общая выручка")
    print("6. Выйти")
    
    choice = input("Выберите действие: ")
    
    if choice == "1":
    
        print("\n=== ФИЛЬМЫ ===")
        for name, info in movies.items():
            print(f"{name} - {info['цена']} руб. ({info['ограничение']}+)")
    
    elif choice == "2":
        print("\n=== ПОКУПКА БИЛЕТА ===")
        
        for name, info in movies.items():
            print(f"{name} - {info['цена']} руб.")
        
        name = input("Имя зрителя: ").strip()
        
        if name in tickets:
            print("У этого зрителя уже есть билет!")
            continue
        
        try:
            age = int(input("Возраст зрителя: "))
            if age <= 0:
                print(" Неверный возраст!")
                continue
        except:
            print(" Введите число!")
            continue
        
        film = input("Название фильма: ").strip()
        
        if film not in movies:
            print("Фильм не найден!")
            continue
        
        if age < movies[film]["ограничение"]:
            print(f" Возрастное ограничение: {movies[film]['ограничение']}+")
            continue
        
        tickets[name] = {
            "фильм": film,
            "цена": movies[film]["цена"],
            "возраст": age
        }
        print("Билет куплен!")
    
    elif choice == "3":
        print("\n=== ОТМЕНА БИЛЕТА ===")
        name = input("Имя зрителя: ").strip()
        
        if name in tickets:
            film = tickets[name]["фильм"]
            del tickets[name]
            print(f"Билет {name} на '{film}' отменен")
        else:
            print("Билет не найден!")
    
    elif choice == "4":

        print("\n=== КУПЛЕННЫЕ БИЛЕТЫ ===")
        
        if not tickets:
            print("Билетов нет")
        else:
            for name, info in tickets.items():
                print(f"{name} ({info['возраст']} лет) - {info['фильм']} - {info['цена']} руб.")
    
    elif choice == "5":
        print("\n=== ВЫРУЧКА ===")
        total = sum(info["цена"] for info in tickets.values())
        print(f"Продано билетов: {len(tickets)}")
        print(f"Общая выручка: {total} руб.")
    
    elif choice == "6":
        print("До свидания!")
        break
    
    else:
        print("Неверный выбор!")