#AC
import sys
# sys.stdout.flush()

print 1
print 3,1,1,2
print 3,3,3,4
sys.stdout.flush()
res = input()
print 2
if res == 2:
	print 1
elif res == 1:
	print 2
elif res == 0:
	print 5
elif res == -1:
	print 4
elif res == -2:
	print 3