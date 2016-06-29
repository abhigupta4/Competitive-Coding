#include <bits/stdc++.h>
using namespace std;
#define scd(a) scanf("%d",a);

int A[4100],B[4100],C[4100],D[4100];

int main(){
    unordered_map <int,int> sum1;
    sum1.reserve(16000000);
    int n;
    scd(&n);
    for(int i=0;i<n;i++){
        scd(&A[i]);
        scd(&B[i]);
        scd(&C[i]);
        scd(&D[i]);
    }
    // printf("%d",sum1[3]);
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
        	int s = A[i]+B[j]
        	if (sum1.count(s) == 0){
        		sum1[s] = 1
        	}
        	else{
    	        sum1[s]++;
        	}
            // printf("%d",A[i]);
        }
    }
    long long int count = 0;
    for(int i = 0;i<n;i++){
        for(int j=0;j<n;j++){
            count += sum1[-1*(C[i]+D[j])];
            // printf("%d",c)
        }
    }
    printf("%lld",count);
    return 0;
}