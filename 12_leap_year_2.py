# Check Leap Year

num = int(input("enter number: "))

if (num % 4 == 0 and num % 400) and (num % 100 != 0):
    print("{0} is a Leap Year".format(num))
else:
    print("{0} is not a Leap Year".format(num))