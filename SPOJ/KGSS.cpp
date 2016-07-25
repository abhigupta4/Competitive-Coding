#include <bits/stdc++.h>
#define sd(x) scanf("%d",&x)
#define sdc(ch) scanf("%c ",&ch)
#define pd(a) printf("%d\n",a)
#define pii pair<int,int>
#define F first
#define S second
#define mp make_pair

using namespace std;

int arr[100010];
pii st[520000];

pii comp1(int a,int b,int c,int d){
	if(arr[a] >= arr[c]){
		if(arr[b] >= arr[c]){
			return mp(a,b);
		}
		else{
			return mp(a,c);
		}
	}
	else{
		if(arr[d] >= arr[a]){
			return mp(c,d);
		}
		else{
			return mp(c,a);
		}
	}
}

void build(int idx, int start, int end){
    if(start == end){
    	st[idx].F = start;
    	st[idx].S = 100002;
        return;
    }
    int mid = (start + end) / 2;
    int le = 2*idx+1;
    int ri = 2*idx+2;
    build(le, start, mid);
    build(ri, mid+1, end);
    st[idx] = comp1(st[le].F,st[le].S,st[ri].F,st[ri].S);
} 

pii query(int index, int start, int end, int l, int r)
{
    if(r < start or end < l){
        pii temp;
        temp.F = temp.S = 100002;
        return temp;
    }
    if(l <= start and end <= r)
    {
        return st[index];
    }
    int mid = (start + end) / 2;
    int le = 2*index+1;
    int ri = 2*index+2;
    pii left = query(le, start, mid, l, r);
    pii right = query(ri, mid+1, end, l, r);
    return comp1(left.F,left.S,right.F,right.S);
}

void update(int pos,int start,int end,int idx,int val){
    if (start == end){
        arr[idx] = val;
        return;
    }
    int mid = (start + end)/2;
    int le = 2*pos + 1;
    int ri = 2*pos + 2;
    if(idx >= start && idx <= mid){
        update(le,start,mid,idx,val);
    }
    else{
        update(ri,mid+1,end,idx,val);
    }
    pii left = st[le];
    pii right = st[ri];
	st[pos] = comp1(left.F,left.S,right.F,right.S);
}

int main(){
	int n,start,end,q;
	char ch;
	sd(n);
	for(int co=0;co<n;co++){
		sd(arr[co]);
	}
	arr[100002] = -1;
	build(0,0,n-1);
	sd(q);
	sdc(ch);
	for(int i=0;i<q;i++){
		sdc(ch);sd(start);sd(end);
// 		printf("%c",ch);
// 		pd(start);
// 		pd(end);
		if (ch == 'U'){
			update(0,0,n-1,start-1,end);
// 			pd(1);
		}
		else{
			pii temp = query(0,0,n-1,start-1,end-1);
// 			pd(2);
			pd(arr[temp.F]+arr[temp.S]);
		}
		sdc(ch);
	}
	return 0;
}