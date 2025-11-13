#новая тема
#lambda-анонимные функции - функции без имени
#встроенные функции map(), filter()
#импорты


def numMul(x, y):
    return x*y

print(numMul(5,8))

#lambda аргументы выражение
sq = lambda x,y: x*y
print(sq(4,7))


orders = ['Кофе',"Чай","Молоко","Капучино","Коктейл"]
#1. 
#filter (условие ,то к чему это условие)
long_orders = list(filter(lambda order: len(order)>4, orders))
print(long_orders)
#2.Заказы, начинающиеся на букву "К" показывать
k_orders = list(filter(lambda order: order.upper(), orders))
print(k_orders)
#3 Преобразовать все заказы верхний регистр
k_orders = list(map(lambda order: order.upper(),orders))
print(k_orders)

# 1. Вывести только те блюда, где цена выше 150 сом 
# 2. Найти самое дорогое блюдо
# 3. отсортировать блюда по цене (от дешевых к дорогим)
# 4. Проверить, есть ли хоть одно бдюдо, где категории -"десерт"

orders = [
    {"название": "Кофе", "цена": 120,"категорий": "напиток"},
    {"название": "Чай", "цена": 80,"категорий": "напиток"},
    {"название": "Пирог", "цена": 150,"категорий": "десерт"},
    {"название": "Салат", "цена": 200,"категорий": "оснавное"},
]

# 1. Блюда, где цена выше 150 сом
expensive_dishes = [dish for dish in orders if dish["цена"] > 150]
print("Блюда дороже 150 сом:", expensive_dishes)

# 2. Самое дорогое блюдо
most_expensive = max(orders, key=lambda d: d["цена"])
print("Самое дорогое блюдо:", most_expensive)

# 3. Сортировка блюд по цене (от дешевых к дорогим)
sorted_dishes = sorted(orders, key=lambda d: d["цена"])
print(sorted_dishes)

# 4. Есть ли блюдо категории "десерт"
has_dessert = any(dish["категорий"] == "десерт" for dish in orders)
print(has_dessert)