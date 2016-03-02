#include <iostream>
#include <stdio.h>
#include <ctype.h>
#include <math.h>

using namespace std;

int main(){
	int test;
	scanf("%d",&test);
	long double check;
	unsigned long long number;
	unsigned long long test2;
	unsigned long long root,temp;
	int flag = 0;
	for(int temp2 = 0; temp2 < test;temp2++){
		scanf("%llu",&number);
		root = sqrt(number);
		//cout <<"test is" << test;
		flag = 0;
		temp = 0;
		while(temp <= root ){
			check = sqrt(number - (temp*temp));
			//cout << check;
			test2 = check;
			//cout << test2;
			if (test2 == check){
				flag = 1;
				break;
			}
			temp++;
		}
		if (flag == 1){
			printf("%s\n","Yes");
		}
		else{
			printf("%s\n","No");
		}
	}
	return 0;
}

//DONE