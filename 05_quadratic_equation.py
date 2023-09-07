# Solve Quadratic Equation 

# ax2 + bx + c
# where,
# a, b, and c are coefficient and real numbers and also a ≠ 0.
# If a is equal to 0 that equation is not valid quadratic equation.
import math

a=1
b=4
c=2

dis = (b ** 2 - 4 * a *c )

quad1 = (-b + math.sqrt(dis))/ (2 * a) 
quad2 = (-b - math.sqrt(dis))/ (2 * a) 

print("The Roots are:")
print(quad1)
print(quad2)