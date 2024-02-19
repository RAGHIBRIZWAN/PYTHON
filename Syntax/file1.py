// OPERATORS

print(3 > 2)
print(3 < 2)
print(3 >= 2)
print(3 <= 2)
print(3 == 2)
print(2 == 2)
print(3 != 2)
print(3 != 3)


#logical operators

#atleast one is true then print true (or)
print(2 > 3 or 2 > 1)

# if both are true then print true (and)
print(2 > 3 and 2 > 1)
print(4 > 3 and 2 > 1)

#not operator : converts false into true and vice versa

print(not 2 > 3)

i = 5
i = i + 2 #expended form
i += 2 #minimize form

#operator precedence

results = 2 + 3 * 5
print(results)

results = (2 + 3) * 5
print(results)

// CAPITALIZE CHARACTERS

name = "Tony Stark"

print(name.find('S'))
print(name.find('a')) #-1 shows there is no letter you are finding
print(name.find('T')) #index starts from zero(0)

print(name.replace('Tony Stark' , 'Iron Man'))

//CONVERSIONS

first = input("Enter first number")
second = input("Enter second number")

sum = int(first) + int(second)
print(sum)

print("The sum is :" + str(sum))

// DICTIONARY

marks = {"english" : 95, "chemistry" : 98} # where english is key and 95 is value
information = {"raghib" : "rizwan"}
print(marks["chemistry"])

marks["physics"] = 97; # to add physics in dictionary
print(marks)

marks["physics"] = 99; # to change previous marks
print(marks)

// IF ELSE

a = input("Enter first number")
operator = input("Enter operator (+,-,*,/,%) : ")
c = input("Enter second number")

a = int(a)
c = int(c)

if operator == "+":
    print(a + c)
elif operator == "-":
    print(a - c)
elif operator == "*":
    print(a * c)
elif operator == "/":
    print(a / c)
elif operator == "%":
    print(a % c)
else:
    print("Invalid operation")

// FIND AND REPLACE METHOD

name = "Tony Stark"

print("T" in name)

// WHILE loop on list data type

marks = [97,98,99,100]

i = 0

while i < len(marks):
    print(marks[i])
    i = i + 1

marks.clear()
print(marks)

// # MODULE / MATH MODULE

import math
print(dir(math))

from math import sqrt
print(sqrt(4))

from math import * # * means to select all or for all
print()

# USER-DEFINED
def print_sum(first, second):
    print(first + second)

print_sum(1, 2)


def print_sum(first, second=4):
    print(first + second)

print_sum(1)

//# Arthimetic Operators

print(5+2)
print(5-2)
print(5*2)
print(5/2)

print(5//2) #using // the part after decimal will be removed

print(5%2) #remainder operator

print(5**2) #power operator

// #list data type

marks = [97,97,95]

print(marks)
print(marks[1])
print(marks[-1])

print(marks[0:2]) # where 2 doesn't be considered
print(marks[1:3]) # where 0 and 3 doesn't be considered

//# for loop in list data type

marks = [95,96,98]   # square brackets are used

for score in marks:
    print(score)


#append operation: add at the end

marks.append(99)
print(marks)

# insert operation:add where you want

marks.insert(0,99) # where 0 tells about the index where 99 prints
print(marks)

print (len(marks))

// Logical Operators

age = 19

if age >=18:

    print("you are an adult")
    print("you can vote")

print("Thank you") #space of four letters is must to execute if statement

age_1 = 16

if age_1 >=18:

    print("you are an adult")
    print("you can vote")

print("Thank you") #space of four letters is must to execute if statement

//#tupple : it is just like list but we cannot make changes in it

marks = (95,98,97) # in tupple round brackets are used

# marks[0] = 99 # always error

mark = (97,97,97,98,95)

print(mark.count(97))
print(mark.index(97))

//#for loops is used to apply on list or items

for item in range(5):
    print(item)
    print(item + 1)

// JSON load and dump

import json

d={
"name":"python",
"fees":15000
}

a = json.dumps(d)
print(type(a))
print(a)

import json

d = '{"name":"python","fees":15000}'
a = json.loads(d)
print(type(a))
print(a)

