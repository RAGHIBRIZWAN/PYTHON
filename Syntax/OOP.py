#CLASS

class DemoClass:
    a = 10

#OBJECT (USED TO CALL FUNCTIONS)

object = DemoClass() # OBJECT IS FORMED

print(object.a) # . + variable is used to call class

#METHODS ARE DEFINED IN CLASS BUT ARE SAME AS FUNCTIONS

class DemoClass1:
    def sumvalue(self): # SELF IS A METHOD OF CLASS
        print(20+30)

object1=DemoClass1()
object1.sumvalue()

#METHODS

class Demo:
    a = 20
    def showvalue(self):
        print(self.a) # SELF IS MUST TO SHOW RESULTS

        self.c = self.a * self.a
        print(self.c)

    def showvalue1(self):
        print("WELCOME HOME")

    def showvalue2(self,a,b):
        print(a+b)

obj=Demo()
obj.showvalue()
obj.showvalue1()
obj.showvalue2(10,20)

#CONSTRUCTOR

class Hello:
    def __init__(self): # __init__ is used to define constructor
        print("WELCOME HOME")

obj=Hello()

# INHERITANCE

class A:
    def displayA(self):
        print("WELCOME HOME A")

class B(A):
    def displayB(self):
        print("WELCOME HOME B")
class C(B):
    def displayC(self):
        print("WELCOME HOME C")

obj=C()
obj.displayA()
obj.displayB()
obj.displayC()

#MULTIPLE INHERITANCE

class A:
    def displayA(self):
        print("WELCOME HOME A")

class B():
    def displayB(self):
        print("WELCOME HOME B")
class C(A,B):
    def displayC(self):
        print("WELCOME HOME C")

obj=C()
obj.displayA()
obj.displayB()
obj.displayC()

#ENCAPSULATION (GETTER AND SETTER)

class Student:
    def __init__(self): # __init__ is used to define constructor
        self.__name=""
    def getname(self):
        return self.__name
    def setname(self,name):
        self.__name=name

obj=Student()
obj.setname("Testing")
name = obj.getname()
print(name)

class Student1:
    __name = "Raghib" # __ is used to make private variable
    def __init__(self):
        print(self.__name)
        self.__displayinfo()
    def __displayinfo(self):
        print("WELCOME HOME")

obj=Student1()
obj.__name

# POLYMORPHISM (SAME FUNCTION NAME BUT DIFFERENT SIGNATURES)

l = [10,20,30,40]
print(len(l))

s = "WELCOME"
print(len(s))

#OVERLOADING

class ws:
    def displayinfo(self,name=""):
        print("WELCOME TO WSCUBETECH"+name)

obj = ws()
obj.displayinfo()
obj.displayinfo("PYTHON") # THIS IS CALLED OVERLOADING (SAME FUNC BUT DIFF RESULT MEANS DIFF PARAMETER)


# OVERRIDING
class Hello:
    def displayinfo(self):
        print("WELCOME TO WSCUBETECH")

class Hi(Hello):
    def displayinfo(self):
        print("WELCOME TO PAKISTAN")

obj = Hi()
obj.displayinfo() # IT OVERWRITES THE FUNCTION

#SUPER() FUNCTION

class Hello:
    def displayinfo(self):
        print("WELCOME TO WSCUBETECH")

class Hi(Hello):
    def displayinfo(self):
        super().displayinfo() # CALLS BOTH FUNCTIONS
        print("WELCOME TO PAKISTAN")

obj = Hi()
obj.displayinfo()

#OVERLOADING EXAMPLES

class Area:
    def find_area(self,a=None,b=None):
        if a !=None and b != None:
            print("AREA OF RECTANGLE:",a*b)
        elif a != None:
            print("AREA OF SQUARE:",a*a)
        else:
            print("Nothing")

obj = Area()
obj.find_area()
obj.find_area(10)
obj.find_area(10,20)

#OVERRIDING EXAMPLE

class A:
    def ShowData(self):
        print("HELLO A")
class B(A):
    def ShowData(self):
        print("HELLO B")
obj=B()
obj.ShowData()
