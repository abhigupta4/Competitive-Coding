#include <iostream>
#include <vector>
#include <stdio.h>
#include <math.h>

using namespace std;

long long min(long long a,long long b){
	if (a<b){
		return a;
	}
	return b;
}

void build(vector<long long> &st,long long arr[],int pos,int start,int end){
	if (start == end){
		st[pos] = arr[start];
		return;
	}
	int mid = (start + end)/2;
	int le = 2*pos + 1;
	int ri = 2*pos + 2;
	build(st,arr,le,start,mid);
	build(st,arr,ri,mid+1,end);
	st[pos] = min(st[le],st[ri]);
}

long long r_query(vector<long long> &st,int idx,int start,int end,int q_s,int q_e){
	if(q_e < start || q_s > end){
		return (pow(10,9) + 5);
	}
	if (q_s <= start && q_e >= end){
		return st[idx];
	}
	int mid = (start + end)/2;
	int l = 2*idx + 1;
	int r = 2*idx + 2;
	return min(r_query(st,l,start,mid,q_s,q_e),r_query(st,r,mid+1,end,q_s,q_e));
} 

int main(){
	int T,N,Q,q_s,q_e;
	scanf("%d",&T);
	for(int i = 0;i < T;i++){
		scanf("%d %d",&N,&Q);
		long long arr[N];
		vector<long long> seg_t(4*N);
		for(int j = 0;j < N;j++){
			scanf("%lld",&arr[j]);
		}
		build(seg_t,arr,0,0,N-1);
		printf("Scenario #");
		printf("%d",i+1);
		printf(":\n");
		printf("\n");
		for(int k = 0;k < Q;k++){
			scanf("%d %d",&q_s,&q_e);
			printf("%lld\n",r_query(seg_t,0,0,N-1,q_s-1,q_e-1));
		}
	}
	return 0;
}

//AC