# solve quadratic euqation
# ax**2+bx+c=0

import cmath
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
c=int(input("Enter the value of c: "))

d=(b**2)-(4*a*c)

sol1=(-b-cmath.sqrt(d)/(2*a))
sol2=(-b+cmath.sqrt(d)/(2*a))

print(f"The answer to the quadratic equation will be {sol1} and {sol2}")