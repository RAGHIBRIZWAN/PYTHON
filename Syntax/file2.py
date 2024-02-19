
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

def simplefunction():
    print("WELCOME HOME") #JUST DEFINED RIGHT NOW

simplefunction() #ANSWER WILL DISPLAY NOW

def sumdata(a,b): #ARGUMENTS WILL BE PASS IN PARENTHESIS
    print(a+b)

sumdata(20,30)


def sum(c=10,d=15): #ARGUMENTS WILL BE PASS IN PARENTHESIS
    print(c+d)

sum()

def sum2(c,d=15): #ARGUMENTS WILL BE PASS IN PARENTHESIS
    print(c+d)

sum2(20)

# (3) RETURN FUNCTION (USED TO STORE VALUES)

def returns(a,b=5):
    c = a+b
    return c
output = returns(40)

print(output)
