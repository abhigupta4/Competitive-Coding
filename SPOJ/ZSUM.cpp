#include <iostream>
#include <math.h>

using namespace  std;

int main(){
	int n,k;
	cin >> n >> k;
	cout << (pow(n,k) + (2 * pow(n-1,k)) + pow(n,n) + (2 * pow(n-1,n-1))) % 10000007 ;
	return 0;
}