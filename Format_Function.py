'''
Output Formatting in python :
    The string format() method formats the given string into a nicer output in Python.
'''
# x,y=10,5
# print("The Value of x is {} and y is {}".format(x,y))

# print('I love {0} and {1}'.format('bread','butter'))
# print('I love {1} and {0}'.format('bread','butter'))

# users = ['Pradyumna', 'Parth', 'Krushna']
# Password  = ['Python', 'Java', 'C++']
# for i in range(0, len(users)):
#     template = "Tech Stack of {1} is {0}"
#     print(template.format(users[i],Password[i]))

import math
me = "Pradyumna"
cal = 3 
a = f" This is {me} {cal} {4*10} {math.sin(45)}"
print(a)
