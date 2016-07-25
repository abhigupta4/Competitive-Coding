#include <iostream>
#include <string>

using namespace std;

string willitst(int n){
	while(n > 1){
		if((n % 2) != 0){
			return "NIE";
		}
		n /= 2;
	}
	return "TAK";
}

int main(){
	int long long number;
	cin >> number;
	int flag = 0 ;
	while(number > 1){
		if((number % 2) != 0){
			cout << "NIE";
			flag = 1;
			break;
		}
		number /= 2;
	}
	if (flag == 0){
			cout << "TAK";
	}
	return 0;
}