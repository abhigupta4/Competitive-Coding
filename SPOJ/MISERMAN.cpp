#include <iostream>
using namespace std;

int min_three(int a, int b, int c){
	if (a < b){
		if( a < c){
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

int min_array(int arr[],int length){
	int mini = arr[0];
	for(int j = 0;j < length ; j++){
		if (arr[j] < mini){
			mini = arr[j];
		}
	}
	return mini;
}

int main(){
	int T,C,R;
	int input[101][101];
	int temp[102][102];
	int i,j,current_input;
	
	cin >> R;
	cin >> C;
	for(i = 0; i < C + 2 ; i++){
		temp[0][i] = 0;
	}
	for(i = 0; i < R + 1 ; i++){
		temp[i][0] = 101;
		temp[i][C + 1] = 101;
	}
	for(i = 1; i < R + 1; i++){
		for(j = 1; j < C + 1; j++){
			cin >> current_input;
			temp[i][j] = current_input + min_three(temp[i - 1][j - 1],temp[i - 1][j], temp[i - 1][j + 1]);
		}
	}
	cout << min_array(temp[R], C + 2) << endl;
	
	// for (i = 0;i < R + 1;i++){
	// 	for(j = 0; j <C +2 ;j++){
	// 		cout << temp[i][j];
	// 	}
	// 	cout << endl;
	// }
	return 0;
}

//DONE