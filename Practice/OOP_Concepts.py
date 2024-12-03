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

def authenticate(fx):
    def mfx(name,pswd):
        if names[name] == pswd:
            print('Logged In!')
            # fx()
        else:
            print('Incorrect Password!')
    return mfx

@authenticate
def hello():
    pass

hello('raghib',1)








class Person:
    name = "Raghib"
    occupation = "AI Specialist"
    networth = 0
    def info(self): # self is used as a parameter for an object or self is an object made afterwards like obj
        print(f'{self.name} is an {self.occupation} having networth {self.networth}')

obj = Person()
obj.name = "Harry"
obj.info()

class officer:
    name = "Raghib"
    post = "Sergant"

    def __init__(self,i,j): # CONSTRUCTOR
        print('I am an officer')
        self.name = i
        self.post = j

    def information(self):
        print(f'officer name is {self.name} and his post is {self.post}')

off1 = officer("Raghib","Marshal")
print(off1.information())

class MyClass:
    def __init__(self,value):
        self.value = value

    def show(self):
        print(f"Value is {self.value}")

    def setter(self,newValue): # SETTER
        self.value = newValue

classObj = MyClass(10)
classObj.show()
classObj.setter(20)
classObj.show()

# INHERITANCE

class Employee:
    def __init__(self,name,id,password):
        self.name = name
        self.id = id
        self.__password = password # __ is used to make a private variable
    
    def showDetails(self):
        print(f"The name is {self.name} and id is {self.id}")

class Programmer(Employee): #Inheritance
    def showLanguage(self):
        print('Default language is Python')
    
p = Programmer('Raghib',12,123456) 
# print(p.__password) # Cannot be accessed directly
print(p._Employee__password) # Can be accessed indirectly
p.showDetails()
p.showLanguage()

class Man:
    companyName = 'RRR Clouds' # Associated to class or same for all
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.raiseAmount = 20

    def showDetails(self):
        print(f"name: {self.name}, age: {self.age}, raise amount: {self.raiseAmount}, company name: {self.companyName}")

man1 = Man('Raghib',19)
man1.raiseAmount = 30
man1.companyName = 'Apple' # It checks instance first then class
man1.showDetails()

man2 = Man('Rizwan',45)
man2.raiseAmount = 40
man2.showDetails()

man3 = Man('Rabani',60)
man3.showDetails()

# Class Method

class check:
    company = 'Apple'
    def show(self):
        print(f"Company name is {self.company}")

    @classmethod # By this we can change the class variables directly
    def changeName(self,newCompany):
        self.company = newCompany
    
c1 = check()
print(c1.company)
c1.changeName('Tesla')
print(c1.company)
c1.show()
print(check.company)

# Class Method As Alternative Constructor

class using:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod
    def fromstr(cls,string):
        return cls(string.split("-")[0],string.split("-")[1])
    
u1 = using('Raghib',19)
print(u1.name)
print(u1.age)

string = "Raghib-19"
u2 = using.fromstr(string)
print(u2.name)
print(u2.age)

# dir,dict,help

x = [1,2,3]
print(dir(x))

class dict:
    def __init__(self,name,age):
        self.name = name
        self.age = age

d = dict('Hello',20)
print(d.__dict__) # All variables will be displayed as dictionary

# print(help(dict))

# Super Keyword:- This is used to call the method of parent class

class Parent:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def parentMethod(self):
        print('Parent method')

class Child(Parent):
    def __init__(self, name, age,lang):
        super().__init__(name, age)
        self.lang = lang

    def childMethod(self):
        print('Child method')
        super().parentMethod()

c = Child('Raghib',19,'Python')
c.childMethod()
print(c.lang)
print(c.name)
print(c.age)


class Hello:
    def displayinfo(self):
        print("WELCOME TO WSCUBETECH")

class Hi(Hello):
    def displayinfo(self):
        super().displayinfo() # CALLS BOTH FUNCTIONS
        print("WELCOME TO PAKISTAN")

obj = Hi()
obj.displayinfo()

# Method Overriding

class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
    
    
rec = Shape(3,5)
print(rec.area())

cir = Circle(5)
print(cir.area())

# Operator Overloading

class Vector:
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
    def __add__(self,x):
        return Vector(self.i+x.i,self.j+x.j,self.k+x.k)
    
    def __sub__(self,x):
        return Vector(self.i-x.i,self.j-x.j,self.k-x.k)
    
vec1 = Vector(2,3,4)
vec2 = Vector(2,3,4)
print(vec1)
print(vec2)
print(vec1 + vec2)
print(type(vec1 + vec2))
print(vec1-vec2)
print(type(vec1 - vec2))
