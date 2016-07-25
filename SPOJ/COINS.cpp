#include <iostream>
#include <stdio.h>
#include <map>
#include <string>

using namespace std;

map<long long int,long long int> dict;

long long int coins_bank(long long int  number){
	return  (number / 2) + (number / 3) + (number /4);
}

long long int bytelandian(long long int coins){
	if (coins == 0){
		return 0;
	}
	if (dict.find(coins) != dict.end()){
		return dict[coins];
	}
	if(coins > coins_bank(coins)){
		dict[coins] = coins;
		return coins;
	}
	else{
		long long int a,b,c;
		a = bytelandian(coins / 2);
		dict[coins / 2] = a;
		b =  bytelandian(coins / 3) ;
		dict[coins /3 ] = b;
		c = bytelandian (coins / 4);
		dict[coins /4] = c;
		return a + b + c;
	}	
	
}
int main(){
	long long int number,byte;
	dict.clear();
	while(scanf("%lld", &number) != -1){
		byte = bytelandian(number);
		dict[number] = byte;
		cout << byte << endl;

	}
	return 0;
}

//DONE