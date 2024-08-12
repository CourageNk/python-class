from func import divide

print(divide(10))
print(len(range(10)))

# Lambda Functions
x = lambda y : y *2
print(x(10))

name = lambda fname, lname : f'How are you {fname} {lname}'
print(name("John", "Bright"))

b = list(map(lambda x: x/3, [15,30,45,60]))
print(b)

def name(b):
    return f"Hello {b}"

c = list(map(lambda x :f"Hello {x}", ['John', "Kenny", "Brian", "Paul"]))
print(c)
g = list(map(name, ['John', "Kenny", "Brian", "Paul"]))
print(g)

def user(fname, lname):
    return f"How are you {fname} {lname}"

t = tuple(map(user, ["John", "Bassey", "Kenny"],["Bright", "Paul", "Andrew"]))
print(t)

#filter
y = list(filter(lambda num : num if num % 2 == 0 else False, [1,2,3,4,5,6,7,8,9,10]))
print(y)

def add(num):
    c = lambda x: x + num
    return c

d = add(20)
f = d(10)
print(f)

from functools import reduce
#Reduce
xy = reduce(lambda a,b : a if a > b else b, [1,2,3,4,5,6])
print(xy)

er = reduce(lambda c, d : c if c < d else d, [10,44,11,12,9] )
print(er)



