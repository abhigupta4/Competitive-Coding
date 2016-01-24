while(True):
	a, b = map(int,raw_input().split())
	count = 0
	if (a + b) == 0:
		break
	else:
		attackers = map(int,raw_input().split())
		min_attack = 10000
		for attack_dist in attackers:
			if attack_dist < min_attack:
				min_attack = attack_dist
		defenders = map(int,raw_input().split())
		for defence_dist in defenders:
			if defence_dist <= min_attack:
				count += 1
	if (count > 1):
		print "N"
	else:
		print "Y"

#DONE