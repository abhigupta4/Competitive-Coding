#include <iostream>
using namespace std;

int abs(int numb){
	if (numb >= 0){
		return numb;
	}
	else{
		return numb * -1;
	}
}

int main(){
	int T,N,M;
	int i,j,temp;
	cin >> T;
	while (T > 0){
		cin >> N;
		int N_arr[N];
		for (i = 0; i< N; i++){
			cin >> N_arr[i];
		}
		cin >> M;
		int M_arr[M];
		for(j = 0; j < M;j++){
			cin >> M_arr[j];
		}
		int min = 1000001;
		for ( i = 0; i < N; i ++){
			for(j = 0;j < M; j ++){
				temp = abs(M_arr[j] - N_arr[i]);
				if ( temp < min){
					min = temp;
				}
			}
		}
		cout  << min << endl;
		T--;
	}
	return 0;
}

//DONE