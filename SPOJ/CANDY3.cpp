#include <iostream>
#include <string>
#include <cstdlib>
using namespace std;

int main(){
	string line;
	int test;
	int number,sum,count;
	getline(cin,line);
	cin >> test;
	while (test > 0){
		do{
			cin >> line;
			number = atoi(line);
			cout << number <<endl;
			count++;
		}while(!line.empty());

		if ((sum % number) == 0){
			cout << "YES" <<endl;
		}
		else{
			cout << "NO" << endl;
		}
		test--;

	}
	return 0;
}