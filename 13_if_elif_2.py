# Find the Largest Among Three Numbers

num1 = int(input("enter number 1: "))
num2 = int(input("enter number 2: "))
num3 = int(input("enter number 3: "))

if (num1 > num2) and (num1 > num3):
    print("\n{0} is Greater than {1} and {2}".format(num1,num2,num3))
elif (num2 > num1) and (num2 > num3):
    print("\n{1} is Greater than {0} and {2}".format(num1,num2,num3))
else:
    print("\n{2} is Greater than {0} and {1}".format(num1,num2,num3))