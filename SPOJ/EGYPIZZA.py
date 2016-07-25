one_quarter = three_quarter = half = 0
half_left = 0
number = 1
for _ in range(input()):
	quantity = (raw_input())
	if quantity == "1/2":
		half += 1
	elif quantity == "3/4":
		three_quarter += 1
	else:	
		one_quarter += 1

if half % 2 :
	number += (half / 2) + 1
	half_left = 1
else:
	number += half / 2

if three_quarter >= one_quarter :
	number += three_quarter
	three_quarter = 0
else:
	number += three_quarter
	one_quarter -= three_quarter
	if half_left:
		if one_quarter <= 2:
			one_quarter = 0
		else:
			one_quarter -= 2		
	if one_quarter % 4:
		number += (one_quarter / 4 ) + 1
	else:
		number += one_quarter / 4
print number