#include <iostream>
using namespace std;

int max(int arr[], int k,int offset){
	int max,i;
	max = i = 0;
	while (i < k){
		if (arr[i + offset] > max){
			max = arr[i + offset];
		}
		i++;
	}
	return max;
}

int main(){
	int n,i,k,offset;
	cin >> n;
	int array[n];
	i = 0;
	while (i < n ){
		cin >> array[i];
		i++;
	}
	cin >> k;
	offset = 0;
	while (offset < (n - k) + 1){
		cout << max(array, k , offset) <<" " ;
		offset ++;
	}
	return 0;
}

#DONE