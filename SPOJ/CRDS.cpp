#include <iostream>
using namespace std;

int main(){
	int test,level;
	cin >> test;
	int count;
	while (test > 0){
		cin >> level;
		count = 2 * level;
		while(level > 0){
			count += (level - 1) * 3;
			level-- ;
		}
		cout << count % 1000007 << endl;
		test-- ;
	}
	return 0;
}