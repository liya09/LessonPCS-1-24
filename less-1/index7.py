# Запрашиваем у пользователя два числа
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

# Запрашиваем знак операции
operation = input("Введите знак операции (+, -, *, /): ")

# Выполняем операцию и выводим результат
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Ошибка: деление на ноль!"
else:
    result = "Ошибка: неизвестная операция!"

print("Результат:", result)
