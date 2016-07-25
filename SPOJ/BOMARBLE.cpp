#include <iostream>
using namespace std;

int main(){
	int n,temp;
	while(1){
		cin >> n;
		if (n == 0){
			break;
		}
		n++;
		temp = (n*(3*n-1))/2;
		cout << temp;
	}
	return 0;
}