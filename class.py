class Student:
    x = "John"
    print(x)
    
    def happy():
        return "I am happy"
    
print(Student.x)
print(Student.happy())

class teacher:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
d = teacher("Peter", 23)
print(d.name)
print(d.age)

class Car:
    def __init__(self, model, year, name):
        self.model = model
        self.year = year
        self.name = name
        
    def drive(self):
        return f"I drive {self.name} {self.model} {self.year} model"
C = Car("C202", 2024, "Mercedez")
print(C.name)
print(C.model)
print(C.year)
print(C.drive())

class Person:
    def __init__(self, address, name, occupation):
        self.address = address
        self.name = name
        self.occupation = occupation
        
    def Greet(self, Salary):
        print(f"Hello {self.name} is a {self.occupation} and earns ${Salary}")
        
    def play(self):
        return f"He stays at {self.address}"
    
p = Person("12 NTA Road", "Moses", "Lawyer")
print(p.address) 
print(p.name)
print(p.Greet(300000))
print(p.play())

# Classes

class Food:
    x = "Eba"
    y = "Noodles"
    
print(Food.y)
print(Food.x)

class Play:
    def name(fname, lname):
        print(f'Hello {fname} {lname} hope you are playing')
        
Play.name('John', 'Kenny')

class Happy:
    
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        print(f'Hello {self.fname} {self.lname}')
        
h = Happy("Henry", 'Bassey')
print(h.fname)
print(h.lname)

class Animal:
    def __init__(self, name, age, leg):
        self.name = name
        self.age = age
        self.leg = leg
    
    def display(self):
        print(f"The name of this animal is {self.name}")
        print(f'This animal is {self.age} years old')
        print(f'This animal has {self.leg} legs')
        
A = Animal("Cow", 102, 4)
print(A.name)
print(A.age)
print(A.leg)
A.display()        
        