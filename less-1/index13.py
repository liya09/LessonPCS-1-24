# #1
# name = input("Введите имя:")
# print("Привет,<имя>!")
# #2
# age = int(input("Ваш возраст:"))
# print(age+1)
# #3
# length = float(input("Введите длину прямоугольника: "))
# width = float(input("Введите ширину прямоугольника: "))
# area = length * width
# print("Площадь прямоугольника:", area)

# #4
# print(type(45-3.5))
# print(type(45-35))
# print(type(True))
# print(type('hello'))

# #5
# sentence = input("введите предложение:")
# count = len(sentence.replace(" ",""))
# print = ("Количество символов без пробела",count)

# #6
# text = input("Введите текст: ").lower()
# if "python" in text:
#         print("Да это про Python!")
# else:
#     print("Нет, не про Python")

# #7
# name = input("Введите ФИО: ").title()
# print(name)


# #8
# text = input("Введите текст:")
# vowels = "аоэеиыуёюяАоэеиыуёюя" 
# count = 0

# for char in text:
#     if char in vowels:
#         count += 1

# print(f"Количество гласных в строке: {count}")

# #9

# my_string = "Введите текст"
# new_string = my_string.replace(" ", "_")
# print(new_string)

#10
number = int(input("Пишите число:"))
if number % 2 == 0:
    print ("Чётное")
else:
    print ("Нечётное")


# #11
# number = int(input("Введите число: "))

# if number > 0:
#     print("Это положительное число.")
# elif number < 0:
#     print("Это отрицательное число.")
# else:
#     print("Это ноль.")



# #12
# grade = int(input("Введите оценку от 0 до 5: "))
# if grade == 5:
#     print("Отлично")
# elif grade == 4:
#     print("Хорошо")
# elif grade == 3:
#     print("Норм")
# elif grade == 2 or grade == 1:
#     print("Ты тупой")
# else:
#     print("Оценка вне диапазона")

# #14
# password = input("Введите пароль: ")
# if password == "admin123":
#     print("Доступ разрешён")
# else:
#     print("Доступ запрещён")

# #15
# login = input("Введите логин: ")
# password = input("Введите пароль: ")

# if len(password) < 8:
#     print("Внимание! Пароль должен быть не менее 8 символов.")
# else:
#     print("Пароль принят.")

# #16
# change = int(input("Введите сумму долларов которую хотите перевести в соммы: "))
# print(f"{change} долларов равно {change*87} соммов")

# #17
# a = input("Введите первое слово: ").lower()
# b = input("Введите второе слово: ").lower()
# if a == b:
#     print("Совпадают")
# else:
#     print("Разные")

# #18
# num1 = float(input("Введите первое число: "))
# num2 = float(input("Введите второе число: "))
# operation = input("Введите знак операции (+, -, *, /): ")
# if operation == '+':
#     result = num1 + num2
# elif operation == '-':
#     result = num1 - num2
# elif operation == '*':
#     result = num1 * num2
# elif operation == '/':
#     if num2 != 0:
#         result = num1 / num2
#     else:
#         result = "Ошибка: деление на ноль!"
# else:
#     result = "Ошибка: неизвестная операция!"

# print("Результат:", result)
 