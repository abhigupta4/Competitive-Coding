#include <iostream>
using namespace std;

int main() {
	int number;
	cin >> number ;
	while ( number != 0){
		cout << (number * (number + 1) *((2 * number) + 1))/6 <<endl;
		cin >> number;
	}

	return 0;
}
