# An ordered way of presenting data in python
a = list ((1,2,3,4))
b = ['a', 'b', 'c', 'd']
#print (type (b))
#print (a)
#print (b)
#print (a[0])
#print (b[2])
#print (len(a)) # count the number of items
a. append
#print (a)
b.remove ('c')
#print (b)

list1 = ['item1', 'item2', 'item3', 'item4', 'item5']
list2 = ['item6', 'item7']
list3 = list1 + list2
#print(list3)

fruit = ['Guava', 'Orange', 'Grape']
leaf = ['pumpkin', 'vegetable', 'Grean leaf']
fruit.extend(leaf)
#print(fruit)

for i in fruit:
    #print('I have'+ i)
    ### New List
    a = []
    b =list()
    #print (type(a))
    #print (type(b))
num = [1,2,3,4,5]
#print (len (num))   
#print (num [2])
names = ['John', 'Peter', 'Andrew', 'Philip']
#print (names [2])
names.append ("Kelvin")
#print (names)
names.insert (1, "Joy")
#print (names)
names.remove ("Philip")
#print (names)
popped_name = names.pop(4)
print ("Hello "+ popped_name)

names2 = ["George", 'Bassey', "Paul"]
name = names + names2
#print (name)

list1 = ["BMW", "Toyota", "Audi", "Benz"]
list2 = ['sequia', "Lexus"]
list1.extend(list2)
#print(list1)

#print(list1[0].lower())
#print(list1[0].capitalize())
#print('Toyota'in list1)

for i in list1:
    #print("I have " + i)
    
    print(list(range(1,10)))
   # print(list(range(1,10+1)))
    
    #list comprehension
    b = [x**2 for x in range(1,10+1)]
   # print(b)
    
    #Tuple
    () #Tuple
    [] #LiSt
    
    e = tuple()
    d = ()
    #print(type(e))
    #print(type(d))
    
    names [3] = 'Mathew'
    #print(names)
    
    loc = ('Uzoba', 'Obiri Kwere', 'Rumuosi')
    #print(loc)
    
    dd = list(loc)
    #print(dd)
    dd[2] = "NTA"
    dd.append("Rumuosi")
    #print(dd)
    
    y = (i.upper()for i in loc)
    #print(tuple(y))
    
    f1 = (1,2,3,4)
    f2 = (5,6,7,8)
    f3 = zip(f1,f2)
    #print (list(f3))
    #print(tuple(f3))
   # print(list1[:3])
    
    num = list(range(1,10+1))
   # print(num[:2])
    #print(num[:3])
    #print(num[::3])
    #print(num[4:])
    
    num2 = num[:]
    #print(num2)
    
    tt = list(loc).copy() 
   # print (tt)
    
    num3 = [2,3,4,2,4,5,4,2]
    num3.sort()
    #print(num3)
    
    num4 = [1,3,5,2,3,6,3,2,4,5]
    num4.reverse()
    #print(num4)
    
    num5 = [1,3,5,2,3,6,3,2,4,5]
    num5.sort(reverse=True)
   # print(num5)
    
    freq = max(num3, key=num3.count)
    #print(freq)
    
    x = [3,4,5,6,7,4]
    del x[1]
    #delx
    #print(x)
    
    #print(num4.count(5)
   # print(num4.index(3)
   
tup = ("a","b","c","d")
#print(tup[:2])
 
#print(tup[-2:])  
#print(len(x))
#print(x[3:])

#print(sorted(x))