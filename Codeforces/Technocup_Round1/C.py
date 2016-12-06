import sys

yo = sys.stdout.flush()

n = input()
print '? 1 2'
a1 = input()
yo
print '? 2 3'
a2 = input()
yo
print '? 1 3'
a3 = input()
yo

fir = (a1+a2+a3)/2 - (a2)
li = [fir,a1-fir,a3-fir]
for i in xrange(4,n+1):
	print '? 1 ' +  str(i)
	temp = input()
	li.append(temp-fir)
	yo

s = '!'
for ele in li:
	s += ' ' + str(ele)

print s
yo