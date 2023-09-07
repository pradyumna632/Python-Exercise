# Print the Fibonacci sequence
# The Fibonacci sequence is, by definition, 
# the integer sequence in which every number after the first two is the sum of the two preceding numbers
def fib(n):
    a=0
    b=1
    
    if n == 1:
        print(n)
    else:
        print(a)
        print(b)
        
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)

fib(5)        