import numpy as np
# Numpy Array using List.

# a.ndim -> used for checking dimensions
# a = np.array([1,2,3,4,5], ndmin = 5) -> used to make an array of 5 dimensions
# np.append() is used to append list in an array
# np.diag([1,2,3,4,5]) is used to make a diagonal matrix
# np.isnan is used to check is the array null or not
# arr.dtype is used to get data type of array
# for x in np.nditer(arr):
#    print(x) -> gives each and every element of an array.
# np.array_split(arr,3) -> 3 = number of splits
# np.where(arr == 4) -> used to find an element in an array.
# np.searchsorted(arr,10) -> finds index where value 10 should be inserted
# arr.transpose()
# np.linalg.det(arr) -> Determinant of 2-D matrix.
# np.linalg.inv(arr) -> Inverse of a matrix


l1 = [1,2,3]
a = np.array(l1)
print(a)

l2 = [[1,2,3],[4,5,6],[7,8,9]]
b = np.array(l2)
print(b)

# arange: print values with equal intervals.

c = np.arange(0,11)
print(c)

d = np.arange(0,11,2)
print(d)

# zeros and ones functions gives the arrays of zeroes and ones having number elements written in the parameter.

z = np.zeros((5,5))
print(z)

o = np.ones((5,5))
print(o)

# linspace gives the array of number over a specified interval.

e = np.linspace(0,10,20)
print(e)

# eye: Creates an identity matrix.

f = np.eye(4)
print(f)

# np.random.rand(5,5) is used to make the 5x5 array of random numbers.

# np.random.randn(5x5) is used to make the 5x5 array of random numbers but the numbers are closer to zero.

# np.random.randint(0,100) returns integer from 0 to 99.

# np.random.randint(0,100,10) returns array of size 10 from 0 to 99.

# np.random.seed(42) is used to fixed the random value. After it you have to write random.rand().

# arr.reshape(5x5) is used to convert 1D array into 2D array.

# arr.min(), arr.max() gives min and max value from an array.

# arr.argmin(), arr.argmax() gives index values of min and max from an array.

# Broadcasting: Using this you can change the multiple values in the list in the same iteration.

c[:] = 10
print(c)

# Arthimetic operations

print(a+a)
print(a*a)
print(a-a)
print(a/a)

# arr.sum(), arr.mean() gives sum and mean.

arr = np.arange(1,10)
print(arr.sum()) # Gives 45

newarr = arr.reshape(3,3)

print(newarr)

print(newarr.sum(axis=0)) # Add column-wise and return an array
print(newarr.sum(axis=1)) # Add row-wise and return an array

# arr.shape gives number of rows and columns

# frompyfunc() functions takes function,number of input arrays, number of output arrays.

def add(x,y):
    return x+y

myAdd = np.frompyfunc(add,2,1)

print(myAdd([1,2,3,4,5],[6,7,8,9,10]))

# np.add(l1,l2) adds the arrays.

# np.subtract(l1,l2) subtract the arrays.

# np.multiply(l1,l2) multiplies the array.

# np.divide(l1,l2) divides the array.

# np.power(l1,l2) makes the second argument power of the first argument.

# np.mod(l1,l2) gives the remainder.

# np.absolute(arr) gives the absolute values of the elements of the array.

# np.trunc() round off the decimals of elements of an array.
arr = np.array([3.55,3.45,3.89,3.2,3.5,-3.9,-3.5,-3.2])
newarr = np.trunc(arr) # Makes all the values 3.
print(newarr)

# np.around()
arr = np.array([3.55,3.45,3.89,3.2,3.5,-3.9,-3.5,-3.2])
newarr = np.array([3.559,3.4552,3.8945,3.258,3.558,-3.945,-3.525,-3.22])
print(np.around(arr))
print(np.around(newarr,2))

# np.floor(arr)
print(np.floor(arr))

# np.ceil(arr)
print(np.ceil(arr))

# np.unique(arr) removes the duplicates.

# np.union1d(arr1,arr2) gives the union of the array.

# np.setdiff1d(arr1,arr2) gives the difference of the array.

# np.gcd(num1,num2) gives the greatest common denominator.

# np.gcd.reduce(arr) gives the greatest common denominator of all elements of an array(returns int).

# np.lcm(num1,num2) gives the least common multiple.

# np.lcm.reduce(arr) gives the least common multiple of all elements of an array(returns int).

# np.diff(arr) subtracts two successive elements.

# np.prod(arr) gives product of all elements of an array.
arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,10])
print(np.prod(arr1))
x = np.prod([arr1,arr2]) # multiply like 1*2*3*4*5*6*7*8*9*10
print(x)

# np.cumsum(arr) adds two successive elements.

# Random Distributions
print(np.random.normal(loc = 1, scale = 1, size = (2,3)))
print(np.random.binomial(n=10,p=0.5,size=10))
print(np.random.poisson(lam=2, size=10))
print(np.random.uniform(low=0,high=1,size=(2,3)))
print(np.random.logistic(loc=1, scale=2, size=(2,3)))
