##author: ricky
##date: 26 sep 2018
##decription: convert farenheit to celcius
##C = (F-32)*5/9
##date modified: 26 Sep 2018
while True:
    user_input = int(input("please enter a number: "))

    def F_2_C(farenheit):
        celcius = (farenheit-32)*5/9
        return celcius

    result = F_2_C(user_input)
    print(user_input,"F =",result,"C")

