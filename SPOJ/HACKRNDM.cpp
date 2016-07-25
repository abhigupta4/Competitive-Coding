#include <bits/stdc++.h>

using namespace std;

int main(){
	int n,k;
	scanf("%d %d",&n,&k);
	int arr1[n],count = 0;
	unordered_map<int,int> ele;
	for(int i = 0;i<n;i++){
		scanf("%d",&arr1[i]);
		ele[arr1[i]] = 1;
	}
	sort(arr1,arr1 + n);
	for(int i = 0;i<n;i++){
		if (ele.find(arr1[i]+k) != ele.end()){
			count += 1;
		}
	}
	printf("%d",count);
	return 0;
}