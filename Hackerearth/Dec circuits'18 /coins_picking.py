test = input()
for _ in xrange(test):
    n, k = map(int, raw_input().split())
    if k == 1:
        if n%2 == 0:
            print 'Bob'
        else:
            print 'Alice'
    else:
        cur = k
        while(n>=0):
            if(n >= 2*cur):
                n -= 2*cur
                cur *= k
            elif(n>=cur):
                print 'Alice'
                break
            else:
                print 'Bob'
                break