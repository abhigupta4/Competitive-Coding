#include <iostream>
#include <stdio.h>
using namespace std;

int main(){
	int count = 0;
	int open = 0;
	int close = 0;
	int test = 0;
	char brack;
	scanf("%c",&brack);
	while (brack != '-'){
		if (brack == '{' || brack == '}'){
			test++;
			open = close = count = 0;
			while(brack == '{' || brack == '}'){
				if (brack == '{'){
					open++;
				}
				else{
					if (open < (close + 1)){
						count++;
						open++;
					}
					else{
						close++;
					}
				}
				scanf("%c",&brack);
			}
			count += (open - close) / 2;
			// cout << "Open = "<<open << endl;
			// cout << "Close = " << close << endl;
			cout << test <<". "<< count << endl;
		}
		scanf("%c",&brack);
	}
	return 0;
}

//DONE