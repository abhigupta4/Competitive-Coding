#include <iostream>
#include <string>
using namespace std;

int main(){
	int end;
	char space;
	cin >> end;
	cout << "\n";
	string encrypt;
	while (end != 0){
		cout << end;
		getline(cin, encrypt);
		cout << end;
		cout << endl << encrypt;
		cin >> end;
	}
	return 0;
}