# Make a Simple Calculator

def add(x,y):
    return x + y

def sub(num1,num2):
    return num1 - num2

def mul(num1,num2):
    return num1 * num2

def div(num1,num2):
    return num1 / num2

print('''Enter your choice:
        1) Addition
        2) Subtraction
        3) Multiplication
        4) Division''')

choice = int(input())

if choice == 1:
        num1 = int(input("Enter number 1: "))
        num2 = int(input("Enter number 2: "))
        print(num1 ,"+", num2, "= ",add(num1,num2)) 
        
elif choice == 2:
        num1 = int(input("Enter number 1: "))
        num2 = int(input("Enter number 2: "))
        print(num1 ,"-", num2, "= ",sub(num1,num2))
        
elif choice == 3:
        num1 = int(input("Enter number 1: "))
        num2 = int(input("Enter number 2: "))
        print(num1 ,"*", num2, "= ",mul(num1,num2)) 
        
elif choice == 4:
        num1 = int(input("Enter number 1: "))
        num2 = int(input("Enter number 2: "))
        print(num1 ,"/", num2, "= ",div(num1,num2))
else:
    print("Enter Valid Choice! :)")