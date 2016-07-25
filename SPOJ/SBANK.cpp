#include <iostream>
#include <map>
#include <string>
using namespace std;

int main(){
	int test,n;
	cin >> test;
	map<string,int> account_count;
	map<string,int>::iterator iter;
	string account;
	while(test > 0){
		cin >> n;
		account_count.clear();
		getline(cin,account);	
		while(n > 0){
			getline(cin,account);
			account_count[account]++;
			n--;
		}
		cout << endl;
		for(iter = account_count.begin(); iter != account_count.end(); ++iter)
		{
			cout << iter->first << " ";
			cout << iter->second << endl;
		//ignore value
		//Value v = iter->second;
		}
		cout << endl;
   		test--;
	}	
	return 0;

}

//DONE
