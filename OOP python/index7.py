# *args - arguments
def add (*args):
     total = 0 
     for i in args:
        total +=i 
        print(total)

add(2,4,6,7,8,4) 


##### **kwargs - keyword arguments
def pets (owner,**kwargs):
    print(owner)
    for k,v in kwargs.items():
        print(k,v)


pets('Aliya',cat='Felix' , city='Bishkek' , age = 18)


#### комбинация
def demo (*args, **kwargs):
    print(args)
    print(kwargs)

demo(7703010101,180,90, name='Gena' , prof='слесарь')

###
class Student:
    def __init__(self,name,**kwargs):
        self.name =name
        self,kwargs =kwargs
    def info(self):
        print(f"name: {self.name}")
        for i,v in self.kwargs.items():
            print(f"{i}:{v}")

#s = Student('Oleg', car='Gelik', home='JK Muras', child='Vanya')
#s.info()   



import re

my_str = "ghfv3ghjm34hjgb345jgbm45hnjg3456"
numbers = re.findall('[0-9]+', my_str)
for i in numbers:
    nums.append(int(i))
print(nums)

hello = fh # функция это обьект 
hello()
#№№№№№№№№
def gromko(text):
    return text.upper()

def tiho(text):
    return text.lower()

def speak(func,x):
    res = func(x)
    return res

print(speak(gromko, 'как дела гена'))
print(speak(tiho, 'Хорошо Вася, сам как'))

##### функция передаем как параметр, и она работает внутри другой
def inc(x):
    return x*2

def dec(x):
    return x/2

def oper(func, x):
    res = func(x)
    return res

print(oper(inc, 6))
print(oper(inc, 9))
##########
def before_after(func):
    def wrapper():
        print("то что может работать до")
        func()
        print("то что может работать после")
    return wrapper

def say_hi():
    print("привет друг")

decorated = before_after(say_hi)
decorated()
