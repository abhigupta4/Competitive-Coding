#include <bits/stdc++.h>
using namespace std;

#define sld(a) scanf("%lld",&a)
#define pld(a) printf("%lld\n",a) 
#define ll long long
#define min1 -100000000000099

ll yo(ll val){
	if(val > 0){
		return val;
	}
	return 0;
}

struct seg{
	ll suff,pref,tot,seg1;
};

seg st[512345];
ll lis[112345];

seg comb(seg a,seg b){
	seg c;
	c.pref = max(a.pref,a.tot+b.pref);
	c.suff = max(b.suff,a.suff+b.tot);
	c.tot = a.tot+ b.tot;
	c.seg1 = max(a.seg1,max(b.seg1,a.suff+b.pref));
	return c;
}

void cons(ll start,ll end,ll node){
	if(start == end){
		st[node].suff = st[node].pref = st[node].tot = st[node].seg1 = lis[start];
		return;
	}
	ll mid = (start+end)/2;
	ll le = 2*node+1;
	ll ri = 2*node+2;
	cons(start,mid,le);
	cons(mid+1,end,ri);
	st[node] = comb(st[le],st[ri]);
	return;
}

void update(ll start,ll end,ll node,ll pos){
	if(start == end){
		st[node].suff = st[node].pref = st[node].tot = st[node].seg1 = min1;
		return ;
	}
	ll mid = (start+end)/2;
	ll le = 2*node+1;
	ll ri = 2*node+2;
	if(pos <= mid){
		update(start,mid,le,pos);
	}
	else{
		update(mid+1,end,ri,pos);
	}
	st[node] = comb(st[le],st[ri]);
	return ;
}

int main(){
	ll n;
	sld(n);
	int order[n];
	for(ll i=0;i<n;i++){
		sld(lis[i]);
	}
	for(int j=0;j<n;j++){
		scanf("%d",&order[j]);
	}
	cons(0,n-1,0);
	for(int i=0;i<n;i++){
		update(0,n-1,0,order[i]-1);
		pld(yo(st[0].seg1));
	}
	return 0;
}
