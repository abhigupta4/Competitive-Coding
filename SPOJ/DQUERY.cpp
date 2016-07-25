#include <bits/stdc++.h>
#define sd(a) scanf("%d",&a)
#define pd(a) printf("%d\n",a)
#define N 210000
#define A 1234567
#define B 460

using namespace std;

int cnt[A],arr[N],ans[N],answer = 0;

struct node{
	int l,r,i;
}q[N];

bool cmp(node x,node y){
	if (x.l/B != y.l/B){
		return x.l/B < y.l/B;
	}
	return x.r < y.r;
}

void add(int pos){
	cnt[arr[pos]]++;
	if(cnt[arr[pos]] == 1){
		answer++;
	}
}

void remove(int pos){
	cnt[arr[pos]]--;
	if(cnt[arr[pos]] == 0){
		answer--;
	}
}

int main(){
	int n,query,currentL,currentR,L,R;
	sd(n);
	for(int i=0;i<n;i++){
		sd(arr[i]);
	}
	sd(query);
	for(int i=0;i<query;i++){
		sd(q[i].l);sd(q[i].r);
		q[i].i = i;
		q[i].l--;
		q[i].r--;
	}

	sort(q,q+query,cmp);

	currentR = 0;
	currentL = 0;
	for (int i = 0; i < query; i++)
	{
		L = q[i].l;
		R = q[i].r;
		while(currentL < L) {
			remove(currentL);
			currentL++;
		}
		while(currentL > L) {
			add(currentL-1);
			currentL--;
		}
		while(currentR <= R) {
			add(currentR);
			currentR++;
		}
		while(currentR > R+1) {
			remove(currentR-1);
			currentR--;
		}
		ans[q[i].i] = answer;
	}
	for(int i=0;i<query;i++){
		pd(ans[i]);
	}
	return 0;
}