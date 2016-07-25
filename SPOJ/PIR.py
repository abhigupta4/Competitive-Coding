import math
for _ in range(input()):
	u, v, w, W, V, U = map(int,raw_input().split())
	u1 = v**2 + w**2 - U**2
	v1 = w**2 +  u**2 - V**2
	w1 = u**2 + v**2 - W**2
	temp = (4 * u**2 * v**2 * w**2) - (u*u1)**2 - (v * v1)**2 - (w* w1)**2 + (u1 * v1 * w1)
	volume = (1/12.0) * math.sqrt(temp)
	print ("%.4f") % (volume)

#DONE