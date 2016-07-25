from __builtin__ import pow

def power(n,k):
	

while True:
	n, k = map(int, raw_input().split())
	dict1 = {}
	if n and k:
		#print ((pow(n,k) + (2 * pow(n - 1,k)) + pow(n,n) + (2 * pow(n - 1,n- 1))))% 10000007
		print (pow(n,k,10000007) + (2 * pow(n - 1,k,10000007)) + pow(n,n,10000007) + (2 * pow(n - 1,n- 1,10000007)))  % 10000007
		#print pow(n,k,12);
	else:
		break