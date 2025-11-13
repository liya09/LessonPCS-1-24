### @property
    #getter
    #setter
    #deletwer


class Teacher:
    def __init__(self, name, phone):
         self.name = name
         self.__phone = phone



@property 
  def phone (self):
  return self.__phone

  @phone.setter
  def phone (self,value):
    print("Сеттер сработал")
    self.__phone = value


  @phone.deleter
  def phone (self):
    print("Удалили номер deleter")

    def info(self):
        return f"{self.name} {self.__phone}"

t = teacher ('Ali',770770770)
t.phone = 45
print (t.phone)
#del t.phone
print(t.info())