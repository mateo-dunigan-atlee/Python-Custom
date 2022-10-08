def collatz(seed_, include_first = True):
	if include_first:
		yield seed_
	while seed_ != 1:
		if seed_ % 2 == 0:
			seed_ /= 2
		else:
			seed_ = seed_ * 3 +1
		yield seed_
		
		
	
	
	


for x in collatz(3):
	print(x)
print(list(collatz(3)))