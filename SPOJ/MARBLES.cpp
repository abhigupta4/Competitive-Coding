#include <iostream>
using namespace std;

long long nCr(long long int n,long long int r){
	if (r > n - r){
		r = n - r;
	}
	long long int ans = 1;
	int i;
	for(i = 0; i < r; i++){
		ans = ans * (n-i)/(i+1);
	}

	return ans;
}

int main(){
	int test;
	long long int N, K, ans,f1,f2;
	cin >> test;
	while (test > 0){
		cin >> N;
		cin >> K;
		cout << nCr(N - 1,K - 1) << endl;
		test--;
	}

	return 0;
}

//DONE