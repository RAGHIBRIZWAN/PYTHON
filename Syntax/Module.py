# CALLING MODULE

# 1ST METHOD

import module_creatte # CALLING FUNCTION
print(module_creatte.sum(10,20))
print(module_creatte.mul(10,10))

# 2ND METHOD

from module_creatte import sum # CALLING FUNCTION
print(sum(10,20))

import module_creatte as m # where m = alias (used instead of module name)
print(m.sum(10,20))

#MODULES IN MATH

import math # MATH = LIBRARY

x = 10.2 # WHEN FOLAT VALUE IS USED IT WILL AUTOMATICALLY CONVERT IT IN FORWARD INTEGER
print(math.ceil(x))

x = -10
print(math.fabs(x)) # CONVERTS NEGATIVE INTO POSITIVE

x = 5
print(math.factorial(x)) # NO NEGATIVE VALUE IN FACTORIAL

x = 10.6
print(math.floor(x)) # WHEN FOLAT VALUE IS USED IT WILL AUTOMATICALLY CONVERT IT IN BACKWARD INTEGER

l=[10,20,30,40]
print(math.fsum(l)) # GIVES THE SUM OF WHOLE LIST OR TUPLE

print(math.sqrt(16)) #GIVES SQUARE ROOT OF ANY NUMBER

#RANDOM MODULE

import random # BUILTIN MODULE

print(random.randint(3,10)) # 3 AND 10 ARE INCLUDED

print(random.randrange(3,10)) # 3 IS INCLUDED BUT 10 IS NOT INCLUDED

l = ["Apple","BANANA","cherry"]
print(random.choice(l)) # GIVES ANY ELEMENT FROM LIST

print(random.random()) #GIVES ANY VALUE FROM 0 TO 1

l = ["Apple","BANANA","cherry"]
print(random.shuffle(l)) #SHUFFLE VALUES OF LIST
print(l)

print(random.uniform(10,20)) # ANY FLOAT NUMBER FROM GIVEN PARAMETERS

# DATE AND TIME MODULE

import datetime

x = datetime.datetime.now()  # CURRENT DATE AND TIME
print(x)

x =datetime.datetime(2005,6,30)
print(x)

x =datetime.datetime.now()
m = x.strftime("%Y") #GIVES FULl YEAR (2023)
print(m)

m = x.strftime("%y") #GIVES YEAR (23)
print(m)

m = x.strftime("%b") #GIVES MONTH
print(m)

m = x.strftime("%B") #GIVES FULl MONTH
print(m)

m = x.strftime("%M") #GIVES MINUTES
print(m)

m = x.strftime("%m") #GIVES MONTH AS A NUMBER
print(m)

m = x.strftime("%H") #GIVES HOUR (13)
print(m)

m = x.strftime("%I") #GIVES HOUR (1)
print(m)

m = x.strftime("%p") #GIVES PM/AM
print(m)

#PICKLE LIBRARY (USED TO STORE DATA IN A FILE) (BUILTIN LIBRARY)
# TO SERIALIZE DATA USE DUMP()

import pickle
l = [10,20,30,40]

file = open('pickledata.txt','wb') # wb is used for dump

pickle.dump(l,file)
file.close()

# TO DE-SERIALIZE DATA USE LOAD() --- USED TO READ SERIALIZE DATA

import pickle
file = open('pickledata.txt','rb') # rb is used for load
l=pickle.load(file)

print(l)
