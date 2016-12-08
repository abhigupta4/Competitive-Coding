n,a = map(int,raw_input().split())
li = map(int,raw_input().split())
a -= 1
co = 0
fr = a-1
bk = a+1

if li[a]:
	co += 1
while (fr >= 0 and bk < n):
	if li[fr] and li[bk]:
		co += 2

	fr -= 1
	bk += 1

while (fr >=0 ):
	if li[fr]:
		co += 1

	fr -= 1

while(bk < n):
	if li[bk]:
		co += 1

	bk += 1

print co