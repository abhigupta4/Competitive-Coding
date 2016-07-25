#include <iostream>
#include <algorithm>

using namespace std;

long long int min1(long long int a,long long int b){
    if(a <= b){
        return a;
    }
    else{
        return b;
    }
}

int main(){
	long long int test,n,i,j;
	test = 1;
	while(1){
		cin >> n;
		if(n == 0){
			break;
		}
		long long int arr1[n][3];
		for(i = 0;i < n;i++){
			for(j = 0;j < 3;j++){
				cin >> arr1[i][j];
			}
		}
		long long int arr2[n][3];
		long long int temp;
		arr2[0][0] = arr1[0][1];
		arr2[0][1] = arr1[0][1];
		arr2[0][2] = arr1[0][2] +arr1[0][1];
		for(i = 1;i < n;i++){
			for(j = 0;j < 3;j++){
				if(j == 0){
				    temp = *min_element(arr2[i -1],arr2[i-1] + 2);
					arr2[i][j] = arr1[i][j] + temp;
				}
				else if(j == 1){
				    temp = *min_element(arr2[i-1],arr2[i-1] + 3);
					arr2[i][j] = arr1[i][j] + min1(arr2[i][j-1],temp );
				}
				else{
				    temp = min1(arr2[i-1][1],arr2[i-1][2]);
					arr2[i][j] = arr1[i][j] + min1(arr2[i][j-1], temp);
				}
			}
		}
		cout <<test<< ". " <<arr2[n-1][1] << endl;
        test++;
	}
	return 0;
}

//DONE