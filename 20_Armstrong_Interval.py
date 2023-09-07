# Find Armstrong Number in an Interval

lower = int(input("Enter Lower value: "))
upper = int(input("Enter Upper value: "))

for num in range(lower,upper+1):
    
    sum1=0
    length = len(str(num))
    
    temp = num
    
    while temp>0:
        digit = temp%10
        sum1 += digit**length
        temp//=10

    if num==sum1:
        print(num)