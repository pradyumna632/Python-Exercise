# Find the Factorial of a Number
# The factorial of a number is the product of all the integers from 1 to that number.
# Factorial is not defined for negative numbers, and the factorial of zero is one, 0! = 1

num = int(input("Enter the number: "))
fact=1

if num < 0 :
    print("fact is not less than 0")
elif num == 0:
    print("The factrial of 0 is 1")
else:
    for i in range(1,num+1):
        fact = fact*i
    print("The factorial :", fact)    