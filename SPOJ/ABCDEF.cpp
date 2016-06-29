#include <bits/stdc++.h>
using namespace std;
#define ll long long 

unordered_map<ll,int> left;
unordered_map<ll,int> right;

int main(){
	int N;
	scanf("%d",&N);
	int arr[N];
	for(int i =0;i<N;i++){
		scanf("%d",&arr[i]);
	}
	for(int i =0;i<N;i++){
		for(int j = 0;j<N;j++){
			for(int k=0;k<N;k++){
				left[arr[i]*arr[j] + arr[k]]++;
				if(arr[k] != 0){
					right[arr[k]*(arr[i]+arr[j])]++;
				}
			}
		}
	}
	ll count = 0;
	for(auto it = right.begin();it != right.end();++it){
		count += (it->second) * left[it->first];
	}
	// for(int i =0;i<N;i++){
	// 	for(int j = 0;j<N;j++){
	// 		for(int k=0;k<N;k++){
	// 			if (arr[k]!=0){
	// 				count += first[arr[k]*(arr[j]+arr[i])];
	// 			}
	// 		}
	// 	}

	// 	}
	// }
	printf("%lld",count);
	return 0;
}