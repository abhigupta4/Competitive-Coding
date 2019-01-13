n = input()
lis = map(int, raw_input().split())
temp = [0]
for ele in lis:
    temp.append(temp[-1]+ele)

q = input()

def search_choc(l,r,val):
    mid = (l+r)/2
    if temp[mid] < val:
        return search_choc(mid+1,r,val)
    elif temp[mid] == val or temp[mid-1] < val:
        return mid
    else:
        return search_choc(l,mid-1,val)
        

for _ in xrange(q):
    choc = input()
    print search_choc(0,n,choc)