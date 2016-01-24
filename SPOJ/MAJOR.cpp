#include <iostream>
#include <stdio.h>
#include <string.h>
#include <map>
using namespace std;

int main(){
	int test,temp;
	long long int count,n,maxi,data;
	scanf("%d",&test);
	while (test > 0){
		maxi = 0;
		scanf("%lld", &n);
		count = n;
		map<int, int> dict;
		while(n > 0){
			scanf("%d", &temp);
			dict[temp]++;
			if (dict[temp] > maxi){
				maxi = dict[temp];
				data = temp;
			}
			n--;
		}
		if (maxi > (count / 2)){
			printf("%s", "YES ");
			printf("%d", data);
			cout << endl;
		}
		else{
			printf("%s", "NO ");
			cout << endl;
		}
		test--;
	}
	return 0;
}

//DONE