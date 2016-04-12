import math
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modin(a, m):
    g, x, y = egcd(a, m)
    return x % m

def combi(a,b):
	mod = 10**9 + 7
	if a < b:
		return 0
	if a == 1:
		return 1
	if b < a/2:
		b = a - b
	temp = 1
	for i in range(b + 1,a + 1):
		temp = (temp * i%mod)%mod
	denom = modin(math.factorial(a-b),mod)
	# print denom
	return (temp%mod * denom%mod)%mod
	
for _ in range(input()):
	mod = 10**9 + 7
	string1 = raw_input()
	n = len(string1)
	dict1 = {}
	count = 0
	alpha = set()
	for ele in string1:
		if ele in dict1:
			dict1[ele] += 1
		else:
			dict1[ele] = 1
			alpha.add(ele)
			count += 1
 
	count_list = []
	total = 1
	rem = n
	for ele in alpha:
		total = (total % mod) * (combi(rem,dict1[ele]) % mod)%mod
		rem -= dict1[ele]
		count_list.append(dict1[ele])
 
	sum_list = [n - count_list[0]]
	for i in range(1,count):
		sum_list.append(sum_list[i - 1] - count_list[i])
 
	sub_2 = 0
	sub = 0
	for i in count_list:
		sub_2 += (n - i) * i
	sub_2 /= 2
	# print sub_2
 
	sub_3 = 0
	for i in range(count):
		for j in range(i + 1,count):
			sub_3 += count_list[i] * count_list[j] * sum_list[j]
 
	sub_3 = 2 * sub_3
 
	sub_4_4 = 0
	for i in range(count):
		for j in range(i + 1,count):
			for k in range(j + 1,count):
				sub_4_4 += count_list[i] * count_list[j] * count_list[k] * sum_list[k]
 
	sub_4_4 *= 3
	sub_4_2 = 0
	for i in range(count):
		for j in range(i + 1,count):
			sub_4_2 += (count_list[i] * (count_list[i] - 1) * count_list[j] * (count_list[j] - 1))/4
 
	sub_4_3 = 0
	for i in range(count):
		temp = 0
		for j in range(count):
			if j != i:
				temp += count_list[j] * (n - count_list[i] - count_list[j])
		temp /= 2
		sub_4_3 += ((count_list[i] * (count_list[i] - 1)) * temp)/2
		# print sub_4_3
	sub_4_3 *= 2
	# sub_4 = ((sub_4_2%mod + sub_4_3%mod) + sub_4_4%mod)%mod
	# sub_tot = ((sub_2%mod + sub_3%mod)%mod + sub_4%mod)%mod
	sub_4 = sub_4_3 + sub_4_4 + sub_4_2
	sub_tot = sub_2 + sub_3 + sub_4

	# print ((total * (total - 1)) - (total * sub_tot%mod))%mod
	# print ((total)* (total - 1 - (((sub_3 + sub_2)%mod + (sub_4_4 +sub_4_3)%mod)%mod + sub_4_2%mod)))% mod 
	print (total * (total - (sub_tot + 1)%mod)%mod)%mod