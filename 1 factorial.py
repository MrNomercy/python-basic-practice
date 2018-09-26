# author: ricky
# date: 26 sep 2018
# description: factorial excercise
# 4! = 4X3X2X1
# date modified: 26 sep 2018

while True:
        user_input = int(input("please enter a number: "))
        fatorial = 1
        for i in range(user_input,1,-1):
                fatorial *= i      

        print(user_input,"! = ",fatorial)




