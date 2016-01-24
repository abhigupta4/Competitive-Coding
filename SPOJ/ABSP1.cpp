#include <iostream>

using namespace std;

int main(){
	int T,N;
	for(int i = 0;i< T;i++){
		long long int arr[N];
		for(i = 0;i< N;i++){
			cin >> arr[i];
		}
		long long int sum,tot_sum,first;
		first = arr[0];
		sum = tot_sum = 0;
		for(i = 1;i<N;i++){
			sum += arr[i] - first;
		}
		tot_sum += sum;
		for(i = 1;i < N - 1;i++){
			tot_sum += sum - (N - i)*(arr[i] - first);
		}	
		cout << tot_sum << endl;
	}
	return 0;
}

//DONE