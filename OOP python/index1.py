#инкапсулация-изолируем объект
# public-публичный 
#_protected-защищенный
#__private-приватный
class Animal:
    def __init__(self,name,age, color,gender):
        self.name = name
        self.age = age
        self.color=color
        self.gender=gender

    @property
    def age(self):
        return self.__age


    @age.setter
    def age(self,value):
        if value >0 and value <20:
            self.__age = value


    def set_name(self,new_name):
        self.name = new_name
        return self.name

    def info(self):
        print(f'имя:{self.name}, возрасть: {self.age}, свет: {self.color}, гендер: { self.gender}')



class Cat(Animal):
    def mau(self):
        print("мяу-мяу")

class Dog(Animal):
    def dog(self):
        print("гав-гав")

cat1 = Cat('Felix',2,'рыжий','самка')
dog1= Dog('Bobik',3,'черный','самец')
cat1.age=12
print(cat1.age)

