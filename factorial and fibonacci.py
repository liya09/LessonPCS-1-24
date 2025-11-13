def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def main():
    print("Алгоритмические задачи:")
    print("1. Вычисление факториала")
    print("2. Вычисление числа Фибоначчи")
    
    choice = input("Выберите задачу (1 или 2): ")

    if choice not in ["1", "2"]:
        print("Неверный выбор.")
        return

    try:
        num = int(input("Введите целое неотрицательное число: "))
        if num < 0:
            print("Число должно быть неотрицательным.")
            return
    except ValueError:
        print("Ошибка: введите целое число.")
        return

    if choice == "1":
        print(f"Факториал числа {num} равен {factorial(num)}")
    elif choice == "2":
        print(f"{num}-е число Фибоначчи: {fibonacci(num)}")

if __name__ == "__main__":
    main()
