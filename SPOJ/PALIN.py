def palin(string_list):
	n = len(string)
	temp = ''
	if n == 1:
		return '11'
	if all9(string):

		temp += '1'
		for i in xrange(n-1):
			temp += '0'
		temp += '1'
		return temp
	else:
		mid = n/2
		leftsmaller = 0
		i = mid-1
		if n%2:
			j = mid+1
		else:
			j = mid
		while(i >= 0 and string_list[i] == string_list[j]):
			i -= 1
			j += 1

		if (i<0 or string_list[i] < string_list[j]):
			leftsmaller = 1
		while i >= 0:
			string_list[j] = string_list[i]
			j += 1
			i -= 1

		if leftsmaller:
			carry = 1
			i = mid-1
			if n%2:
				string_list[mid] += carry
				carry = string_list[mid]/10
				string_list[mid] %= 10
				j = mid+1
			else:
				j = mid
			while i >= 0:
				string_list[i] += carry
				carry = string_list[i] / 10
				string_list[i] %= 10
				string_list[j] = string_list[i]
				j += 1
				i -= 1
		for ele in string_list:
			temp += str(ele)
		return temp

def all9(string):
	for ele in string:
		if ele != '9':
			return 0
	return 1

list1 = []
for _ in xrange(input()):
	string = raw_input()
	print palin(map(int,list(string)))	