#include <iostream>
#include <math.h>

#define MOD 10000007

using namespace std;

long long int fast_exp(long long int base,long long int exp){
	if (exp == 0){
		return 1;
	}
	if (exp == 1){
		return base % MOD;
	}
	if (exp % 2 == 0){
		long long temp = fast_exp(base,exp / 2) % MOD;
		return (temp * temp) % MOD;
	}
	else{
		long long temp = fast_exp(base,exp /2 ) % MOD;
		return ((base % MOD) * ((temp * temp)% MOD)) % MOD;
	}
}

int main(){
	long long int n,k,i,j,temp1,temp2,temp3,temp4,fin;
	cin >> n >> k;
	while ((n + k) != 0){
		temp1 = fast_exp(n, n) % MOD;
		temp2 = fast_exp(n, k) % MOD;
		temp3 = (2 * (fast_exp(n - 1, n- 1)% MOD)) % MOD;
		temp4 = (2 * (fast_exp(n - 1, k )%MOD)) % MOD;
		fin = (((temp1 + temp2) % MOD) + ((temp3 + temp4) % MOD)) % MOD;
		cout << fin << endl;
		cin >> n >> k;
	}
	return 0;
}

//DONE