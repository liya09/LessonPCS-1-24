class Book:
    def __init__(self, title, author, year):  
        self.title = title
        self.author = author
        self.year = year
        self.is_available = True

    def info(self):
        return f"Название: {self.title}, Автор: {self.author}, Год: {self.year}, Доступность:{self.is_available}"

    def borrow(self):
        if self.is_available:
            self.is_available = False
            return self.is_available

    def return_book(self):
        self.is_available = True
        return self.is_available

book1 = Book('Война и мир',"Лев Толстой ", 1867)
book1.borrow()
message = book1.info() 
print(message)
book1.return_book()
message = book1.info()
print(message)



class Student:
    def __init__(self, name, group):
        self.name = name
        self.group = group
        self.courses = [] 

    def enroll(self, course):
     if course not in self.courses:
        self.courses.append(course)
        course.add_student(self)  


class Course:
    def __init__(self, name):
        self.name = name
        self.students = [] 

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            if self not in student.courses:
                student.courses.append(self)  

                