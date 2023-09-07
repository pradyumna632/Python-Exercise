# Check Armstrong Number
# abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + ....
# The Armstrong number in python is the number whose sum of each digit powered with 
# the total number of digits is the same as the given number.

num = int(input("Check Armstrong number: "))
summ = 0
length = len(str(num))
temp=num
while temp > 0:
    digit = temp%10
    summ += digit ** length
    temp //=10
    
if num==summ:
    print("Number is Armstrong")
else:
    print("Number is Not Armstrong")