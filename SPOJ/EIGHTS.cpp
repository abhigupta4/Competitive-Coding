#include <iostream>
using namespace std;

int main(){
	int test;
	long long k,number;
	cin >> test;
	while (test > 0){
		cin >> k;
		// number = 182;
		// while(k > 0){
		// 	number += 10;
		// 	number_cube = 1;
		// 	for (int i = 0;i < 3 ; i++)
		// 	{
		// 		number_cube *= number;
		// 	}
		// 	//cout << number_cube / 1000;
		// 	if ((number_cube % 1000) == 888)
		// 	{
		// 		k--;
		// 	}	
		// }
		number = 192 + (k - 1) * 250;
		cout  << number << endl;
		test--;
	}
	return 0;
}

//DONE