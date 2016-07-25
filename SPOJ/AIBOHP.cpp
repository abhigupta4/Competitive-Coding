#include <bits/stdc++.h>
using namespace std;

string str1;
int dp[6200][6200];

int compute(){
	int len1 = str1.length();
	for(int i = 0;i <= len1;i++){
		for(int j = 0;j <= len1;j++){
			if ((i == 0) || (j==0)){
				dp[i][j] = 0;
			}
			if(str1[j-1] == str1[len1-i]){
				dp[i][j] = dp[i-1][j-1] + 1;
			}
			else{
				dp[i][j] = max(dp[i-1][j],dp[i][j-1]);
			}
		}
	}
	return len1 - dp[len1][len1];
}

int main(){
	int test;
	scanf("%d",&test);
	getline(cin,str1);
	for(int t=0;t<test;t++){
		getline(cin,str1);
		printf("%d",compute());
	}
	return 0;
}