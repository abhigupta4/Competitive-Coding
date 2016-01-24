#include <iostream>
using namespace std;

int main(){
	int j,i,N,M,sum,max;
	cin >> N >> M ;
	//cin>> M ;
	int value[N];
	max = sum = 0;
	for(i = 0;i < N ; i++){
		cin >> value[i];
	}
	j = 0;
	for(i = 0;i < N; i++){
		sum += value[i];
		while (sum > M){
			sum -= value[j];
			j++;
		}
		if (sum > max){
		    max = sum;
		}
	}
	cout << max;
	return 0;
}

#DONE