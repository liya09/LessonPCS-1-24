#Напиши программу, которая:
#1. Добавляет заказ (блюдо, количество, цена)
#2. Показывает все заказы
#3. Ищет заказы по названию блюда
#4. Подсчитывает общую выручку
#5. Завершает работу по выбору пользователя
#Все данные сохраняются в файле orders.txt.

while True:
     print("""
      1. Добавляет заказ (блюдо, количество, цена)
      2. Показывает все заказы
      3. Ишет заказы по название блюда
      4. Подсчитывает  общую выручку
      5. Завершает работу по выбору пользователя""")
         
     choice = input("Выберите дейтвие: ")
     if choice == '1':
        dish = input("Назовите блюдо: ")
        quantity = int(input("Сколько штук:"))
        price = float(input("Цена:")) 
        total = quantity * price
        with open('orders.txt', 'a', encoding="utf-8") as file:
            file.write(f"{dish},{quantity},{price},{total}\n")
            print(" Заказ добавлен!")

     elif choice == '2':
        with open('orders.txt', 'r', encoding='utf-8') as file:
         content = file.read()
         print(" Все заказы:\n", content)
     elif choice == '3':
         search = input("Введите название блюда: ")
         found = False
         with open('orders.txt', 'r', encoding='utf-8') as file:
          for line in file:
           if search.lower() in line.lower():
              print("Найдено,", line.strip())
              found = True
          else:
              print("Нет такой блюда")
     elif choice == '4':
        total_income = 0
        with open('orders.txt', 'r', encoding='utf-8') as file:
            
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 4:
                    total_income += float(parts[3])
        print(f" Общая сумма: {total_income} сом")
     elif choice == '5':
        print(" Программа завершена.")
        break
     else:
        print("Неверный выбор, повтори еще раз.")