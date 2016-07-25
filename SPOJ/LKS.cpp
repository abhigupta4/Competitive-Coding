#include <bits/stdc++.h>
#define l long
#define pb push_back

long int dp[2][2000001]
int v[12345678],w[12345678];

int main(){
	int K,N,flag=0;
	scanf("%d %d",&K,&N);
	for(int n=0;n<N;n++){
		scanf("%d %d",&v[n],&w[n]);
	}
	memset(dp,0,sizeof dp);
	for(int n=0;n<N;n++){
		for(int k=0;k<K;k++){
			if (w[n]>k){
				dp[!flag][k] = dp[flag][k];
			}
			else{
				dp[!flag][k] = max(dp[flag][k],v[n]+dp[flag][k-wt[n]])
			}
		}
	}
	printf("%ld",dp[flag][K]);
	return 0;
}