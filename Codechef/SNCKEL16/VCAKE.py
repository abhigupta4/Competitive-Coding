def vcake(R, C, M, K,J):
	if (R*C) == M + K + J:
		if (not M%R) and (not K%R) and (not J%R) :
			return "Yes"
		if (not M%C) and (not K%C) and (not J%C):
			return "Yes"
		if not(M%R):
			if (not K%(C-(M/R))) and (not J%(C-(M/R))):
				return "Yes"
		if not(K%R):
			if (not M%(C-(K/R))) and (not J%(C-(K/R))):
				return "Yes"
		if not(J%R):
			if (not M%(C-(J/R))) and (not K%(C-(J/R))):
				return "Yes"
		if not(M%C):
			# print "yo"
			if (not K%(R-(M/C))) and (not J%(R-(M/C))):
				return "Yes"
		if not(K%C):
			if (not M%(R-(K/C))) and (not J%(R-(K/C))):
				return "Yes"
		if not(J%C):
			if (not M%(R-(J/C))) and (not K%(R-(J/C))):
				return "Yes"
	return "No"

for _ in xrange(input()):
	R, C, M, K,J = map(int,raw_input().split())
	print vcake(R,C ,M, K,J)