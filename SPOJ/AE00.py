import math
number_of_squares = int(raw_input())
rectangles_sum = 0
for i in range(1,int(math.sqrt(number_of_squares)) + 1):
	rectangles_sum += (number_of_squares / i) - (i - 1)
print rectangles_sum

