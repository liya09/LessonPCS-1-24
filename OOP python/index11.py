class Ingredient:
    def init(self, name, price_per_gram):
        self._name = name
        self._price_per_gram = price_per_gram

    def cost(self, weight):
        return weight * self._price_per_gram


class Dish:
    def init(self, name, base_price, **ingredients):
        self._name = name
        self._ingredients = ingredients  
        self._base_price = base_price

    def total_cost(self):
        total = self._base_price
        for ing, grams in self._ingredients.items():
            total += ing.cost(grams)
        return round(total, 2)

    def info(self):
        return f"Блюдо: {self._name}, цена: {self.total_cost()}"


class HotDish(Dish):
    def init(self, name, base_price, spicy_level, **ingredients):
        super().init(name, base_price, **ingredients)
        self._spicy_level = spicy_level

    def info(self):
        return f"Горячее: {self._name}, острота {self._spicy_level}, цена {self.total_cost()}"


class Dessert(Dish):
    def init(self, name, base_price, sweetness, **ingredients):
        super().init(name, base_price, **ingredients)
        self._sweetness = sweetness

    def info(self):
        return f"Десерт: {self._name}, сладость {self._sweetness}, цена {self.total_cost()}"


class Drink(Dish):
    def init(self, name, base_price, volume, **ingredients):
        super().init(name, base_price, **ingredients)
        self._volume = volume

    def info(self):
        return f"Напиток: {self._name}, объем {self._volume} мл, цена {self.total_cost()}"


class Kitchen:
    def init(self):
        self._dishes = []

    def add_dishes(self, *dishes):
        self._dishes.extend(dishes)

    def find_dishes(self, **filters):
        result = []
        for d in self._dishes:
            ok = True
            for key, value in filters.items():
                if getattr(d, "_" + key, None) != value:
                    ok = False
                    break
            if ok:
                result.append(d)
        return result

    def remove_dish(self, dish):
        self._dishes.remove(dish)

    def all_dishes(self):
        return list(self._dishes)


class Restaurant:
    def init(self, name):
        self.name = name
        self.kitchen = Kitchen()
        self.__income = 0

    @property
    def income(self):
        return self.__income

    def order_dish(self, dish_name):
        for dish in self.kitchen._dishes:
            if dish._name == dish_name:
                self.__income += dish.total_cost()
                self.kitchen.remove_dish(dish)
                return f"Заказано: {dish_name}"
        return "Нет такого блюда!"

    def menu(self):
        return [dish.info() for dish in self.kitchen.all_dishes()]

    def status(self):
        return f"Доход: {self.__income} | Осталось блюд: {len(self.kitchen._dishes)}"