def todo_list():
    tasks = [] 

    while True: 
        print("1. Посмотреть список дел")
        print("2. Добавить новое дело")
        print("3. Удалить дело по названию")
        print("4. Отметить дело как выполненное")
        print("5. Выйти")

        choice = input("Выберите пункт (1-5): ")

        if choice == "1":
            if not tasks:
                print("Список дел пуст.")
            else:
                print("\nВаши дела:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
        
        elif choice == "2":
            task = input("Введите новое дело: ")
            tasks.append(task)
            print(f"Дело '{task}' добавлено.")
        
        elif choice == "3":
            task = input("Введите дело для удаления: ")
            if task in tasks:
                tasks.remove(task)
                print(f"Дело '{task}' удалено.")
            else:
                print("Такого дела нет.")
        
        elif choice == "4":
            task = input("Введите дело, которое выполнено: ")
            if task in tasks:
                tasks[tasks.index(task)] = f"{task}  (выполнено)"
                print(f"Дело '{task}' отмечено как выполненное.")
            else:
                print("Такого дела нет.")
        
        elif choice == "5":
            print("Выход из программы. До свидания!")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

todo_list()
