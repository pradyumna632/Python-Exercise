# Print all Prime Numbers in an Interval

start = int(input("Enter start :"))
end = int(input("Enter end :"))

for num in range(start,end):
    if num > 1:
        for i in range(2,num):
            if (num % i == 0):
                break
        else:
                print(num)