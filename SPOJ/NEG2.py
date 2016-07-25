def cowm(numb):
	ans = ''
	if numb == 0:
		return '0'
	elif numb == 1:
		return '1'
	elif numb > 0:
		sum1 = 1
		cur = 1
		count = 1
		while(numb > sum1):
			count += 2
			cur *= 4
			sum1 += cur
	else:
		sum1 = -2
		cur = -2
		count = 2
		while (numb < sum1):
			count += 2
			cur *= 4
			sum1 += cur
	temp = cowm(numb-cur)
	ans = '1' + '0'*(count-len(temp)-1) + temp
	return ans

print cowm(input())