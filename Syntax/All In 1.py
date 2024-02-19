#PRINT

print("WELCOME TO PAKISTAN","HELLO WORLD",80)
print(10>5)

#variable

a = 10
b = 20
print(a,b)

print(id(a),id(b))

#Concatenation

a = "HELLO"
b = "WORLD"
print(a+b)

c = 20
d = 30
print(c+d)

#Arthimetic Operators

a = 20
b = 10

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(10%3)
print(5**2)
print(10//3)

#Assignment operators

x = 5
print(x)

x = x + 5 # INCREMENT
print(x)

x += 5 # INCREMENT (SAME AS ABOVE)
print(x)

x -= 5 # DECREMENT
print(x)

x = x - 5 # DECREMENT (SAME AS ABOVE)
print(x)

# COMPARISON OPERATORS

a = 5
b = 10

print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)
print(a>b)
print(a<b)

# LOGICAL OPERATORS

x = 10
y = 20

print(x==10 and x<y)
print(x==10 or x>y)
print(x==10 and x<y and x==y)
print(not x==10)

#MEMBERSHIP OPERATORS

x = "HELLO"
print("H" in x)
print("P" in x)

# IDENTITY OPERATORS

a = 10
b = 10

print(a is b,a==b)
print(a is not b,a!=b)

#BITWISE OPERATOR

a = 10
b = 8
print(bin(a))
print(bin(b))

print(a&b,bin(a&b))

print(a|b,bin(a|b))

print(a^b,bin(a^b))

#DATA TYPES

a = 5
print(a,type(a)) #integer

a = 5.5
print(a,type(a)) #float

a = 2+5j
print(a,type(a)) #complex

s = "hello@gmail.com" #string
print(s,type(s))

#list (DATA TYPE)

l = ["A",20,4.5]
print(l,type(l))
l[2] = 10
print(l,type(l))

#TUPLE (FASTER THAN LIST) (DATA TYPE)

t = (10,20,"HELLO")
print(t,type(t))

t = (2)
print(t,type(t))

#DICTIONARY (DATA TYPE)

d= {
    'name':'Raghib',
    'course_name':'python',
    'course_duration':'one week'
}
print(d,type(d))
print(d['name']) # gives only name

#SET (DATA TYPE)

s = {10,20,30,20}
print(s,type(s))

#TYPE CASTING AND INPUT

a = input("ENTER THE VALUE:")
b = input("ENTER ANOTHER VALUE")

print(a+b) # IT CONCATENATES

a = int(input("ENTER 1ST NUMBER")) # convert a and b in integer
b = int(input("ENTER 2ND NUMBER"))

print(a + b)

a = float(input("ENTER 1ST NUMBER"))
b = float(input("ENTER 2ND NUMBER"))

print(a + b)

a = eval(input("ENTER 1ST NUMBER")) # IT CONVERTS EVERYTHING LIKE BINARY NUMBERS , INTEGERS , FLOAT ETC.
#b = eval(input("ENTER 2ND NUMBER"))

#print(a + b)

#CONDITIONAL STATEMENTS

#IF

a = int(input("ENTER THE VALUE:"))
if a > 2 :
    print(a)

#IF ELSE

a = int(input("ENTER THE VALUE:"))
if a > 2 :
    print(a)
else:
    print("FALSE")

#IF ELIF ELSE

per = int(input("ENTER THE VALUE"))
if per>=60:
    print("1ST DIV")
elif per>=40:
    print("2ND DIV")
elif per>=35:
    print("3RD DIV")
else:
    print("FAIL")

#FOR LOOP WITH RANGE

#range(5) #start=0 , condition<4 , increment = 1 (DEFAULT) means 0 1 2 3 4
#range(1,6,2) #start=1 , condition<6 , increment=2 means 1 3 5

for n in range(5): #01234
    print(n)

for x in range(1,6):
    print(x)

for y in range(1,6,2):
    print(y)

for z in range(2,21,2):
    print(z)

# REVERSE LOOP

for n in range(10,0,-1):
    print(n)

#WHILE LOOP

i=1
while i<=10:
    i=i+1
    print("HELLO WORLD")

a=10
while a>=1:
    a = a-1
    print(a)

#STRING INDEXING

w = "WELCOME TO HOME"
print(w[6])
print(w[-4])

#STRING SLICING

# L TO R SLICING
w = "WELCOME TO HOME"
print(w[0:7])
print(w[0:])
print(w[0::2])

# R TO L SLICING
print(w[-1:])
print(w[-1::-1])
print(w[-1::-2])

#STRING ITERATION (Single Letter Required)

w = "WELCOME TO WSCUBETECH"
t = len(w)
print(t)

for a in range(t): # FOR LOOP IS MUST
    print(w[a]) #w[0],w[1],w[2],.......

#REVERSE

w = "WELCOME TO WSCUBETECH"
w=w[-1::-1]
t = len(w)
print(t)

for a in range(t): # FOR LOOP IS MUST
    print(w[a]) #w[0],w[1],w[2],.......

#METHOD 2 OF ITERATION FOR ITERATION

for a in range(t-1,-1,-1):
    print(w[a])

#STRING FUNCTIONS

w = "WELCOME HOME"
n = w.lower() #all in small
print(n)

n = w.upper() #all in capital
print(n)

n = w.title() #1st letter in capital
print(n)

n = w.capitalize() #capitalize 1st letter of 1st word only
print(n)

h = "WELCOME"
print(h.find('L'))
print(h.find('E',2))

h = "WELCOME"
print(h.index('E'))

#isalpha (all are alphabets then true)

w = "WELCOME"
print(w.isalpha())

#isalpha (all are alphabets then true)

print(w.isdigit())

#isalnum (all are numbers or characters but no special characters then true)

print(w.isalnum())

#CHR(passing integer value between its brackets)

a = 65
print(chr(a))

#ORD(passing string value between its brackets and always single value)

print(ord("a"))
print(ord("A"))

#STRING FORMAT

a = "welcome to {}".format("PAKISTAN")
print(a)
a = "welcome to {a:10} {b}".format(a=30,b=40)
print(a)
a = "welcome to {a:^10} {b}".format(a=30,b=40)
print(a)
a = "welcome to {a:<10} {b}".format(a=30,b=40)
print(a)
a = "welcome to {a:>10} {b}".format(a=30,b=40)
print(a)

#CREATE LIST

l=[1,2,3]
print(l)

l=[1,2,3,[4,5,6]]
print(l[3][1])

l=[10,30,40,50,"HELLO"]
print(l,type(l))

#SLICING
print(l[3],l[4])
print(l[0:2]) # 2 values
print(l[0:3])
print(l[0::2])
print(l[-1::-1])
print(l[-1::-2])

#LIST ITERATION

#METHOD 1
l=[10,20,30,40,50,60,70]
t=len(l)
print(t)

for a in range(t):
    print(l[a])

#METHOD 2
for a in l:
    print(a)

for a in range(t-1,-1,-1):
    print(l[a])

#LIST COMPREHENSION

l=[]
for a in range(1,101,1):
    print(a)

    l.append(a) #NORMAL FORMULA
print(l)

n = [b for b in range(1, 101)] #COMPREHENSION
print(n)

n = [b for b in range(1, 101) if b%2==0 ] # b%2==0 is used for even numbers
print(n)

#STRING IN LIST

s="HELLO"
d=[g for g in s]
print(d)

#LIST FUNCTIONS

l=[10,20,30,40]
print(l)

del l[1] #ONLY FOR LIST
print(l)

print(l.pop(1)) #TELLS THE NUMBER WHICH IS DELETED
print(l)

l.remove(40)
print(l)

l.clear()
print(l)

l.insert(0,20)
print(l)

l.append(70) #ALWAYS ADD ON LAST
print(l)

l=[10,20,30,40]
n=[50,60]
l.append(n)
print(l)

l=[10,20,30,40]
n=[50,60]
l.extend(n)
print(l)

p=[10,20,30,40,50,10,20]
a = l.count(10)
print(a)

b = max(p)
print(b)

c=min(p)
print(c)

q=['hello','world']
b = max(q)
print(b)

c = min(q)
print(c)

p.sort() #DISPLAY DATA IN ASCENDING ORDER
print(p)

p.reverse(p)
print(p)

a = p.index(50)
print(a)

#ZIP FUNCTION (ITERATE OVER 2+ LISTS AT A SAME TIME)

l=[10,20,40,50]
l1=[3,4,77,88]

for a,b in zip(l,l1):
    print(a,b)

#OR

l=[10,20,40,50]
l1=[3,4,77,88]

t=len(l)
for h in range(t):
    print(l[h],l1[h])

#STRING TO A LIST

l = input("ENTER THE VALUE:")
print(l)
a = l.split()  #SPLIT FUNCTION IS USED TO CONVERT STRING INTO LIST
print(a)

#multiple inputs

l=[]
for a in range(3):
    n=input("ENTER THE VALUE"+ str(a) + ":")
    l.append(n)

print(l)

#LIST STACK(LIFO)

l=[]
while True:
    c = int(input('''
       1 push elements
       2 pop elements #DELETE LAST ELEMENT
       3 peek elements #LAST ELEMENT
       4 display stack
       5 exit
    '''))
    if c==1:
        n=input("ENTER THE VALUE:")
        l.append(n)
        print(l)
    if c==2:
        if len(l)==0:
            print("EMPTY LIST")
        else:
            p=l.pop()
            print(p)
            print(l)
    if c==3:
        if len(l)==0:
            print("EMPTY LIST")
        else:
            print("LAST STACK VALUE",l[-1])
    if c==4:
        print("DISPLAY STACK",l)
    if c==5:
        break;
    else:
        print("INVALID OPERATION")

    #LIST QUEUE(FIFO)

    l = []
    while True:
        c = int(input('''
           1 push elements
           2 pop first elements
           3 front elements
           4 last stack
           5 display stack
           6 exit
        '''))
        if c == 1:
            n = input("ENTER THE VALUE:")
            l.append(n)
            print(l)
        if c == 2:
            if len(l) == 0:
                print("EMPTY QUEUE")
            else:
                del l[0]
                print(p)
                print(l)
        if c == 3:
            if len(l) == 0:
                print("EMPTY LIST")
            else:
                print("FIRST STACK VALUE", l[0])
        if c == 4:
            if len(l) == 0:
                print("EMPTY LIST")
            else:
                print("LAST STACK VALUE", l[-1])
        if c == 5:
            print("DISPLAY QUEUE",l)
        if c == 6:
            break;
        else:
            print("INVALID OPERATION")


# DICTIONARY

d={
    'name':'Raghib',
    'course':'Python',
    'fees':8000
}
print(d)
print(d["name"])

for a in d:
    print(a) # RETURNS KEY

for a in d:
    print(d[a]) #RETURNS VALUE


# DICTIONARY FUNCTIONS

d={
    'name':'Raghib',
    'course':'Python',
    'fees':8000
}
print(d)
print(d["name"])

for a in d:
    print(a) # RETURNS KEY

for a in d:
    print(d[a]) #RETURNS VALUE

d = {
        'name': 'Raghib',
        'course': 'Python',
        'fees': 8000
}
c = d.get('course')
print(c)

for a in d.keys():
    print(a)

for a in d.values():
    print(a)

for a,b in d.items(): #RETURNS BOTH KEYS AND VALUES
    print(a,b)

del d["fees"]
print(d)

d.pop('name')
print(d)

d = dict(name = 'raghib',fees=8000,course='python')
print(d)

d.update({"fees":10000})
print(d)

d.clear()
print(d)

d = dict(name = 'raghib',fees=8000,course='python')
print(d)

d["desc"]="THIS IS PYTHON"
print(d)

#NESTED DICTIONARY

d={
    'php':{'duration':'3 months','fees':15000},
    'java': {'duration': '4 months', 'fees': 18000},
    'python': {'duration': '2 months', 'fees': 10000}
}
print(d)
print(d['php']['fees'])

#iterating whole value

for a,b in d.items():
    print(a,b)
    print(a,b['duration'])

d['java']['fees']=20000
print(d)

#TUPLE

t=(10,20,30,40,50)
print(t,type(t))

n = t[3]
print(n)

#ITERATION TUPLE

l = len(t)
print(l)

for a in range(l):
    print(t[a])
#OR
for b in t:
    print(b)

#TUPLE FUNCTIONS

t=(10,20,30,40,50)

m = min(t)
print(m)

m = max(t)
print(m)

c = t.count(10)
print(c)

d = t.index(50)
print(d)

e = sum(t)
print(e)


#SETS
s = {10,20,30,40,50}
print(s,type(s))

#ITERATION
for a in s:
    print(a)

#SETS FUNCTIONS

l=[10,20,30,40,50]
s = set(l)
print(s)

s = {10,20,30,40,50}
s.remove(20)
print(s)
#OR
s.discard(40)
print(s)

s.pop() #RANDOMLY DELETE
print(s)

s.clear()
print(s)

s.add(60)
print(s)

l=[10,20,30,40,50]
s = {10,20,30,40,50,60}
s.update(l)
print(s)

#USER DEFINE FUNCTION

# (1) SIMPLE FUNCTION

def simplefunction():
    print("WELCOME HOME") #JUST DEFINED RIGHT NOW

simplefunction() #ANSWER WILL DISPLAY NOW

# (2) ARGUMENT FUNCGTION

def sumdata(a,b): #ARGUMENTS WILL BE PASS IN PARENTHESIS
    print(a+b)

sumdata(20,30)
#OR
def sum(c=10,d=15): #ARGUMENTS WILL BE PASS IN PARENTHESIS
    print(c+d)

sum()
#OR
def sum2(c,d=15): #ARGUMENTS WILL BE PASS IN PARENTHESIS
    print(c+d)

sum2(20)

# (3) RETURN FUNCTION (USED TO STORE VALUES)

def returns(a,b=5):
    c = a+b
    return c

output = returns(40)

print(output)
