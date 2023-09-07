# Find the Sum of Natural Numbers

# Natural numbers refer to a set of all the whole numbers excluding 0.
# These numbers are significantly used in our day-to-day activities and speech.
# Natural numbers, also known as non-negative integers(all positive integers). 
# Few examples include 23, 56, 78, 999, 100202, and so on.

natural_num = int(input("Enter Number: "))

if natural_num < 0:
    print('Enter the positive number')
else:
    sum1=0
    while (natural_num>0):
        sum1=natural_num*(natural_num+1)/2
    print(sum1)