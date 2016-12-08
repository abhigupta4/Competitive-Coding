n = input()
if n ==1 or n == 2:
	print -1
else:
	if n%2:
		print (n**2 - 1)/2,(n**2 + 1)/2
	else:
		print (n**2/4 -1),(n**2/4 + 1)