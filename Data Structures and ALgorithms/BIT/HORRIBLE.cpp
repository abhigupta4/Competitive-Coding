#include <bits/stdc++.h>

using namespace std;

long int arr[123456];
long int arr2[123456];

long int getsum(int index){
	long int sum1,sum2;
	long int temp = index;
	sum1 = 0;
	while(index > 0){
		sum1 += arr[index];
		index -= index & (-index);
	}
	sum2 = 0
	index = temp;
	while(temp > 0){
		sum2 += arr2[temp];
		temp -= temp & (-temp);
	}
	return sum1*index - sum2;
}

void update(int n,int index,int val,int temp[]){
	while(index <= n){
		temp[index] += val;
		index += index & (-index);
	}
}

void upd(int n,int start,int end,int val){
	update(n,start,val,arr);
	update(n,end+1,-val,arr);
	update(n,start,v*(start-1),arr2);
	update(n,end+1,- (v*end),arr2)
}

int main(){
	int T,N,C,Q,st,end,val,temp,first;
	scanf("%d",&T);
	for(int t=0;t<T;t++){
		scanf("%d %d",&N,&C);
		for(int j = 0;j <= N;j++){
			arr[j] = 0;
			arr2[j] = 0;
		}
		for(int c=0;c<C;c++){
			scanf("%d",&first);
			if (first == 0){
				scanf("%d %d %d",&st,&end,&val);
				upd(N,st,end,val);
			}
			else{
				scanf("%d %d",&st,&end);
				printf("%d",getsum(end)-getsum(st-1));
			}
		}

	}
	return 0;
}