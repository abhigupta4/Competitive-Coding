#include <iostream>
using namespace std;

int max_three(int a, int b, int c){
	if (a > b){
		if( a > c){
			return a;
		}
		else{
			return c;
		}
	}
	else{
		if(b > c){
			return b;
		}
		else{
			return c;
		}
	}
}

int max_array(int arr[],int length){
	int maxi = arr[0];
	for(int j = 0;j < length ; j++){
		if (arr[j] > maxi){
			maxi = arr[j];
		}
	}
	return maxi;
}

int main(){
	int T,C,R;
	int input[101][101];
	int temp[102][102];
	int i,j,current_input;
	cin >> T;
	while(T > 0){
		cin >> R;
		cin >> C;
		for(i = 0; i < C + 2 ; i++){
			temp[0][i] = 0;
		}
		for(i = 0; i < R + 1 ; i++){
			temp[i][0] = 0;
			temp[i][C + 1] = 0;
		}
		for(i = 1; i < R + 1; i++){
			for(j = 1; j < C + 1; j++){
				cin >> current_input;
				temp[i][j] = current_input + max_three(temp[i - 1][j - 1],temp[i - 1][j], temp[i - 1][j + 1]);
			}
		}
		cout << max_array(temp[R], C + 2) << endl;
		T--;
	}

	return 0;
}

//DONE