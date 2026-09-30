def do_something(zahl):
	if zahl < 2:
		return False

	for teiler in range(2, zahl):
		if zahl % teiler == 0:
			return False

	return True
