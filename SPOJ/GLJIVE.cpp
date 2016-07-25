#include <iostream>
#include <stdio.h>
using namespace std;

int main(){
	int sum,min,input,count;
	sum = min = count = 0;
	while (count < 10) {
		scanf("%d", &input);
		sum += input;
		if (sum == 100){
			cout << 100 <<endl;
			break;
		}
		else if(sum > 100){
			if ((sum - 100) == (100 - min)){
				cout <<sum <<endl;
			}
			else if((sum - 100) < (100 - min)){
				cout <<sum <<endl;
			}
			else{
				cout << min << endl;
			}
			break;
		}	
		else{
			min = sum;
		}
		count++;
	}
	if (sum < 100){
		cout << sum << endl;
	}
	return 0;
}

#DONE