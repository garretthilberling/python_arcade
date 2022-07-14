import os

class params:
	s = 1
	options = [] # options will be assigned where this is called
	l = 3


def menu():
	clear = lambda: os.system('cls')
	clear()
	global params
	print(params.s)
	print("\n")
	print("Choose an option:")
	for i in range(1,params.l+1):
		print("{1} {0}. {3} {2}".format(i, ">" if params.s == i else " ", "<" if params.s == i else " ", params.options[i - 1]))

def up():
	global params
	if params.s == 1:
		return
	params.s -= 1
	menu()

def down():
	global selected
	if params.s == params.l:
		return
	params.s += 1
	menu()
