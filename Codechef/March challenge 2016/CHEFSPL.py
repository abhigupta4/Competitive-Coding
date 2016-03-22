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
		count = 0
		del1 = 0
		left_shift = 0
		right_shift = 0
		while (count < half):
			if (count + 1 + right_shift + half) < len1:
				if string1[count + left_shift] == string1[count + 1 + right_shift + half]:
					count += 1
					continue
				else:
					pass
			if string1[count + 1] == string1[count + 1 + half]:
				if del1 > 0:
					break
				if (count + 2 + half) < len1 :
					if string1[count + 2] == string1[count + 2 + half]:
						left_shift = 1
						del1 = 1
						count += 1
						continue
					else:
						pass
				else:
					count += 1
					break
			if (count + 2 + half) < len1:
				if string1[count] == string1[count + 2 + half]:
					if del1 > 0:
						break
					if (count + 3 + half) < len1:
						if string1[count + 1] == string1[count + 3 + half]:
							right_shift = 1
							del1 = 1
							count += 1
							continue
						else:
							break
					else:
						count += 1
						break
				else:
					break
			else:
				break

		if count == half:
			return "YES"

		count = 0
		del1 = 0
		left_shift = 0
		right_shift = 0
		while (count < half):
			if (count + right_shift + half) < len1:
				if string1[count + left_shift] == string1[count + right_shift + half]:
					count += 1
					continue
				else:
					pass
			if string1[count + 1] == string1[count + half]:
				if del1 > 0:
					break
				if (count + 1 + half) < len1:
					if string1[count + 2] == string1[count + 1 + half]:
						left_shift = 1
						del1 = 1
						count += 1
						continue
					else:
						pass
				else:
					count += 1
					break
				
			if (count + 1 + half) < len1:
				if string1[count] == string1[count + 1 + half]:
					if del1 > 0:
						break
					if (count + 2 + half) < len1:
						if string1[count + 1] == string1[count + 2 + half]:
							right_shift = 1
							del1 = 1
							count += 1
							continue
						else:
							break
					else:
						count += 1
						break
				else:
					break
			else:
				break

		if count == half:
			return "YES"

		return "NO"


for _ in range(input()):
	string1 = raw_input()
	print chef_spl(string1)