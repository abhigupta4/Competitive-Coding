#include <iostream>
#include <stdio.h>

#define MOD 1000000007

using namespace std;

int main(){
	long long int N,K,i,j;
	scanf("%lld",&N);
	long long int A[100001],B[100001],temp1,temp2;
	temp1 = temp2 = 0;
	for(i = 0;i< N;i++){
		scanf("%lld",&A[i]);
		A[i] += i + 1;
		temp1 = ((A[i] % MOD) + (temp1%MOD))%MOD;
	}
	for(i = 0;i< N;i++){
		scanf("%lld",&B[i]);
		B[i] += i + 1;
		temp2 = ((B[i]%MOD) + (temp2%MOD))%MOD;
	}
	K = N;
	while(K > 0){
		printf("%lld ", ((temp2%MOD) * (temp1%MOD) % MOD);
		temp2 = temp1 = 0;
		for(j = 0;j < K - 1;j++){
			A[j] = max(A[j],A[j + 1]);
			//temp1 = ((A[j] % MOD) + (temp1%MOD))%MOD;
			temp1 += A[j] ;
			B[j] = max(B[j],B[j + 1]);
			// temp2 = ((B[j]%MOD) + (temp2%MOD))%MOD; 
			temp2 += B[j];
		}
		K--;
	}
	return 0;
}