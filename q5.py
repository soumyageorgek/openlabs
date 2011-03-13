def sum(l1):
	if len(l1) == 0:
		return 0
	return l1[0] + sum(l1[1:])

def sum(l1, s):
	if len(l1) == 0:
		return s
	return sum(l1[1:], s + l1[0])

