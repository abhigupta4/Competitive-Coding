#include <bits/stdc++>
#define max1 2147483647
using namespace std;

long int min(long int a,long int b){
	if a < b{
		return a;
	}
	return b;
}

int main(){
	unorderedmap<int,int> mymap;
	int empty,full,coins,weight,val;
	cin >> empty >> full;
	vector<long int> dp(full-empty + 1,max1);
	cin >> coins;
	int wt[coins];
	for(int i=0;i<coins;i++){
		cin >> val >> weight;
		mymap[weight] = val;
		wt[i] = weight;
	}
	dp[0] = 0;
	for(int i = 1;i < full-empty + 1;i++){
		for(int j = 0;j < coins;j++){
			if (wt[j] <= i){
				if dp[i-wt[j]] != max1{
					dp[i] = min(dp[i-wt[j]] + mymap[wt[j]],dp[i]);
				}
			}
		}
	}
	if (dp[full-empty] == max1){
		cout << "The minimum amount of money in the piggy-bank is " << dp[full-empty] << "." << endl;
	}
	else{
		cout << "This is impossible." << endl;
	}
	return 0;
}