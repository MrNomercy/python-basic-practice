##author: ricky
##date: 26 sep 2018
##decription: odd or even number
##date modified: 26 sep 2018


while True:
	num_input = int(input("please enter an odd or even number: "))

	if num_input%2 == 0:
		print(num_input,"is an even number.")
	elif num_input%2 != 0:
		print(num_input,"is an odd number.")
	else:
		print("invalid input.")
	print("")
