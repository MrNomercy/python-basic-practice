##author: ricky
##date: 26 sep 2018
##description: quadratic eqution solver
##date modified: 27 sep 2018

import cmath
while True:
        print("quadratic equation form: ax^2 + bx + c = 0")
        print("Please enter the value of a,b,c to find roots")
        print("")

        A = float(input("enter the value of a: "))
        B = float(input("enter the value of b: "))
        C = float(input("enter the value of c: "))

        def quadratic_equ(a,b,c):
            delta = b**2 - 4*a*c
            x_1 = (-b-cmath.sqrt(delta))/(2*a)
            x_2 = (-b+cmath.sqrt(delta))/(2*a)
            return print('X1 =',x_1,'; X2 =',x_2)

        print("")
        result = quadratic_equ(A,B,C)
        print(result)
        print("")
