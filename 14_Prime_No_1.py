# Check Prime Number

# A prime number is a whole number greater than 1 whose only factors are 1 and itself.
# A factor is a whole number that can be divided evenly into another number.

prime_no = int(input("Enter the number to Check: "))
if prime_no > 1:
    for i in range(2,prime_no):
        if (prime_no % i == 0):
            print(prime_no,"is not a prime number")
            break
    else:    
        print(prime_no,"is a prime number")         
else:
    print(prime_no,"is not a prime number")