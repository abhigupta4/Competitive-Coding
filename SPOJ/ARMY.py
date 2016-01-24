for _ in range(input()):
	raw_input()
	NG, NM = map(int,raw_input().split())
	mini = min(NG, NM)
	NG_array = map(int,raw_input().split())
	NM_array = map(int,raw_input().split())
	NG_max = max(NG_array)
	NM_max = max(NM_array)
	if (NG_max < NM_max):
		print "MechaGodzilla"
	else:
		print "Godzilla"

#DONE