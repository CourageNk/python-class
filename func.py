def name(fname, lname):
    return f"{fname} {lname}"

def add(num1, num2):
    return num1 * num2

def divide(num):
    return num/2

def addsub(num1,num2):
    return num1 + num2 -20

print(addsub(10,5))

#Lambda Function
d = lambda num : num * 2
print(d(10))

s = lambda fname, lname : f'Hello {fname} {lname}'
print(s('John', 'Moses'))

def multiply(n):
    return lambda x : x * n

f = multiply(10)
print(f(5))

#Map Function
#x = tuple(map(lambda n: n * 5, [4,5,6,7,5]))
x = list(map(lambda n: n * 5, [4,5,6,7,5] ))
print(x)

y = list(map(lambda n,t : n** t, [1,2,3,4],[5,6,7,8]))
print(y)

g = list(map(addsub, [2,4,5,6],[4,6,7,8]))
print(g)

#Filter Function

def Calsub(num1):
    if (num1 + 5) % 2 == 0:
        return num1 + 5
    else:
        return False
    
rt = list(filter(Calsub, [1,2,3,4,5,6,7,8]))
print(rt)    

u = tuple(filter(lambda n : n if n % 3 == 0 else False, [2,3,4,9,12,15,18,16]))
print(u)

from functools import reduce
#reduce

lis = reduce(lambda a,b: a if a < b else b, [2,4,5,6,7])
print(lis)

yer = reduce(lambda a,b: a if a > b else b, [2,4,5,6,7])
print(yer)

ge = reduce(lambda a,b: a+b, [2,4,5,6,7])
print(ge)