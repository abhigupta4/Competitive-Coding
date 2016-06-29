#include <bits/stdc++.h>

using namespace std;

long int arr[10001];

long int getsum(int index){
	long int sum = 0;
	while(index > 0){
		sum += arr[index];
		index -= index & (-index);
	}
	return sum;
}

void update(int n,int index,int val){
	while(index <= n){
		arr[index] += val;
		index += index & (-index);
	}
}

void upd(int n,int start,int end,int val){
	update(n,start,val);
	update(n,end+1,-val);
}

int main(){
	int T,N,U,Q,st,end,val,temp;
	scanf("%d",&T);
	for(int t=0;t<T;t++){
		scanf("%d %d",&N,&U);
		for(int j = 0;j < N+1;j++){
			arr[j] = 0;
		}
		for(int u = 0;u<U;u++){
			scanf("%d %d %d",&st,&end,&val);
			upd(N,st+1,end+1,val);
		}
		scanf("%d",&Q);
		for(int q = 0;q<Q;q++){
			scanf("%d",&temp);
			printf("%d\n",getsum(temp+1));
		}
	}
	return 0;
}