#include <bits/stdc++.h>
using namespace std;
#define ll long long
int main(){
	ll price,n,x,q;
	ll temp;
	ll ans[101050];
	cin >> n;
	for(int i=0;i< n;i++){
		cin >> price;
		ans[price]++; 
	}
	for(int i = 1;i<101000;i++){
		ans[i] += ans[i-1];
	}
	cin >> q;
	for(int i =0;i<q;i++){
		cin >> temp;
		if (temp > 100100){
			cout << n << endl;
		}
		else{
			cout << ans[temp] << endl;
		}
	}
	return 0;
}