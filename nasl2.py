class CanRun:
    def run(self):
        print("Бегу!")

class CanBark:
    def bark(self):
        print("Гав-гав!")

class Dog(CanRun, CanBark):
    pass

dog = Dog()
dog.run()   
dog.bark() 