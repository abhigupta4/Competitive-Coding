#include <iostream>
using namespace std;

long long int max(long long int a,long long int b){
	if (a > b){
		return a;
	}
	else{
		return b;
	}
}

long long unsigned int sum(long long int arr[],int start,int stop){
	long long unsigned int sum = 0;
	for (int i = start; i <= stop; i++){
		sum += arr[i];
	}
	return sum;
}



int binary_search(long long int elem, long long int arr[],int size,int low){
	int high = size ;
	low = -1;
	int mid,midval;
	while(high >= low){
		mid = (low + high)/2;
		midval = arr[mid];
		if (midval > elem){
			high = mid - 1;
		}
		else if(midval < elem){
			low = mid + 1;
		}
		else{
			return mid;
		}
	}
	return -1;
}

int main(){
	while (1){
		int first,i,second,prev1,prev2,sum1,curr1,curr2;
		long long int sum2,sum_main,temp;
		cin >> first;
		if (first == 0){
			break;
		}
		long long int first_array[first];
		for(i = 0; i < first ; i++){
			cin >> first_array[i];
		}
		cin >> second;
		long long int second_array[second];
		for(i = 0;i < second; i++){
			cin >> second_array[i];
		}
		prev1 = prev2 = sum1 = sum2 = sum_main = 0;
		for(curr1 = 0; curr1 < first ; curr1++){
			curr2 = binary_search(first_array[curr1],second_array,second,0);
			if ( curr2 != -1){
				sum1 = sum(first_array, prev1, curr1);
				sum2 = sum(second_array,prev2,curr2);
				temp = max(sum1,sum2);
				sum_main += temp;
				prev1 = curr1 + 1;
				prev2 = curr2 + 1;
			}
		}
		if (prev1 != first){
			sum1 = sum(first_array,prev1,first - 1);
			sum2 = sum(second_array,prev2,second - 1);
			sum_main += max(sum1,sum2);
			prev2 = second;
		}
		if (prev2 != second){
			sum1 = sum(first_array,prev1,first - 1);
			sum2 = sum(second_array,prev2,second - 1);
			sum_main += max(sum1,sum2);
		}
		// else{
		// 	if (prev2 != second){
		// 		sum_main += sum(second_array,prev2,second - 1);
		// 	}
		// }
		cout << sum_main << endl;
	}
	return 0;
}

//DONE