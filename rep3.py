#новая тема : Работа с файлами
# mode-режим
# r - read -чтение
# w - write - писать - создание нового файла , старый очищает
# a - append - добавляеть
# x - создание нового файла, но если есть такая то вызов ошибка 
# b - binary - binary - используется вместе с rb и wb
# t - текстовой режим по умолчанию
# open () функции во круг которого все 
# file = open("имя_файла", "режим")
# запись файла
#with open ('data.txt','w', encoding='utf-8') as file:
    #file.write("Урок по теме работе с файлами \n")
    #file.write("Шодияна в шарфе\n")
    #file.write("Абудулвадуд сегодня пришел")

#with open('data.txt', 'r', encoding='utf-8') as file:
  #  content = file.read()
  #  print(content)


#добавить новую запись в data.txt , без удаление старого
#with open('data.txt','a', encoding ='utf-8')as file:
   # file.write('Новая запись\n')






#   задача: "Блокнот"
#   условие: Создай программу, которая:
while True:
    print("""
    1. Добавляет заметку в файл
    2. Показывает все заметки
    3. Ищет заметку по слову 
    4. Заканчивает работу по выбору пользователя""")
    choice = input("Выберите действие: ")
    if choice == "1":
        user_text = input("Что хотите добавить?")
        with open ('bloknot.txt', 'a', encoding='utf-8') as file:
            file.write(f"{user_text}\n")

    elif choice =='2':
        with open('bloknot.txt', "r", encoding="utf-8") as file:
            content = file.read()
            print(content)

    elif choice =='3':
        search = input("Что ищете? ")
        with open('bloknot.txt', "r", encoding="utf-8") as file:
            lines = file.readlines()
            found = False
            for line in lines:
                if search.lower() in line.lower():
                    print(line.strip())
                    found = True
            if not found:
                print("такого нет")
    elif choice == '4':
        break
    else:
            print("выбирайте от 1го до 4х")
            continue

                    