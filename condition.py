num = 20
age = 17
'''if num == 20:
   print("Above teenage age")
if age < 20:
    print("Teenage age")'''

# If & Else
name = "Bassey"
'''if name == "Philip":
    print("Name found")
else:
    print("Not user")'''

#if, elif, else
score = 90
'''if score == 40:
    print("D")
elif score <=60:
    print("C")
elif score <=70:
    print("B")
elif score > 70:
    print("A")
else:
    Print("F") '''
    
letter = "John"

if len(letter) > 6:
 print(letter)
else:
    print("You need more characters in your letter")
    
if type ("Hello") == str:
    print("This is a String")
else:
    print("This is not s String")
    
def calc(num1, num2):
    symbols =["+","-","*","/"]
    for symbol in symbols:
        if symbol =="+":
            print(num1 +num2)
        elif symbol =="-":
            print(num1-num2)
            
        elif symbol =="*":
            print(num1*num2)
        else:
            print(num1/num2)
                
calc(5,10)
        
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
        
if num1 > num2:
    print("Lucky user")
else:
    print("try again")
                