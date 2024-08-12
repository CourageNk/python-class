def num ():
  #  print ("Today is Monday!")
#num()
    return "Today is Monday!"
#print(num())
#print(num())
#print(num())

def add():
    #return 2 + 5
   # return 2 * 5
   return 2 - 5
#print(add())

def addTwoNum(num):
    return num + 10

#print(addTwoNum(20))

def username(fname, lname):
    #print(f'Your name is {fname} {lname}')
    #print('Your name is ' +fname+" "+lname)
    
#username("John", "Doe")

  #def calculate(num1, num2):
    symbols = input("Choose from this symbols '+', '-', '*', '/',")
    if symbols == '+':
        return(num1+num2)
    elif symbols == '-':
        return(num1-num2)
    elif symbols == '/':
        return(num1/num2)
    elif symbols =='*':
        return(num1*num2)
    
#print(calculate(10,5))

#FirstName = input("Enter Your first Name: ")
#LastName = input("Enter Your last Name: ")

def User(first, last):
    return f"Welcome {first} {last}"

#print(User(FirstName, LastName))

l = [2,5,4,6,7,8,11,12]
def calc (arr):
    d = []
    for i in arr:
        if i % 2==0:
            d.append(i*2)
           # print(d)
            
        else:
            d.append(i)
           # print(i)
            
calc(l)
    
l = [2,5,4,6,7,8,11,12]
def calce (arr):
    for i in arr:
        if i % 2==0:
            print(i*2)
        else:
            print(i)
            
#calce(l)
    
def Greet(user="Mark"):
    return f"Good evening {user}"

#print(Greet())
#print(Greet("Peter"))

#first = input("Enter your first name: ")
#last = input("Enter your last name: ")
#middle = input("Enter your middle name: ")

def salute(first, last, middle=""):
    if middle == "":
        print(f"{first} {last}") #Print(f"{first} {middle} {last}")
    else:
        print(f"{first} {middle} {last}") #print(f"{first} {last}")
        
#salute(first, last, middle)

#Functions with keyword argument
def dog(name, breed):
    return f'I have a dog named {name} whose breed is {breed}'
#print(dog("Willie", "Shiwawa")) #keyword argument
#print(dog(breed='Shiwawa', name='Willie')) # positional argument

def thingsToBuy(meat, oil, Rice):
    print(f"I just bought {meat} meat")
    print(f"I just bought {oil} oil")
    print(f"I just bought {Rice} rice")
    
thingsToBuy("Goat", "Red", "Foreign",) #Keyword argument
thingsToBuy(Rice="Foreign", meat="Goat", oil="Vegetable") # positional argument!!

def play(name, *args): 
    return f"This user is called {name} and has a {args[1]}"

print(play("Moses", "car", "house",))

#Functions with multipe positional arguments
def sleep(bed,**args):
    
    args['bed'] = bed
    return f"I sleep on {args} {bed}"

print(sleep("roll", water="water", foam="foam"))

def run(person, *type, **types):
    types['person'] = person
    return f"{person} runs {type[1]} and has {type}"

print(run('Sandra', "100 meters", "200 meters", jump="High Jump", Relay="Senior Relay"))
