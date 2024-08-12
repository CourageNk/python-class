#Dictionaries && Set
d = {2}
print(type(d))

f = {1:20, 2:30}
print(type(f))

a = {1,1,2,4,3,2,3,5,4}
print(a)

c = {"a", "b", "c", "d", "a", "c", "b",}
print(c)

c.add("k")
print(c)

print(c.pop())
#c.remove("b")
print(c)

g = {"Car", "House", "Shop", "Church"}
r = {"Man", "Women", "Boy", "Girl", "Car" }

d = g.union(r)
print(d)

print(g.intersection(d))
print(g.symmetric_difference(r))

k = r.update(g)
print(k)

#Dictionaries

y = {"Age": "20", "Address": "Mgbuoba", "Hobby":"Dancing"}
print(y)
print(y['Age'])
print(y['Address'])

y['Mood'] = "Happy"
print(y)

y.update({"Rain": "Fall"})
print(y)

for c in g:
    print(c)

for x in y.keys():
    print(x)

for x in y:
    print(x)
    
    for k in y.values():
        print(k)
        
        for i,j in y.items():
            print(j,":",i)
            
            #Dict Comprehension
            u = {i for i in y.values()}
            print(u)
            
            l = {i for i in y.keys()}
            print(l)