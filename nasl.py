class Product:
    def init(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def buy(self, amount):
        if amount > self.quantity:
            print(f"Недостаточно {self.name}")
            return False
        self.quantity -= amount
        print(f"Покупка {amount} шт {self.name} оформлена")
        return True

    def show_info(self):
        print(f"{self.name}, цена: {self.price}, количество: {self.quantity}")


class FoodProduct(Product):
    def init(self, name, price, quantity, expiration_date): 
        super().init(name, price, quantity) 
        self.expiration_date = expiration_date     


    def show_expiration(self):
        print(f"Срок годности продукта {self.name}: {self.expiration_date}")

class ElectronicsProduct(Product):
    def init(self, name, price, quantity, warranty_years): 
        super().init(name, price, quantity) 
        self. warranty_years =  warranty_years  

    def show_warranty(self):
        print(f"Срок гарантии продукта {self.name}: {self.warranty_years} год(а)")


hleb = FoodProduct("Яблоко", 100, 10, "10.11.2025")
apple = ElectronicsProduct('Apple pro m4', 22500, 6, 1)
hleb.show_expiration()
apple.show_warranty()
apple.buy(3)
hleb.buy(3)