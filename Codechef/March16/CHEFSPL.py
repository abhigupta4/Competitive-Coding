def chef_spl(string1):
	len1 = len(string1)
	if(len1 == 1):
		return "NO"
	if (len1 % 2) == 0:
		if string1[:(len1/2)] == string1[(len1/2):]:
			return "YES"
		else:
			return "NO"
	else:
		half = len1 / 2
		if string1[1:half + 1] == string1[half + 1:]:
			return "YES"

		#Element to be deleted is on left half
		count = 0
		left_shift = 0
		while (count < half):
			if string1[count + left_shift] == string1[count + half + 1]:
				count += 1
			elif string1[count + 1] == string1[count + half + 1]:
				left_shift = 1
				count += 1
			else:
				break

		if count == half:
			return "YES"

		#Element to be deleted is on right half

		count = 0
		right_shift = 0
		while (count < half):
			if string1[count] == string1[count + half + right_shift]:
				count += 1
			elif string1[count] == string1[count + half + 1]:
				right_shift = 1
				count += 1
			else:
				break

		if count == half:
			return "YES"

		return "NO"

for _ in range(input()):
	string1 = raw_input()
	print chef_spl(string1)

#AC