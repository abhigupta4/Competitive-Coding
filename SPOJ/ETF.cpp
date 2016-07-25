#include <iostream>
using namespace std;

int totient(int numb){
	int result = numb;
	int i;
	for(i = 2; i * i <= numb; i++){
		if((numb % i) == 0){
			result -= result / i;
		}
		while ((numb % i) == 0){
			numb /= i;
		}
	}
	if (numb > 1){
		result -= result/numb;
	}
	return result;
}

int main(){
	int test,n;
	cin >> test;
	while (test > 0){
		cin >> n;
		cout << totient(n) << endl;
		test--;
	}	
	return 0;
}

//DONE