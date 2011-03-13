def sum_fn(l1, l2):
	sum = 0
	for x in range(l1,l2):
		sum += x
	return sum

def sum_list(l1):
	sum = 0
	for x in l1:
		sum += x
	return sum
 
print sum_fn(1, 4)
print sum_list([1, 7, 8])
i = 1
while i < 10:
	print "i = ", i 		
	i += 1
