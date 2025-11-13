#1
filename = 'spam.txt'
url = 'http://www.python.org'

# Проверка начала и конца строки
print(filename.endswith('.txt'))     # True
print(filename.startswith('spam'))   # True
print(url.startswith('http://'))     # True
print(url.endswith('.org'))          # True

#2
import random

def guess_number():
    secret = random.randint(1, 100)
    attempts = 0

    print("я загадал число от 1 до 100. Попробуйте угадать!")

    while True:
        guess = int(input("Введите число: "))
        attempts += 1

        if guess < secret:
            print("Число должно быть выше ")
        elif guess > secret:
            print("Число должно быть ниже ")
        else:
            print(f"  а ты хорош ! угадал {secret} за {attempts} попыток.")
            break
#3
import random
import string

def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

print(generate_password(12)) 


#4

def is_palindrome(text):
    text = text.lower().replace(" ", "")  
    return text == text[::-1]

print(is_palindrome("Алия"))       
print(is_palindrome("А роза упала на лапу Лилипута"))  
print(is_palindrome("Привет")) 


#5

menu = {
    "Паста": {"цена": 400, "сложность": 3},
    "Стейк": {"цена": 900, "сложность": 5}
}

chefs = {
    "Айбек": {"уровень": 4},
    "Марина": {"уровень": 5}
}

orders = [
    {"гость": "Канат", "блюда": ["Паста", "Стейк"], "повар": "Марина"}
]

# === 1. Добавить блюдо ===
def add_dish(name, price, difficulty):
    menu[name] = {"цена": price, "сложность": difficulty}

# === 2. Зарегистрировать повара ===
def add_chef(name, level):
    chefs[name] = {"уровень": level}

# === 3. Создать заказ ===
def create_order(guest, dishes, chef_name):
    orders.append({"гость": guest, "блюда": dishes, "повар": chef_name})

# === 4. Проверить, может ли повар приготовить ===
def can_chef_cook(chef_name, dish_name):
    return chefs[chef_name]["уровень"] >= menu[dish_name]["сложность"]

# === 5. Подсчитать общую сумму заказа ===
def calc_order_total(order):
    return sum(menu[dish]["цена"] for dish in order["блюда"])

# === Пример использования ===
for order in orders:
    chef = order["повар"]
    guest = order["гость"]

    print(f"\nЗаказ гостя {guest}:")
    total = 0

    for dish in order["блюда"]:
        if can_chef_cook(chef, dish):
            print(f" {chef} готовит {dish}")
        else:
            print(f"{chef} не может приготовить {dish} (сложность выше уровня)")
        total += menu[dish]["цена"]

    print(f" Общая сумма заказа: {total} сом")



