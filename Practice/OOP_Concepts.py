#BASICS
class Person:
    
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def info(self):
        print(f"{self.__name} is {self.__age} years old")

p = Person('Raghib',19)
p.__name = 'Rizwan'
p.__age = 45
p.info()

a = Person('Rizwan',45)
a.info()

#SUPER FUNCTION
class Hello:
    def displayinfo(self):
        print("WELCOME TO WSCUBETECH")

class Hi(Hello):
    def displayinfo(self):
        super().displayinfo() # CALLS BOTH FUNCTIONS
        print("WELCOME TO PAKISTAN")

obj = Hi()
obj.displayinfo()

class Circle:
    pi = 3.14

    def __init__(self,radius):
        self.radius = radius

    def calc_circumference(self):
        return 2*self.pi*self.radius

c = Circle(4)
print(c.calc_circumference())

class Father:
    def __init__(self):
        print('Father"s Constructor')

    def show(self):
        print('Father here!')

class Son(Father):
    def __init__(self):
        super.__init__()
        print('Son"s Constructor')
    
    def show(self):
        super().show()
        print('Son here!')

s = Son()
s.show()

# MULTIPLE INHERITENCE

class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species

    def show_details(self):
        print(self.name)
        print(self.species)
    
class Dog(Animal):
    def __init__(self,name,species,breed):
        Animal.__init__(self,name,species)
        self.breed = breed

    def show_details(self):
        Animal.show_details(self)
        print(self.breed)

class BullDog(Dog):
    def __init__(self,name,species,breed,color):
        Dog.__init__(self,name,species,breed)
        self.color = color

    def show_details(self):
        Dog.show_details(self)
        print(self.color)

# dog = Dog('Bulldog','Dog','Black')
dog = BullDog('Lulu','Cat','Grey','Black')
dog.show_details()

#STATIC METHOD
class Maths:
    @staticmethod
    def add(x,y):
        return x+y
    
    @staticmethod
    def mul(x,y):
        return x*y
    
print(Maths.add(2,3))
print(Maths.mul(2,3))

#CLASS METHOD
class Car:
    company = 'Apple'
    def show(self):
        print(f"Company name is {self.company}")

    @classmethod
    def changeCompany(self,new):
        self.company = new

c = Car()
c.show()
c.changeCompany('Samsung')
c.show()
print(c.company)
print(Car.company)

#ABSTRACT CLASS
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Duck(Animal):
    def speak(self):
        print('I Quack!')
    
class Cat(Animal):
    def speak(self):
        print('I Meow!')

d = Duck()
d.speak()

#OPERATOR OVERLOADING
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self,other):
        return Point(self.x - other.x, self.y - other.y)
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
p1 = Point(1,2)
p2 = Point(1,2)

p3 = p1 + p2

print(p3)

p3 = p1 - p2

print(p3)

#DECORATORS

def greet(fx):
    def mfx():
        print('Good Morning')
        fx()
        print('Thankyou!')
    return mfx

@greet
def hello():
    print('Hello World!')

hello()
