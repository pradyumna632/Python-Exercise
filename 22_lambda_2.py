# Numbers Divisible by Another Number
# find all numbers divisible by 2

list1 = [1,2,3,4,5,6,7,8,9,10]
num_div = lambda x:  x % 2==0
print(list(filter(num_div,list1)))