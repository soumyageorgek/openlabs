def foobar(arg):
	if arg == []:
		return arg
	else:
		return foobar(arg[1:]) + [ arg[0] ]

foobar([2, 6, 1])

