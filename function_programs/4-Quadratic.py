'''a program Quadratic.java to find the roots of the equation a*x*x + b*x + c.
Since the equation is x*x, hence there are 2 roots. The 2 roots of the equation
can be found using a formula (Note: Take a, b and c as input values)
delta = b*b - 4*a*c
Root 1 of x = (-b + sqrt(delta))/(2*a)
Root 2 of x = (-b - sqrt(delta))/(2*a)'''

a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
c = int(input("Enter the value of c : "))

delta = b*b - 4*a*c
root1 = (-b + (delta**0.5))/(2*a)
root2 = (-b - (delta**0.5))/(2*a)

print(f"Root 1: {root1}, Root 2: {root2}")