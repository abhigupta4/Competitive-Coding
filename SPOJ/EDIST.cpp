#include <iostream>
#include <string>
using namespace std;

int min_func(int a,int b,int c){
	if(a < b){
		if(a < c){
			return a;
		}
		else{
			return c;
		}
	}
	else{
		if(b < c){
			return b;
		}
		else{
			return c;
		}
	}
}

int main(){
	int temp[20][20];
	int test,i,j,lenA,lenB;
	string A,B;
	cin >> test;
	getline(cin,A);
	while(test > 0){
		getline(cin,A);
		getline(cin,B);
		lenA = A.length();
		lenB = B.length();
		cout << A <<"  "<<B;
		for(i = 0;i < lenA + 1;i++){
			temp[0][i] = i;
		}
		for(j = 0; j < lenB + 1;j++){
			temp[j][0] = j;
		}
		for(i = 1;i < lenB + 1;i++){
			for(j = 1;j < lenA + 1;j++){
				if(A[j - 1] == B[i - 1]){
					temp[i][j] = temp[i - 1][j - 1];
				}
				else{
					temp[i][j] = min_func(temp[i-1][j-1], temp[i -1][j], temp[i][j - 1]) + 1;
				}
			}
		}
		cout << temp[lenB][lenA];
		test--;
	}
	
	return 0;
}