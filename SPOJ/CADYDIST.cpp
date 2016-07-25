#include <iostream>
#include<algorithm>
#include<stdio.h>

using namespace std;

int main(){
	long long int N,i,sum;
	while(1){
		scanf("%lld",&N);
		if (N == 0){
			break;
		}
		sum = 0;
		long long int C[N],S[N];
		for(i = 0;i < N;i++){
			scanf("%lld",&C[i]);
		}
		for(i = 0;i < N;i++){
			scanf("%lld",&S[i]);
		}
		sort(C,C + N);
		sort(S,S + N);
		for(i = 0;i < N;i++){
			sum += C[i] * S[N-i-1];
		}
		printf("%lld",sum);
	}
	return 0;
}
//DONE